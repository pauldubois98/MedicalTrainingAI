# AI Tools for Healthcare Educators

One-day hands-on training for teachers and educators in healthcare and medicine: how modern AI works (neural networks, LLMs, context, RAG, agents) and how to use it (web search, memory, knowledge bases, course design).

- **Slides:** `slides.html` (reveal.js). Press `F` for full screen, `Esc` for the overview.
- **Language:** English · **Length:** full day · **Participants:** own laptops, free accounts

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

Every push to `main` runs `.github/workflows/deploy.yml`, which builds everything and publishes `_site/`: a landing page, the slides, the demos and the handout PDFs. One-time setup on GitHub: **Settings → Pages → Source: GitHub Actions**.

## Before the session

- Send `workshops/00_setup.pdf` to participants one week before.
- Check the current free-tier limits of the tools (NotebookLM, deep research modes, assistants with web search and memory) and where the web search and memory settings are in each assistant. They change often.
- Give participants the PDFs from `knowledge_base/` (USB stick, shared drive or LMS).
