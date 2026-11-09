---
title: "Workshop 2 — Your own AI knowledge base"
---

# Workshop 2: Your own AI knowledge base (RAG)

**Tool:** NotebookLM (free, Google account). *Alternatives: Projects in Claude or ChatGPT, or custom GPTs (some features need a paid plan).*

**Goal:** build an AI assistant that answers questions **from your documents only**, with a citation for every answer, and see where it works and where it fails.

<div class="key">

**Reminder:** this is the RAG pipeline from this morning. Your documents are split into passages; for each question, the most relevant passages are retrieved and given to the model, which answers and cites them.

</div>

## Exercise 1: (Fake) St Aldric knowledge base

1. Go to [notebooklm.google.com](https://notebooklm.google.com) and create a new notebook.
2. Add the 4 St Aldric (fake) documents as sources (PDF files from the course materials, folder data/knowledge_base):
   OSCE regulations · Placement handbook · Hand hygiene notes · Diabetes notes.
3. Ask these questions and **click on each citation** to read the source passage:
   - *How many stations are there in the OSCE, and what do I need to pass?*
   - *I missed the OSCE because I was ill. What happens now?*
   - *What should I do after a needle-stick injury on placement?*
   - *Can I wear my smartwatch during the OSCE?* (the answer spans two documents)
4. Now try to **break it**:
   - A question whose answer is **not** in the documents: *Where can students park?*
   - A question that mixes the documents with general knowledge: *What is the HbA1c target for an elderly patient?*
   - A **leading** question: *Since the OSCE has 12 stations, how many must I pass?*

**Discuss:** does it say when it doesn't know? Does it correct the false premise? Does it add information that is not in the sources?


<div class="warn">

**Quality of the sources:** an outdated document gives outdated answers.

</div>

## Exercise 2: Your own knowledge base

Create a new notebook with **your own non-confidential documents**: course notes, a guideline you teach, a programme handbook, open-access articles… and test a few questions

Useful instructions to add (in the chat or the notebook's settings):

```
You are a teaching assistant for [Year 2 nursing students] in [module].
Answer only from the sources. If the answer is not in the sources,
say so clearly and suggest who to contact. Always cite the passage.
Use simple language and short paragraphs.
```

- Which questions worked well?
- Which ones failed, and why (missing document, passage not found, ambiguous question)?

<div class="warn">

**Never upload confidential documents** (patient data, student records, unpublished exam papers) to a public tool.
Some institutions provide an approved tool.

</div>

## Exercise 3: A literature review from scratch

This time, you do **not** give the AI the articles: it has to **find** them itself, with a search tool.

1. **Choose a question**, e.g. *Does simulation-based training improve nursing students' clinical skills?* (or a topic you teach).
2. **Let the AI search:** use a *Deep Research* mode (ChatGPT, Gemini, Claude) or, in NotebookLM, the option to **discover sources on the web**. Ask:

```
Write a short literature review on [question] for health
professions educators. Search for peer-reviewed studies from the
last 10 years, favouring systematic reviews and meta-analyses.
Give a summary table (authors, year, design, population, main
finding, DOI or PMID), then a synthesis: what is known, where the
studies disagree, and what is missing.
```

3. **Check 3 references:** open the DOI or search the title in [PubMed](https://pubmed.ncbi.nlm.nih.gov). Does the article exist? Is it the right one? Does it say what the AI claims?
4. **Close the loop:** add the articles you have checked to a notebook as sources, and ask your questions again: the answers now cite the exact passages.

## Use cases

- **Module assistant** that answers students' practical questions from the module handbook and timetable.
- **Guideline navigator** for a set of clinical guidelines.
- **Revision companion** from lecture notes, generate quizzes/flashcards.
- **Literature review** uploads papers, ask questions about them (highlights the exact part where the answer is).
