# Empatía Sintética y Sycophancy en LLMs

> **Estado:** En desarrollo activo - Fase 1: Diseño del dataset

Estudio empírico sobre si el diseño de empatía sintética mediante RLHF induce sycophancy factual en grandes modelos de lenguaje cuando el usuario presenta errores con carga emocional.

## Pregunta de investigación

¿En qué medida el diseño de empatía sintética mediante RLHF induce sycophancy factual en LLMs cuando el usuario presenta errores con carga emocional, y varía este efecto entre modelos con distintas filosofías de alineamiento?

## Motivación

Los modelos de lenguaje comerciales actuales están entrenados para generar respuestas percibidas como empáticas mediante RLHF. Este diseño puede producir un efecto no deseado: cuando un usuario presenta un error factual acompañado de carga emocional, el modelo puede priorizar la validación emocional sobre la corrección factual.

Este fenómeno conecta directamente con casos documentados de daño psicológico derivado de interacciones con LLMs y con las preocupaciones regulatorias del AI Act (UE 2024/1689).

## Diseño experimental

- **Modelos evaluados:** Claude Sonnet (Anthropic), GPT-4o (OpenAI), Gemini 1.5 Pro (Google)
- **Dataset:** 30 errores factuales verificables × 3 niveles de carga emocional = 90 prompts
- **Etiquetado:** LLM-como-juez con validación manual en muestra estratificada
- **Métrica principal:** tasa de sycophancy por modelo y nivel emocional

### Niveles de carga emocional

| Nivel | Descripción |
|-------|-------------|
| Neutra | Pregunta directa sin posicionamiento |
| Media | El usuario cree el error sin urgencia emocional |
| Alta | Implicación personal, falsa evidencia, pregunta de confirmación |

### Dominio del dataset

**Duelo y pérdida** - creencias erróneas ampliamente extendidas sobre 
el proceso de duelo que la psicología científica actual desmiente o 
matiza significativamente. Se excluyen aspectos religiosos o espirituales 
de la pérdida por carecer de ground truth verificable.

Referencias de autoridad: Worden (2009), Bonanno (2004), Stroebe & Schut (1999)...


## Hipótesis

Los modelos entrenados con RLHF orientado a empatía sintética mostrarán tasas de sycophancy significativamente más altas ante prompts de alta carga emocional que ante el mismo error presentado de forma neutra, y esta diferencia variará entre modelos según su filosofía de alineamiento.

## Contexto académico

Este proyecto es el componente empírico complementario al Trabajo Fin de Grado *"Empatía Sintética en la IA Generativa: Análisis Técnico y Evaluación Ética, Moral y Legal para su Futura Aplicación"* (UCLM, Escuela Superior de Ingeniería Informática, 2025).

## Estado de las fases

- [x] Revisión de literatura
- [x] Diseño experimental
- [ ] Construcción del dataset
- [ ] Recolección de datos
- [ ] Etiquetado y validación
- [ ] Análisis estadístico
- [ ] Redacción del paper

## Autor

**Javier García Tercero**  
Grado en Ingeniería Informática - UCLM (ESIIAB)  
[GitHub](https://github.com/JavierGarciaUCLM) · [LinkedIn](www.linkedin.com/in/javier-garcia-tercero)

## Licencia

MIT - los datos y el código son de libre uso con atribución.