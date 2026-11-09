# AI Tools for Healthcare Educators

One-day hands-on training for teachers and educators in healthcare and medicine: how modern AI works (neural networks, LLMs, context, RAG, agents) and how to use it (web search, memory, knowledge bases, course design).

- **Website:** <https://pauldubois98.github.io/MedicalTrainingAI/>
- **Slides:** [online](https://pauldubois98.github.io/MedicalTrainingAI/slides.html) (reveal.js). Press `F` for full screen, `Esc` for the overview.
- **Language:** English · **Length:** full day · **Participants:** own laptops, free accounts

## Links

**Slides and demos**

- [Slides](https://pauldubois98.github.io/MedicalTrainingAI/slides.html)
- Demos: [train a neural network by hand](https://pauldubois98.github.io/MedicalTrainingAI/demos/network.html) · [automatic training](https://pauldubois98.github.io/MedicalTrainingAI/demos/training.html) · [predict the next letter](https://pauldubois98.github.io/MedicalTrainingAI/demos/letters.html) · [token by token](https://pauldubois98.github.io/MedicalTrainingAI/demos/token.html) · [temperature](https://pauldubois98.github.io/MedicalTrainingAI/demos/temperature.html) · [the importance of context](https://pauldubois98.github.io/MedicalTrainingAI/demos/context.html) · [RAG step by step](https://pauldubois98.github.io/MedicalTrainingAI/demos/rag.html) · [an agent at work](https://pauldubois98.github.io/MedicalTrainingAI/demos/agent.html)

**Handouts**

| Handout | PDF | Web |
|---|---|---|
| Before the day: setup | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/workshops/00_setup.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/workshops/00_setup.html) |
| Workshop 1: Web search and memory | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/workshops/01_search_memory.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/workshops/01_search_memory.html) |
| Workshop 2: AI knowledge base | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/workshops/02_knowledge_base.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/workshops/02_knowledge_base.html) |
| Workshop 3: Designing a course | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/workshops/03_course_design.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/workshops/03_course_design.html) |
| Cheat sheet | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/workshops/04_cheat_sheet.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/workshops/04_cheat_sheet.html) |

**Knowledge base** (fictional St Aldric School of Health Sciences, for Workshop 2 and the demos)

| Document | PDF | Web |
|---|---|---|
| OSCE regulations 2026 | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/osce_regulations_2026.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/osce_regulations_2026.html) |
| Clinical placement handbook | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/clinical_placement_handbook.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/clinical_placement_handbook.html) |
| Hand hygiene course notes | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/hand_hygiene_course_notes.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/hand_hygiene_course_notes.html) |
| Diabetes course notes | [PDF](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/diabetes_course_notes.pdf) | [web](https://pauldubois98.github.io/MedicalTrainingAI/knowledge_base/diabetes_course_notes.html) |

**Repository:** [source code](https://github.com/pauldubois98/MedicalTrainingAI) · [deployment runs (GitHub Actions)](https://github.com/pauldubois98/MedicalTrainingAI/actions)

## Programme

**Theory** (slides and demos)

| Part | Content | Demos |
|---|---|---|
| Welcome | Content of the day, icebreaker | |
| 1. How AI works | Neural networks, training, LLMs, tokens, temperature, knowledge cutoff, context | network, training, letters, token, temperature, **context** |
| 2. Context, RAG, tools and agents | Manual context, RAG and its limits, agents, ways for a model to “know”, chat app vs API vs open-weight models, comparing LLMs (LMArena, costs) | **rag**, **agent** |
| 3. Best practices | Check the sources, protect patient data, give context | |

**Practice** (participants' own laptops)

| Workshop | Content | Handout |
|---|---|---|
| 1. Web search and memory | Questions after the training cutoff, without then with web search; how memory works | `workshops/01_search_memory` |
| 2. AI knowledge base | NotebookLM on the St Aldric documents, then on your own; a literature review from scratch | `workshops/02_knowledge_base`, `knowledge_base/` |
| 3. Designing a course | Outcomes and session plan, iterate on the plan, create materials, iterate | `workshops/03_course_design` |
| Wrap-up | Summary | `workshops/04_cheat_sheet` |

## Contents

```
slides.md            source of the slides (pandoc markdown)  → slides.html
theme.css            slide theme
figures.py, svgkit.py  diagrams → figures/*.svg
demos/               interactive demos (offline, no API key needed)
  network, training, letters, token, temperature   reused from the LibraryConference talk, translated
  context            same question with and without a document in the context
  rag                real keyword search (BM25) over the knowledge base, top-k, prompt, grounded answer
  agent              step-by-step agent loop (literature search, admin email with human approval, knowledge base)
make_corpus.py       knowledge_base/*.md → demos/rag_corpus.js
workshops/           handouts: 00 setup (send before the day), 01–03 workshops, 04 cheat sheet
knowledge_base/      4 documents of the fictional "St Aldric School of Health Sciences" (used by the demos and Workshop 2)
handout.css          style of the handouts
index.md             landing page of the website
.github/workflows/   GitHub Actions: build and deploy to GitHub Pages
```

Only sources are committed: `slides.html`, `figures/`, `demos/rag_corpus.js`, the handout HTML/PDFs and `vendor/` (reveal.js) are generated (see `.gitignore`).

All the example data is **fictional**. The real references used in the slides were checked against Crossref and Europe PMC (November 2026).

## Build

```sh
python3 build.py         # figures, RAG corpus, slides.html, handouts (.html)
python3 build.py --pdf   # same, plus PDFs of the handouts (headless Chrome/Chromium)
python3 build.py --pdf --site   # same, plus _site/ (the website)
```

The first build downloads reveal.js into `vendor/`. Requirements: Python 3 + numpy, pandoc, and Chrome or Chromium for the PDFs.

## Website (GitHub Pages)

Every push to `main` runs `.github/workflows/deploy.yml`, which builds everything and publishes `_site/` to <https://pauldubois98.github.io/MedicalTrainingAI/>: a landing page, the slides, the demos and the handout PDFs. Follow the runs in the [Actions tab](https://github.com/pauldubois98/MedicalTrainingAI/actions). One-time setup on GitHub: **Settings → Pages → Source: GitHub Actions** (already done).

## Before the session

- Send `workshops/00_setup.pdf` to participants one week before.
- Check the current free-tier limits of the tools (NotebookLM, deep research modes, assistants with web search and memory) and where the web search and memory settings are in each assistant. They change often.
- Give participants the PDFs from `knowledge_base/` (USB stick, shared drive or LMS).
