---
title: "Workshop 1 — Web search and memory"
---

# Workshop 1: Web search and memory

**Tool:** your AI assistant (ChatGPT, Claude, Gemini, Le Chat…)

**Goal:** see for yourself what a model knows on its own, what web search adds, and what “memory” really is.

<div class="tip">

Menus change often. If you cannot find a setting, ask your neighbour or the trainer, or simply ask the assistant: “How do I turn off web search in this app?”

</div>

## Exercise 1: A model without web search

### Step 1: turn web search off

| Assistant | How to turn web search off |
|---|---|
| **ChatGPT** | Settings → Personalization → Advanced → switch off **Web search** |
| **Claude** | “Search and tools” menu (under the message box) → switch off **Web search** |
| **Le Chat (Mistral)** | Tools menu (under the message box) → switch off **Web search** |
| **Gemini** | Not possible in the Gemini app. Use [Google AI Studio](https://aistudio.google.com) instead (free, same Google account): “Grounding with Google Search” is off by default |

Then open a **new conversation**.

### Step 2: ask about things that happened after its training

Ask a few of these questions, **one per new conversation**:

```
Who won the 2026 US midterm elections? Give me the final results
for the House and the Senate.
```

```
Who received the 2026 Nobel Prize in Physiology or Medicine,
and for what discovery?
```

```
Which team won the 2026 FIFA World Cup, and what was the score
in the final?
```

```
What are the main changes in the most recent update of
[a guideline you teach, e.g. the national hypertension guideline]?
```

**Observe and note down:**

- Does it say it **does not know** (and mention its training cutoff)?
- Does it **guess**, or invent a confident answer?
- If it invents: how convincing is it? Would a student notice?

<div class="warn">

A model's knowledge is **frozen at its training cutoff**. Without a tool, it cannot know what happened afterwards, but it may still answer as if it did. (Newer models have later cutoffs: if one question is answered correctly, try a more recent one.)

</div>

## Exercise 2: The same model with web search

### Step 1: turn web search back on

Use the same menu as in Exercise 1 (in Google AI Studio: switch on **Grounding with Google Search**). Open a **new conversation**.

### Step 2: ask the same questions again

Ask the same questions, and add:

```
Give your sources, with links.
```

**Observe:** is the answer different? Does it now cite sources?

### Step 3: double-check the sources

For **two** of the answers, open at least **two** of the links:

- Does the page exist, and does it say **what the AI claims**?
- Is the source **reliable**: official body, journal or recognised news outlet, rather than an anonymous blog or forum?
- Is the information **up to date** (check the date of the page)?

<div class="key">

**What changed?** The model is the same. Web search is a **tool**: the model searches, the results are added to its **context**, and it answers from them. This is the agent loop seen this morning. Sources make the answer **checkable**, not automatically **correct**.

</div>

## Exercise 3: How memory works

Many assistants can **remember** things about you from one conversation to the next. Let us see what that really means.

### Step 1: check that memory is on

| Assistant | Where to find memory |
|---|---|
| **ChatGPT** | Settings → Personalization → **Memory** (“Reference saved memories”, “Reference chat history”) |
| **Claude** | Settings → Capabilities → **Memory** |
| **Gemini** | Settings → **Personal context** / Saved info |
| **Le Chat (Mistral)** | Settings → **Memories** |

If your assistant has no memory setting on a free account, pair up with someone whose assistant does.

### Step 2: tell it about yourself

In a conversation, write:

```
Please remember this for our future conversations:
- I teach [Year 2 nursing students] at the St Aldric School of
  Health Sciences.
- My subject is [infection prevention].
- I prefer short answers, with tables when possible, in British English.
```

Check that it confirms it has saved this (in ChatGPT, a “Memory updated” message appears).

### Step 3: open a new conversation

Open a **new** conversation and ask, without any other detail:

```
Suggest a 10-minute activity to start my next class.
```

**Observe:** is the activity adapted to your students, your subject and your format? Then ask:

```
What do you know about me?
```

### Step 4: look at, edit and delete the memory

Go back to the memory settings and **open the list of saved memories**:

- What exactly was saved? Is it **word for word** what you wrote, or a summary?
- **Delete** one item (for example your subject), open a new conversation and ask the same question again. What changed?

### Step 5: a conversation without memory

Open a **temporary chat** (ChatGPT: *Temporary chat*; Claude: *Incognito chat*; Gemini: *Temporary chat*) and ask the same question again. Is the answer still personalised?

<div class="key">

**What is memory?** Saved memories are just **text that the assistant adds to the context** at the start of each conversation, like a note you would paste yourself. The model itself does not change and does not learn: delete the note, and the “memory” is gone.

</div>

<div class="warn">

**Never store** patient information, or personal information about students or colleagues, in an assistant's memory. Review your saved memories regularly, and delete what you added today if you do not want to keep it.

</div>

## To go further

**Custom instructions:** most assistants also have a field for permanent instructions (ChatGPT: *Customize ChatGPT*; Claude: *Personal preferences*).
