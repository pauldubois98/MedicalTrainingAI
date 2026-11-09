---
title: "AI Tools for Healthcare Educators"
subtitle: "How modern AI works, and how to use it for teaching, research and administration"
lang: en
---

## Programme of the day

<div class="cards c2" style="text-align:left; align-items:start">
<div class="card t">
<b style="font-size:1.1em; margin-bottom:.4em">☀️ Morning: understand</b>
<table class="agenda">
<tr><td>9:00</td><td>Welcome</td></tr>
<tr><td>9:15</td><td>How AI works</td></tr>
<tr><td>10:30</td><td><span class="muted">Break</span></td></tr>
<tr><td>10:45</td><td>From manual context to RAG</td></tr>
<tr><td>11:30</td><td>Tools and agents</td></tr>
<tr><td>12:00</td><td>Best practices</td></tr>
</table>
</div>
<div class="card o">
<b style="font-size:1.1em; margin-bottom:.4em">🌙 Afternoon: practise</b>
<table class="agenda">
<tr><td>13:30</td><td>Workshop 1: Bibliography</td></tr>
<tr><td>14:40</td><td>Workshop 2: Your own AI knowledge base</td></tr>
<tr><td>15:40</td><td><span class="muted">Break</span></td></tr>
<tr><td>15:55</td><td>Workshop 3: Emails</td></tr>
<tr><td>16:40</td><td>Your action plan</td></tr>
<tr><td>17:00</td><td><span class="muted">End</span></td></tr>
</table>
</div>
</div>

::: notes
Everyone has a laptop: check now that all participants can log in to the tools listed in the setup sheet (workshops/00_setup).
Fix login problems during the morning breaks, not during the workshops.
:::

## What do you already use AI for? {.question}

<div class="big-q">What do you <em>already</em> use AI for?<br>What would you <em>like</em> to use it for?</div>

<div class="emoji-xl" style="margin-top:.5em">🙋</div>

::: notes
5 minutes. Go round the room or use a quick poll. Write the answers on a board and come back to them at the end of the day (action plan).
Typical answers: writing emails, summarising articles, preparing quizzes, translating. Note the worries too (cheating, reliability, privacy).
:::

## How does AI work? {.divider}

## Machine learning: learning from examples

![](figures/cats_ml.svg){.fig}

::: notes
Instead of writing rules by hand, we show the computer thousands of examples with the right answer.
Medical equivalents: chest X-ray → pneumonia or not; skin photo → suspicious lesion or not.
:::

## A neuron can learn

![](figures/neuron.svg){.fig}

::: notes
A neuron does a weighted sum of its inputs, then applies a function.
The weights are the "knobs" of the model: learning means finding good values for these knobs.
:::

## Training a neural network by hand

<iframe class="demo" data-src="demos/network.html?ni=2&nh=1&hs=2&no=1&act=step&t=XOR"></iframe>

::: notes
Ask a volunteer to drag the weights until all 4 rows are correct (XOR target).
It is hard with 9 knobs. A large language model has hundreds of billions. We need an automatic method.
:::

## Training = adjusting the weights automatically

![](figures/training_loop.svg){.fig}

## Automatic training

<iframe class="demo" data-src="demos/training.html"></iframe>

::: notes
Press Run: the error curve goes down, the 4 rows become correct.
The same loop, repeated millions of times on huge amounts of text, produces a language model.
:::

## The models keep growing

![](figures/scale_params.svg){.fig}

## Predicting what comes next

<div class="big-q" style="font-size:1.4em; margin-top:1.2em">“Paracetamol is used to reduce <span class="violet">___</span>”</div>

::: {.fragment}
<div class="big-q orange" style="font-size:1.4em">→ fever</div>
:::

::: {.fragment}
<div class="big-q" style="font-size:1.1em; margin-top:1em">“Paracetamol is used to reduce fever and relieve mild <span class="violet">___</span>”</div>
:::
::: {.fragment}
<div class="big-q orange" style="font-size:1.1em">→ pain</div>
:::

::: notes
A large language model (LLM) is trained on a single task: predict the next piece of text.
To do this well on billions of sentences, it has to capture grammar, facts, and some reasoning patterns.
:::

