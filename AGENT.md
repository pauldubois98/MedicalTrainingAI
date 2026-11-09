# Project: Introduction to Modern AI Tools for Healthcare Workers

## 1. Target Audience

The training is designed for **teachers and educators in the healthcare and medical fields**.

The goal is to introduce them to modern AI concepts and demonstrate how AI tools can improve their daily academic and administrative workflows.

The training should be accessible to participants with little or no technical background.
Prioritize practical demonstrations over mathematical or technical details.

## 2. Educational Objectives

By the end of the training, participants should understand:

- How neural networks learn.
- How large language models (LLMs) generate text.
- What context is and why it matters.
- How to provide AI models with external knowledge.
- What Retrieval-Augmented Generation (RAG) is.
- How AI agents use external tools to retrieve information and perform tasks.
- How to critically evaluate AI-generated answers and verify their sources.

Participants should also be able to identify practical use cases for AI in their professional activities.

## 3. Course Content

### Part 1: Understanding How AI Works

**Neural Networks (NNs)**
- A neural network learns a task by adjusting its weights during training.
- Training an AI model means optimizing these weights so that the network can perform a given task.

**Large Language Models (LLMs)**
- Text-generating AI models work by predicting the next token (word or part of a word).
- This prediction process is repeated to generate text.

**The importance of context**
- An LLM uses the context provided in the conversation to generate its answers.
- Its knowledge is fundamentally limited by the information acquired during training.
- It cannot automatically know about recent events or information published after its training.
- However, we can provide additional information directly in its context to help it answer questions accurately.

This raises an important question:
What information should we put into the model's context to help it answer correctly?

=> For this part, re-use the relevant live demo slides from this talk I made: `/home/paul/Documents/Talks/LibraryConference`

### Part 2: From Manual Context to RAG

Historically, providing external knowledge to an AI model was a manual process:

1. Search for relevant scientific articles or documents.
2. Copy and paste their contents into the conversation.
3. Ask the AI questions based on the provided information.

This approach works but quickly becomes impractical when dealing with large amounts of information.

**The idea behind Retrieval-Augmented Generation (RAG)**

RAG addresses this problem by connecting an AI model to an external knowledge base.

Instead of manually providing all relevant documents:

1. Build a knowledge base containing relevant documents and information.
2. When a user asks a question, search the knowledge base.
3. Retrieve the most relevant documents or passages (for example, the 20 most useful results).
4. Add these results to the model's context.
5. Let the model generate an answer based on the retrieved information.

This allows AI models to answer questions using external, up-to-date, and domain-specific knowledge.

Potential healthcare applications include searching scientific literature, retrieving clinical guidelines, and querying institutional documentation.

### Part 3: AI Tools and Agents

Another approach is to give AI models access to external tools.

The principle is simple:

- Tell the AI which tools it is allowed to use.
- When answering a question, the AI can decide which tools are relevant.
- For example, it can perform a Google search.
- The search results are returned and added to its context.
- The AI then uses this information to formulate its answer.

This extends the model's capabilities beyond the information it already possesses.

It also closely mimics how humans work: when we do not know something, we look it up, gather information, and use it to formulate an answer.

Tool use and agentic workflows have become central components of modern AI systems.

## 4. Best Practices When Using AI

1. Verify sources
2. Request visual explanations
3. Request interactive explanations

## 5. Practical Applications for Healthcare Educators

The training should include hands-on demonstrations centered around three concrete use cases.

### Use Case 1: Scientific Bibliography and Literature Reviews

Demonstrate how AI can help educators:
- Search for relevant scientific publications.
- Identify key papers on a specific medical or scientific topic.
- Summarize and compare scientific articles.
- Extract relevant information and references.
- Build structured bibliographies.
- Critically evaluate the scientific evidence.

### Use Case 2: AI-Powered Knowledge Bases (RAG)

Demonstrate how to:
- Create a knowledge base from scientific articles, course materials, guidelines, and institutional documents.
- Connect an AI assistant to this knowledge base.
- Ask questions in natural language.
- Retrieve relevant passages and obtain answers grounded in the original documents.
- Trace answers back to their sources.

The objective is to show how educators can build their own AI assistants specialized in their teaching domains.

### Use Case 3: Automated Emails

Demonstrate how AI can assist with email workflows:
- Draft professional emails.
- Adapt tone and wording to different audiences.
- Summarize incoming email threads.
- Extract action items and relevant information.
- Automate repetitive email responses and administrative communications.

Emphasize practical workflows that save time while keeping the educator in control of outgoing communications.

## 6. General Instructions for the Training Materials

When developing the training materials:

- Prioritize practical, real-world examples from healthcare, medicine, and scientific research.
- Use accessible language and avoid unnecessary technical jargon.
- Explain concepts progressively, starting with intuitive examples.
- Include concrete demonstrations wherever possible.
- Favor hands-on exercises over lengthy theoretical explanations.
- Use scientific literature and healthcare-related examples throughout the course.
- Make participants aware of AI limitations, hallucinations, and the importance of human verification.

The overall objective is to help healthcare educators understand modern AI capabilities and, more importantly, learn how to integrate these tools into their teaching, research, and administrative activities.

Read `AGENT.md`, make a plan on the material to create, and tools to create them.
Language: English
Length: a full day
Participants' tools: free accounts, but can have licence if needed
Laptops: participants will have their own laptops