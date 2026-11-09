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

## What do you already use AI for? {.question}

<div class="big-q">
   What do you <em>already</em> use AI for?<br>
   What would you <em>like</em> to use it for?
</div>

## How does AI work? {.divider}

## Machine learning: learning from examples

![](figures/cats_ml.svg){.fig}

## A neuron can learn

![](figures/neuron.svg){.fig}

## Training a neural network by hand

<iframe class="demo" data-src="demos/network.html?ni=2&nh=1&hs=2&no=1&act=step&t=XOR"></iframe>

## Training *means* adjusting weights

![](figures/training_loop.svg){.fig}

## Automatic training

<iframe class="demo" data-src="demos/training.html"></iframe>

## Models size keep growing

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

## Predicting the next letter

<iframe class="demo" data-src="demos/letters.html"></iframe>

## Characters, words, tokens

![](figures/tokens.svg){.fig}

## Token by token

<iframe class="demo" data-src="demos/token.html"></iframe>

## Why answers vary

<iframe class="demo" data-src="demos/temperature.html"></iframe>

## A conversation is just one long text

![](figures/conversation.svg){.fig}

## Model's knowledge… and ignorance

![](figures/knowledge_cutoff.svg){.fig}

## The importance of context

<iframe class="demo" data-src="demos/context.html"></iframe>

## The key question {.question}

<div class="big-q">What information should we put<br>in the model's <em>context</em><br>to help it answer correctly?</div>

## From manual context to RAG {.divider}

## Manual method

![](figures/manual_context.svg){.fig-s}

<div class="cards c3 tight vc">
<div class="card r fragment"><b>⏱ Slow and repetitive</b></div>
<div class="card r fragment"><b>📏 Limited context size</b></div>
<div class="card r fragment"><b>❓ Which documents to choose?</b></div>
</div>

## Retrieval-Augmented Generation (RAG)

![](figures/rag_pipeline.svg){.fig}

## RAG step by step

<iframe class="demo" data-src="demos/rag.html"></iframe>

## RAG in healthcare education

<div class="cards c3 tight">
<div class="card t"><div class="e">📚</div><b>Scientific literature</b>Ask questions across a set of articles</div>
<div class="card o"><div class="e">📋</div><b>Clinical guidelines</b>Find the right recommendation, with the exact passage</div>
<div class="card g"><div class="e">🏫</div><b>Institutional documents</b>Regulations, handbooks, course materials: a 24/7 assistant for students</div>
</div>

<div class="msg fragment">Tools: NotebookLM, Claude Projects, ChatGPT Projects…</div>

<div class="fragment">
<div class="cards c4 tight">
<div class="card r"><b>🔎 The search can miss</b>the right passage</div>
<div class="card r"><b>🗑️ Garbage in,<br>garbage out</b>outdated or wrong documents give wrong answers</div>
<div class="card g"><b>✅ Citations make answers checkable</b>read the source if unsure</div>
</div>
</div>

## Tools and agents {.divider}

## From chatbot to agent

![](figures/chatbot_vs_agent.svg){.fig}

## Just like us

![](figures/human_vs_agent.svg){.fig}

## An agent at work

<iframe class="demo" data-src="demos/agent.html"></iframe>

## Four ways for a model to "know"

![](figures/knowledge_sources.svg){.fig}

## Best practices

<div class="bp">
<div>
<img src="figures/fake_reference.svg" alt="A fabricated reference">
<div class="msg fragment">In an old (2023) study, 55% of references produced by <span style="white-space:nowrap">GPT-3.5</span> were fabricated, 18% for GPT-4.</div>
</div>
<div class="fragment">
<div class="card r fragment"><b>🚫 Data</b>: Never give patient-identifiable data to a public AI tool</div>
<div class="card g fragment"><b>✅ Role</b>: Add “You are an experienced nursing educator…” to the prompt.</div>
<div class="card t fragment"><b>💡 Target</b>: Add “explain for Year 1 students” to the prompt.</div>
</div>
</div>

<div class="src">Walters WH & Wilder EI, “Fabrication and errors in the bibliographic citations generated by ChatGPT”, Scientific Reports 13, 14045 (2023). <a href="https://doi.org/10.1038/s41598-023-41032-5">doi:10.1038/s41598-023-41032-5</a></div>

## Hands-on workshops {.divider}

## Workshop 1: Bibliography and literature review

<div class="cards c3">
<div class="card t"><div class="e">🔎</div><b>Search</b>an AI tool with web search</div>
<div class="card o"><div class="e">📑</div><b>Summarise &amp; compare</b>key papers in a table</div>
<div class="card r"><div class="e">✅</div><b>Check</b>every reference</div>
</div>

<div class="msg">Handout: workshops/01_bibliography</div>

## Workshop 2: Your own AI knowledge base

<div class="cards c3">
<div class="card t"><div class="e">📂</div><b>Upload</b>documents into NotebookLM</div>
<div class="card o"><div class="e">❓</div><b>Ask</b>questions in plain language</div>
<div class="card r"><div class="e">🔗</div><b>Trace</b>each answer to its source</div>
</div>

<div class="msg">Handout: workshops/02_knowledge_base</div>

## Workshop 3: Emails

<div class="cards c3">
<div class="card t"><div class="e">✍️</div><b>Draft</b>professional emails</div>
<div class="card o"><div class="e">🎚️</div><b>Adapt</b>the tone to the audience</div>
<div class="card g"><div class="e">🔁</div><b>Reuse</b>templates for repetitive emails</div>
</div>

<div class="msg">Handout: workshops/03_emails</div>

## Summary

<ol class="retenir">
<li class="fragment"><div>An LLM <b>predicts text</b>, token by token.</div></li>
<li class="fragment"><div>Its answers depend on its <b>context</b>.</div></li>
<li class="fragment"><div><b>RAG</b> and <b>tools</b> fetch information automatically.</div></li>
<li class="fragment"><div><b>Check</b> the sources.</div></li>
<li class="fragment"><div><b>Protect</b> patient data.</div></li>
</ol>

## Sources

<div style="text-align:left; font-size:20px; max-width:1150px; margin:0 auto; line-height:1.55">

- Walters WH, Wilder EI. *Fabrication and errors in the bibliographic citations generated by ChatGPT*. Scientific Reports 13, 14045 (2023). <https://doi.org/10.1038/s41598-023-41032-5>
- Singhal K et al. *Large language models encode clinical knowledge*. Nature 620, 172–180 (2023). <https://doi.org/10.1038/s41586-023-06291-2>
- Thirunavukarasu AJ et al. *Large language models in medicine*. Nature Medicine 29, 1930–1940 (2023). <https://doi.org/10.1038/s41591-023-02448-8>
- Lewis P et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. <https://arxiv.org/abs/2005.11401>
- World Health Organization. *WHO Guidelines on Hand Hygiene in Health Care* (2009).
- Interactive demos adapted from the talk “IA & société” (P. Dubois, 2026).

</div>
