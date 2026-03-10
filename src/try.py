import os
from google import genai as genai_google
from dotenv import dotenv_values
from pathlib import Path

config = dotenv_values(Path(__file__).parent.parent / ".env")
GEMINI_KEY = config.get("GEMINI_API_KEY")

client = genai_google.Client(api_key=GEMINI_KEY)
for m in client.models.list():
    print(m.name)