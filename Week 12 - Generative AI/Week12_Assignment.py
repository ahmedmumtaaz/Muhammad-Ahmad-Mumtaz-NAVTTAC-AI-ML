# Week 12: Generative AI basics and prompt engineering exercises
def prompt_builder(task,context,constraints,format="bullets"):
    return f"Task: {task}\nContext: {context}\nConstraints: {constraints}\nFormat: {format}"
print(prompt_builder("Explain supervised learning","Intro ML course notes","Use beginner language; avoid unsupported facts","5 bullet points"))
# Prompt design checklist: role, task, relevant context, constraints, output format, examples if needed.
# Assignment: create prompts for summarization, extraction and question answering.
# Test each prompt with an answerable, unanswerable and ambiguous input.
# Evaluate response: relevance, factuality, completeness, clarity, safety (1-5 rating).
# Build a course-notes assistant prompt that must answer from supplied notes and admit when context lacks an answer.
# Reflection: define hallucination, grounding, tokenization, LLM, privacy risks and 2 useful applications/limitations.
# This script is a prompt template demo, not a hosted model inference.