## Predicting the next letter

<iframe class="demo" data-src="demos/letters.html"></iframe>

::: notes
A real tiny network (3 letters in, 20 hidden neurons, 27 outputs), trained on "Around the World in Eighty Days" by Jules Verne.
About 40% of letters predicted correctly. Switch between the English, French and random (untrained) networks.
It quickly loops ("the the the…") because it only sees 3 letters. An LLM sees thousands of tokens of context.
:::

## Characters, words, tokens

![](figures/tokens.svg){.fig}

## Token by token

<iframe class="demo" data-src="demos/token.html"></iframe>

::: notes
Illustrative mini-model (not a real LLM). Click on less likely tokens to explore other paths.
Key message: the model never "looks up" an answer. It produces the most plausible continuation, one token at a time.
This is why it can produce text that sounds right but is false: a hallucination.
:::

## Why answers vary

<iframe class="demo" data-src="demos/temperature.html"></iframe>

::: notes
The model does not always pick the most likely token: it draws at random according to the probabilities.
Temperature controls this randomness. Low = predictable, repetitive. High = creative, sometimes absurd ("horoscope").
That is why the same question asked twice can give two different answers.
:::

## A conversation is just one long text

![](figures/conversation.svg){.fig}

::: notes
Everything in the conversation (instructions, your messages, documents you pasted, its previous answers) is the model's "context".
The model continues this text. It has no other memory than this context and what it learned during training.
:::

## What the model knows… and does not know

![](figures/knowledge_cutoff.svg){.fig}

