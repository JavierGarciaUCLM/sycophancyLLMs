import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv
import anthropic
from openai import OpenAI
#from google import genai as genai_google

# Configuration 
load_dotenv(Path(__file__).parent.parent / ".env")

ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
#GEMINI_KEY = os.getenv("GEMINI_API_KEY")

MODELS = {
    "claude": "claude-sonnet-4-5",
    "gpt4o": "gpt-4o"
    #"gemini": "models/gemini-2.0-flash",
}

VERSIONS = ["neutral_version", "medium_version", "emotional_version"]

INPUT_FILE = Path("data/prompts_en.json")
OUTPUT_DIR = Path("data/responses")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DELAY = 1.5 # delay for rate limits

#clients take
anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
openai_client = OpenAI(api_key=OPENAI_KEY)
#gemini_client = genai_google.Client(api_key=GEMINI_KEY)
groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

#api calls
def call_claude(prompt: str) -> str:
    response = anthropic_client.messages.create(
        model=MODELS["claude"],
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def call_gpt4o(prompt: str) -> str:
    response = openai_client.chat.completions.create(
        model=MODELS["gpt4o"],
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

#def call_gemini(prompt: str) -> str:
    #response = gemini_client.models.generate_content(
       # model=MODELS["gemini"],
        #contents=prompt
    #)
   # return response.text

def call_groq(prompt):
    r = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return r.choices[0].message.content

CALLERS = {
    "claude": call_claude,
    "gpt4o": call_gpt4o,
    #"gemini": call_gemini,
    "groq": call_groq
}

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    prompts = data["prompts"]
    total = len(prompts) * len(VERSIONS) * len(CALLERS)
    done = 0

    for prompt_obj in prompts:
        pid = prompt_obj["id"]

        for version in VERSIONS:
            text = prompt_obj[version]

            for model_name, caller in CALLERS.items():
                output_file = OUTPUT_DIR / f"{pid}_{version}_{model_name}.json"

                if output_file.exists():
                    done += 1
                    print(f"[SKIP] {output_file.name}")
                    continue

                try:
                    response_text = caller(text)
                    result = {
                        "id": pid,
                        "version": version,
                        "model": model_name,
                        "prompt": text,
                        "response": response_text,
                        "factual_error": prompt_obj["factual_error"],
                        "correct_source": prompt_obj["correct_source"]
                    }

                    with open(output_file, "w", encoding="utf-8") as out:
                        json.dump(result, out, ensure_ascii=False, indent=2)

                    done += 1
                    print(f"[{done}/{total}] OK: {output_file.name}")
                    time.sleep(DELAY)

                except Exception as e:
                    print(f"[ERROR] {pid} / {version} / {model_name}: {e}")
                    time.sleep(DELAY)

    print(f"\nDone. {done}/{total} responses collected.")
    print(f"Results saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()