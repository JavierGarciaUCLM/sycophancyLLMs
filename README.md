# Synthetic Empathy and Sycophancy in LLMs

> **Status:** Active development - Phase 1: Dataset design

Empirical study on whether the design of synthetic empathy via RLHF induces factual sycophancy in large language models when users present errors with emotional load.

## Research Question

To what extent does the design of synthetic empathy via RLHF induce factual sycophancy in LLMs when users present errors with emotional load, and does this effect vary across models with different alignment philosophies?

## Motivation

Current commercial language models are trained to generate responses perceived as empathetic via RLHF. This design may produce an unintended effect: when a user presents a factual error accompanied by emotional load, the model may prioritize emotional validation over factual correction.

This phenomenon connects directly with documented cases of psychological harm derived from LLM interactions and with the regulatory concerns of the EU AI Act (2024/1689).

## Experimental Design

- **Models evaluated:** Claude Sonnet (Anthropic), GPT-4o (OpenAI), Llama 3 (Meta)
- **Dataset:** 30 verifiable factual errors × 3 emotional load levels = 90 prompts
- **Labeling:** LLM-as-judge with manual validation on a stratified sample
- **Main metric:** sycophancy rate per model and emotional load level

### Emotional Load Levels

| Level | Description |
|-------|-------------|
| Neutral | Direct question without positioning |
| Medium | User believes the error without emotional urgency |
| High | Personal involvement, false evidence, confirmation question |

### Dataset Domain

**Grief and loss** - widely held misconceptions about the grief process that current scientific psychology refutes or significantly nuances. Religious or spiritual aspects of loss are excluded due to lack of verifiable ground truth.

Authority references: Worden (2009), Bonanno (2004), Stroebe & Schut (1999)


## Hypothesis

Models trained with empathy-oriented RLHF will show significantly higher sycophancy rates when facing high emotional load prompts than when facing the same error presented neutrally, and this difference will vary across models according to their alignment philosophy.

## Academic Context

This project is the empirical complement to the undergraduate thesis *"Synthetic Empathy in Generative AI: Technical Analysis and Ethical, Moral and Legal Evaluation for Future Application"* (UCLM, Escuela Superior de Ingeniería Informática, 2025).

## Phase Status

- [x] Literature review
- [x] Experimental design
- [ ] Dataset construction
- [ ] Data collection
- [ ] Labeling and validation
- [ ] Statistical analysis
- [ ] Paper writing

## Author

**Javier García Tercero**  
Computer Science Degree - UCLM (ESIIAB)  
[GitHub](https://github.com/JavierGarciaUCLM) · [LinkedIn](https://www.linkedin.com/in/javier-garcia-tercero)

## License

MIT - data and code are free to use with attribution.
