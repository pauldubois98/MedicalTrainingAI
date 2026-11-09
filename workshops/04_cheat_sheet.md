---
title: "Cheat sheet — Using AI as a healthcare educator"
---

# Cheat sheet: using AI as a healthcare educator

## How AI works

1. An **LLM predicts text**, token by token: its answer is the most *plausible* continuation, not necessarily the *true* one.
2. It only knows what it learned during **training** (frozen at a cutoff date) and what is in its **context** (the conversation).
3. **RAG** automatically adds relevant passages from a knowledge base to the context, and the answer cites them.
4. **Agents** use tools (web search, PubMed, documents, email) to fetch information or act, and add the results to their context.

## Writing a good request

| | Example |
|---|---|
| **Role** | “You are an experienced nursing educator.” |
| **Context** | “My students are in Year 1, before their first placement.” |
| **Task** | “Write 10 multiple-choice questions on hand hygiene.” |
| **Format** | “As a table: question, 4 options, answer, one-line explanation.” |
| **Sources** | “Base your answer only on the attached guideline, and cite the section.” |
| **Iterate** | “Make questions 3 and 7 harder. Add a clinical scenario.” |

## Useful requests

- **Explain:** “Explain [concept] to a Year 1 student, with an analogy, then check my understanding with 3 questions.”
- **Visual:** “Draw a diagram of [process]” · “Compare [A, B, C] in a table” · “Put [stages] on a timeline.”
- **Interactive:** “Create an interactive page / quiz / flashcards on [topic] for my students.”
- **Literature:** “Find systematic reviews from the last 10 years on [topic], with DOI/PMID and links.”
- **Appraisal:** “Act as a critical reviewer of this article: risks of bias, limits, questions to ask.”
- **Course design:** “Write 5 measurable learning outcomes for [session]” · “Turn these outcomes into a 2-hour session plan, as a table” · “Is every outcome taught and assessed?”
- **Teaching material:** “Turn these lecture notes into a clinical case with 3 decision points.”

## Checklist before using an answer

- [ ] Did I **open and read** the sources? (DOI → the *right* article? Does it say what the AI claims?)
- [ ] Are the **numbers, doses, dates and names** correct?
- [ ] Is it consistent with **current guidelines** and my institution's rules?
- [ ] Did I remove all **patient and personal data** before using the tool?
- [ ] Would I be comfortable signing this with **my name**?

## Tools mentioned today

| Need | Tools (free version available) |
|---|---|
| General assistant | Claude, ChatGPT, Gemini, Le Chat, Copilot |
| Literature search | PubMed, Consensus, Elicit, Semantic Scholar, Google Scholar |
| References | Zotero |
| Knowledge base (RAG) | NotebookLM; Projects in Claude / ChatGPT |
| Course design | Any assistant, with your course notes in a project (Claude, ChatGPT) or a NotebookLM notebook |
