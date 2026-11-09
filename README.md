# AI Tools for Healthcare Educators

One-day hands-on training for teachers and educators in healthcare and medicine: how modern AI works (neural networks, LLMs, context, RAG, agents) and how to use it (web search, memory, knowledge bases, course design).

- **Slides:** `slides.html` (reveal.js). Press `S` for speaker notes (timings and demo instructions), `F` for full screen, `Esc` for the overview.
- **Language:** English · **Length:** full day · **Participants:** own laptops, free accounts

## Programme

| Time | Session | Material |
|---|---|---|
| 9:00 | Welcome, icebreaker | slides |
| 9:15 | **Part 1: How AI works** (neural networks, training, LLMs, tokens, temperature, context) | demos: network, training, letters, token, temperature, **context** |
| 10:30 | Break | |
| 10:45 | **Part 2: From manual context to RAG** | demo: **rag** |
| 11:30 | **Part 3: Tools and agents** | demo: **agent** |
| 12:00 | Best practices (check sources, visual and interactive explanations, patient data, writing requests) | |
| 12:30 | Lunch | |
| 13:30 | **Workshop 1: Web search and memory** | `workshops/01_search_memory` (optional extra: `data/references/`) |
| 14:40 | **Workshop 2: Knowledge base (NotebookLM)** | `workshops/02_knowledge_base`, `data/knowledge_base/` |
| 15:40 | Break | |
| 15:55 | **Workshop 3: Designing a course** | `workshops/03_course_design`, `data/knowledge_base/diabetes_course_notes` |
| 16:40 | Wrap-up, action plan | `workshops/04_cheat_sheet` |

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
make_corpus.py       data/knowledge_base/*.md → demos/rag_corpus.js
workshops/           handouts: 00 setup (send before the day), 01–03 workshops, 04 cheat sheet
data/
  knowledge_base/    4 documents of the fictional "St Aldric School of Health Sciences" (used by the demos and Workshop 2)
  references/        reference-check exercise + instructor key (do not distribute the key)
handout.css          style of the handouts
index.md             landing page of the website
.github/workflows/   GitHub Actions: build and deploy to GitHub Pages
```

Only sources are committed: `slides.html`, `figures/`, `demos/rag_corpus.js`, the handout HTML/PDFs and `vendor/` (reveal.js) are generated (see `.gitignore`).

All the example data is **fictional**. The real references used in the slides and the exercise were checked against Crossref and Europe PMC (November 2026).

## Build

```sh
python3 build.py         # figures, RAG corpus, slides.html, handouts (.html)
python3 build.py --pdf   # same, plus PDFs of the handouts (headless Chrome/Chromium)
python3 build.py --pdf --site   # same, plus _site/ (the website, without the instructor key)
```

The first build downloads reveal.js into `vendor/`.

## Website (GitHub Pages)

Every push to `main` runs `.github/workflows/deploy.yml`, which builds everything and publishes `_site/`: a landing page, the slides, the demos and the handout PDFs. One-time setup on GitHub: **Settings → Pages → Source: GitHub Actions**.

The instructor key (`*KEY_instructor*`) is never published on the website, but its Markdown source is in the repository: keep the repository private if participants must not see it.

Requirements: Python 3 + numpy, pandoc, and Chrome or Chromium for the PDFs.

## Before the session

- [ ] Send `workshops/00_setup.pdf` to participants one week before.
- [ ] Check the current free-tier limits of the tools (NotebookLM, assistants with web search and memory) and where the web search and memory settings are in each assistant. They change often.
- [ ] Give participants the PDFs from `data/knowledge_base/` and `data/references/reference_check_exercise.pdf` (USB stick, shared drive or LMS).
- [ ] Prepare the two live demos from the best-practices section (visual explanation, interactive page) in your preferred assistant.
- [ ] Check the room's Wi-Fi with 20+ laptops. The slides and demos work offline; the workshops need internet.
