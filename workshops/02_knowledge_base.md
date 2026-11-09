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

## Exercise 2: Your own knowledge base

Create a new notebook with **your own non-confidential documents**: course notes, a guideline you teach, a programme handbook, open-access articles…

1. Write **5 questions your students actually ask**, and test them.
2. For each answer, note: ✅ correct and well sourced · ⚠️ partly correct · ❌ wrong or invented.
3. Explore the tools that turn your sources into teaching material (study guide, FAQ, mind map, quiz or flashcards, audio overview, depending on what the tool offers). **Read everything before giving it to students.**

Useful instructions to add (in the chat or the notebook's settings):

```
You are a teaching assistant for [Year 2 nursing students] in [module].
Answer only from the sources. If the answer is not in the sources,
say so clearly and suggest who to contact. Always cite the passage.
Use simple language and short paragraphs.
```

## Exercise 3: Debrief

- Which questions worked well? Which ones failed, and why (missing document, passage not found, ambiguous question)?
- **Quality of the sources:** an outdated document gives outdated answers. Who will keep the knowledge base up to date?
- **Sharing with students:** what would you need to check first? (accuracy, institutional policy, data protection, what students may and may not upload)

<div class="warn">

**Never upload confidential documents** (patient data, student records, unpublished exam papers) to a public tool. Check your institution's policy; some institutions provide an approved tool.

</div>

## Use cases

- **Module assistant** that answers students' practical questions from the module handbook and timetable.
- **Guideline navigator** for a set of clinical guidelines.
- **Revision companion** from lecture notes, generate quizzes/flashcards.
- **Literature review** uploads papers, ask questions about them (highlights the exact part where the answer is).