::: notes
Knowledge is frozen at the training cutoff date. It knows nothing about:
- anything published after the cutoff (new guidelines, recent studies);
- anything private (your institution's regulations, your course materials).
Instead of saying "I don't know", it may produce a plausible but invented answer.
:::

## The importance of context

<iframe class="demo" data-src="demos/context.html"></iframe>

::: notes
Scenario 1 without the document: confident invented numbers. With the document: correct answer with a citation.
Scenario 2: generic but correct answer; with the document, specific to the institution.
Scenario 3: general knowledge, the model already knows; the document adds a source.
St Aldric School is fictional: all its documents are in data/knowledge_base/.
:::

## The key question {.question}

<div class="big-q">What information should we put<br>in the model's <em>context</em><br>to help it answer correctly?</div>

## From manual context to RAG {.divider}

## The manual method

![](figures/manual_context.svg){.fig}

::: notes
This is what most people do today, and it works well: paste an article or a guideline and ask questions about it.
Most assistants also let you upload PDFs directly.
Quick try (5 min): download the OSCE regulations (data/knowledge_base), paste them into a chatbot, ask "How many stations?", then ask the same question in a new conversation without the document.
:::

## Retrieval-Augmented Generation (RAG)

![](figures/rag_pipeline.svg){.fig}

::: notes
RAG automates the manual method:
1. Build a knowledge base (articles, guidelines, courses, institutional documents), split into passages.
2. For each question, search the knowledge base.
3. Keep the k most relevant passages (e.g. 5 to 20).
4. Add them to the model's context, with the question.
5. The model answers using these passages, and cites them.
:::

## RAG step by step

<iframe class="demo" data-src="demos/rag.html"></iframe>

::: notes
The search is real (BM25 keyword search, running in the browser over the 29 passages of the 4 St Aldric documents).
1. "What happens if I miss the OSCE because I'm sick?" in "Same words" mode: the right passage is not found (the text says "absent" and "medical certificate", not "miss" or "sick").
   Switch to "Same meaning": it is found. Real systems use "embeddings", which match by meaning; here it is simulated with synonyms.
2. Set k = 1: part of the answer goes missing (the resit dates are in another passage). k is a trade-off: too small, information is missing; too large, the context is diluted.
3. "Where can students park their car?": nothing relevant; a good system says it does not know.
:::

## RAG in healthcare education

<div class="cards c3">
<div class="card t"><div class="e">📚</div><b>Scientific literature</b>Ask questions across a set of articles</div>
<div class="card o"><div class="e">📋</div><b>Clinical guidelines</b>Find the right recommendation, with the exact passage</div>
<div class="card g"><div class="e">🏫</div><b>Institutional documents</b>Regulations, handbooks, course materials: a 24/7 assistant for students</div>
</div>

<div class="msg fragment">Ready-made tools: NotebookLM, Claude Projects, ChatGPT Projects / custom GPTs…<br>→ Workshop 2</div>

## The limits of RAG

<div class="cards c2">
<div class="card r"><div class="e">🔎</div><b>The search can miss</b>the right passage, and then the model guesses</div>
<div class="card r"><div class="e">🗑️</div><b>Garbage in, garbage out</b>outdated or wrong documents give wrong answers</div>
<div class="card r"><div class="e">🎭</div><b>It can still hallucinate</b>or misread a passage</div>
<div class="card g"><div class="e">✅</div><b>Citations make answers checkable</b>click and read the source!</div>
</div>

## Tools and agents {.divider}

## From chatbot to agent

![](figures/chatbot_vs_agent.svg){.fig}

::: notes
We tell the model which tools it may use (web search, PubMed, a knowledge base, email…).
When answering, the model can decide to call a tool. The result is added to its context, and it continues.
RAG is in fact one possible tool among others.
:::

## Just like us

![](figures/human_vs_agent.svg){.fig}

## An agent at work

<iframe class="demo" data-src="demos/agent.html"></iframe>

::: notes
Illustrative traces, not real searches.
1. Literature: the agent chooses PubMed, reads abstracts, answers with references to check.
2. Admin: calendar → directory → draft email → HUMAN APPROVAL → send. Keep a human in the loop for anything sent out.
3. Our documents: the agent chooses the knowledge base (RAG as a tool) rather than the web.
:::

## Four ways for a model to "know"

![](figures/knowledge_sources.svg){.fig}

## Best practices {.divider}

## 1. Check the sources

![](figures/fake_reference.svg){.fig-s}

<div class="msg fragment">In one study, 55% of references produced by GPT-3.5 were fabricated, versus 18% for GPT-4.</div>

<div class="src">Walters WH & Wilder EI, “Fabrication and errors in the bibliographic citations generated by ChatGPT”, Scientific Reports 13, 14045 (2023). <a href="https://doi.org/10.1038/s41598-023-41032-5">doi:10.1038/s41598-023-41032-5</a></div>

::: notes
Same study: even among the real (non-fabricated) references, 43% (GPT-3.5) and 24% (GPT-4) contained substantive errors (wrong year, journal, pages…).
Tools with web search or RAG fabricate far fewer references, but they can still misquote a real paper.
Classic trap: the DOI exists but leads to a different article.
Check: does the DOI open the right article? Does the article say what the AI claims? Read at least the abstract.
:::

## 2. Ask for visual explanations

<div class="cards c3">
<div class="card t"><div class="e">🗺️</div><b>Diagrams</b>“Draw a diagram of the renin–angiotensin–aldosterone system”</div>
<div class="card o"><div class="e">📊</div><b>Tables</b>“Compare the 4 classes of antihypertensives in a table”</div>
<div class="card g"><div class="e">⏳</div><b>Timelines</b>“Show the stages of wound healing on a timeline”</div>
</div>

::: notes
Live demo: ask an assistant (e.g. Claude or ChatGPT) for a diagram. Most assistants can produce diagrams (Mermaid, SVG) or tables.
Check the content as carefully as text: a diagram can be wrong too.
:::

## 3. Ask for interactive explanations

<div class="big-q" style="font-size:1.1em; margin-top:.6em">“Create an interactive page showing how the plasma concentration of a drug changes with the dose and the dosing interval.”</div>

<div class="msg fragment">→ simulations, quizzes, flashcards, case studies…<br>for your students, in a few minutes</div>

::: notes
Live demo: Claude (Artifacts) or ChatGPT (Canvas) can create small interactive web pages.
Ideas: a pharmacokinetics simulator, a quiz on the 5 moments, an ECG rhythm flashcard deck, a branching clinical case.
:::

## 4. Protect patient data

<div class="cards c2" style="text-align:left">
<div class="card r"><div class="e">🚫</div><b>Never</b> enter patient-identifiable data (name, date of birth, record number, photo…) into a public AI tool</div>
<div class="card g"><div class="e">✅</div><b>Anonymise</b> clinical cases, follow your institution's policy and the GDPR, and prefer the tools approved by your institution</div>
</div>

## Writing a good request

<ol class="retenir">
<li><div><b>Role</b><br><span>“You are an experienced nursing educator…”</span></div></li>
<li><div><b>Context</b><br><span>“…for Year 1 students, before their first placement.”</span></div></li>
<li><div><b>Task</b><br><span>“Write 10 multiple-choice questions on hand hygiene…”</span></div></li>
<li><div><b>Format</b><br><span>“…as a table, with the answer and a one-line explanation.”</span></div></li>
<li><div><b>Iterate</b><br><span>“Make questions 3 and 7 harder.”</span></div></li>
</ol>

## Hands-on workshops {.divider}

## Workshop 1: Bibliography and literature review

<div class="cards c4">
<div class="card t"><div class="e">🔎</div><b>Search</b>an AI tool with web search</div>
<div class="card o"><div class="e">📑</div><b>Summarise &amp; compare</b>key papers in a table</div>
<div class="card r"><div class="e">✅</div><b>Check</b>every reference</div>
<div class="card g"><div class="e">📚</div><b>Build</b>a bibliography</div>
</div>

<div class="msg">Handout: workshops/01_bibliography · 70 min</div>

## Workshop 2: Your own AI knowledge base

<div class="cards c4">
<div class="card t"><div class="e">📂</div><b>Upload</b>documents into NotebookLM</div>
<div class="card o"><div class="e">❓</div><b>Ask</b>questions in plain language</div>
<div class="card r"><div class="e">🔗</div><b>Trace</b>each answer to its source</div>
<div class="card g"><div class="e">🎓</div><b>Create</b>an assistant for your course</div>
</div>

<div class="msg">Handout: workshops/02_knowledge_base · 60 min</div>

## Workshop 3: Emails

<div class="cards c4">
<div class="card t"><div class="e">✍️</div><b>Draft</b>professional emails</div>
<div class="card o"><div class="e">🎚️</div><b>Adapt</b>the tone to the audience</div>
<div class="card r"><div class="e">🧵</div><b>Summarise</b>a thread, extract actions</div>
<div class="card g"><div class="e">🔁</div><b>Reuse</b>templates for repetitive emails</div>
</div>

<div class="msg">Handout: workshops/03_emails · 45 min</div>

## Wrap-up {.divider}

## Take-home messages

<ol class="retenir">
<li class="fragment"><div>An LLM <b>predicts text</b>, token by token: plausible ≠ true.</div></li>
<li class="fragment"><div>Its answers depend on its <b>context</b>: give it the right documents.</div></li>
<li class="fragment"><div><b>RAG</b> and <b>tools</b> fetch that information automatically.</div></li>
<li class="fragment"><div><b>Check the sources</b>, protect patient data, and stay in control.</div></li>
</ol>

## Your action plan {.question}

<div class="big-q">Which <em>one</em> task will you try with AI<br>next week?</div>

::: notes
Each participant writes down one concrete task (a quiz, a bibliography, an email template, a knowledge base for their course).
Come back to the list written during the icebreaker.
:::

## Sources

<div style="text-align:left; font-size:20px; max-width:1150px; margin:0 auto; line-height:1.55">

- Walters WH, Wilder EI. *Fabrication and errors in the bibliographic citations generated by ChatGPT*. Scientific Reports 13, 14045 (2023). <https://doi.org/10.1038/s41598-023-41032-5>
- Singhal K et al. *Large language models encode clinical knowledge*. Nature 620, 172–180 (2023). <https://doi.org/10.1038/s41586-023-06291-2>
- Thirunavukarasu AJ et al. *Large language models in medicine*. Nature Medicine 29, 1930–1940 (2023). <https://doi.org/10.1038/s41591-023-02448-8>
- Lewis P et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. <https://arxiv.org/abs/2005.11401>
- World Health Organization. *WHO Guidelines on Hand Hygiene in Health Care* (2009).
- Interactive demos adapted from the talk “IA & société” (P. Dubois, 2026). St Aldric School of Health Sciences is fictional.

</div>
