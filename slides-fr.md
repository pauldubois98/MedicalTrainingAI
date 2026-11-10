---
title: "L'IA pour les enseignants en santé"
subtitle: "Comment fonctionne l'IA moderne, et comment l'utiliser pour enseigner, chercher et administrer"
lang: fr
---

## Contenu

<div class="cards c2" style="text-align:left; align-items:start">
<div class="card t">
<b style="font-size:1.1em; margin-bottom:.4em">Théorie</b>
<table class="agenda">
<tr><td>1</td><td>Comment l'IA apprend</td></tr>
<tr><td>2</td><td>Contexte, RAG, outils et agents</td></tr>
<tr><td>3</td><td>Bonnes pratiques</td></tr>
</table>
</div>
<div class="card o">
<b style="font-size:1.1em; margin-bottom:.4em">Pratique</b>
<table class="agenda">
<tr><td>1</td><td>Atelier : recherche web et mémoire</td></tr>
<tr><td>2</td><td>Atelier : base de connaissances IA</td></tr>
<tr><td>3</td><td>Atelier : concevoir un cours</td></tr>
</table>
</div>
</div>

<div class="big-q" style="font-size:1em">
   L'IA évolue <em>vite</em> : ce contenu pourrait bientôt être dépassé.
</div>

## À quoi utilisez-vous déjà l'IA ? {.question}

<div class="big-q">
   À quoi utilisez-vous <em>déjà</em> l'IA ?<br>
   À quoi <em>aimeriez</em>-vous l'utiliser ?
</div>

## Comment fonctionne l'IA ? {.divider}

## Apprentissage automatique : apprendre par l'exemple

![](figures/cats_ml-fr.svg){.fig}

## Un neurone peut apprendre

![](figures/neuron-fr.svg){.fig}

## Entraîner un réseau de neurones à la main

<iframe class="demo" data-src="demos/network-fr.html?ni=2&nh=1&hs=2&no=1&act=step&t=XOR"></iframe>

## Entraîner, *c'est* ajuster les poids

![](figures/training_loop-fr.svg){.fig}

## Entraînement automatique

<iframe class="demo" data-src="demos/training-fr.html"></iframe>

## Des modèles toujours plus grands

![](figures/scale_params-fr.svg){.fig}

## Prédire la suite

<div class="big-q" style="font-size:1.4em; margin-top:1.2em">« Le paracétamol sert à faire baisser la <span class="violet">___</span> »</div>

::: {.fragment}
<div class="big-q orange" style="font-size:1.4em">→ fièvre</div>
:::

::: {.fragment}
<div class="big-q" style="font-size:1.1em; margin-top:1em">« Le paracétamol sert à faire baisser la fièvre et à soulager les <span class="violet">___</span> »</div>
:::
::: {.fragment}
<div class="big-q orange" style="font-size:1.1em">→ douleurs</div>
:::

## Prédire la lettre suivante

<iframe class="demo" data-src="demos/letters-fr.html"></iframe>

## Caractères, mots, tokens

![](figures/tokens-fr.svg){.fig}

## Token par token

<iframe class="demo" data-src="demos/token-fr.html"></iframe>

## Pourquoi les réponses varient

<iframe class="demo" data-src="demos/temperature-fr.html"></iframe>

## Une conversation n'est qu'un long texte

![](figures/conversation-fr.svg){.fig}

## Ce que sait le modèle… et ce qu'il ignore

![](figures/knowledge_cutoff-fr.svg){.fig}

## L'importance du contexte

<iframe class="demo" data-src="demos/context-fr.html"></iframe>

## La question clé {.question}

<div class="big-q">Quelles informations mettre<br>dans le <em>contexte</em> du modèle<br>pour l'aider à bien répondre ?</div>

## Du contexte manuel au RAG {.divider}

## La méthode manuelle

![](figures/manual_context-fr.svg){.fig-s}

<div class="cards c3 tight vc">
<div class="card r fragment"><b>⏱ Lent et répétitif</b></div>
<div class="card r fragment"><b>📏 Taille de contexte limitée</b></div>
<div class="card r fragment"><b>❓ Quels documents choisir ?</b></div>
</div>

## Génération augmentée par la recherche (RAG)

![](figures/rag_pipeline-fr.svg){.fig}

## Le RAG pas à pas

<iframe class="demo" data-src="demos/rag-fr.html"></iframe>

## Le RAG en formation santé

<div class="cards c3 tight">
<div class="card t"><div class="e">📚</div><b>Littérature scientifique</b>Interroger tout un corpus d'articles</div>
<div class="card o"><div class="e">📋</div><b>Recommandations cliniques</b>Trouver la bonne recommandation, avec le passage exact</div>
<div class="card g"><div class="e">🏫</div><b>Documents de l'établissement</b>Règlements, livrets, supports de cours : un assistant 24 h/24 pour les étudiants</div>
</div>

<div class="msg fragment">Outils : NotebookLM, Projets Claude, Projets ChatGPT…</div>

<div class="fragment">
<div class="cards c3 tight">
<div class="card r"><b>🔎 La recherche peut rater</b>le bon passage</div>
<div class="card r"><b>🗑️ Mauvais documents,<br>mauvaises réponses</b>des documents périmés ou faux donnent des réponses fausses</div>
<div class="card g"><b>✅ Les citations rendent les réponses vérifiables</b>lisez la source en cas de doute</div>
</div>
</div>

## Outils et agents {.divider}

## Du chatbot à l'agent

![](figures/chatbot_vs_agent-fr.svg){.fig}

## Comme nous

![](figures/human_vs_agent-fr.svg){.fig}

## Un agent au travail

<iframe class="demo" data-src="demos/agent-fr.html"></iframe>

## Quatre façons pour un modèle de « savoir »

![](figures/knowledge_sources-fr.svg){.fig}

## Un modèle, plusieurs façons de l'utiliser

<div class="fm">🧠 <b>Modèle de fondation</b><span>entraîné une fois, à grands frais : GPT, Claude, Gemini, Llama, Mistral…</span></div>
<div class="fm-arrows">↙ &nbsp; ↓ &nbsp; ↘</div>

<div class="cards c3 tight">
<div class="card t fragment"><div class="e">💬</div><b>Application de chat</b>ChatGPT, Claude.ai, Gemini…<br><br><span class="muted">pour tout le monde</span></div>
<div class="card o fragment"><div class="e">🔌</div><b>API</b>un logiciel envoie du texte,<br>reçoit du texte<br>paiement au token, sans interface<br><span class="muted">pour les développeurs et les outils institutionnels</span></div>
<div class="card g fragment"><div class="e">💻</div><b>Agent IA</b>un LLM avec accès à un ordinateur virtuel<br><br><span class="muted">pour les tâches longues et complexes</span></div>
</div>

## Comparer les LLM

<div class="cards c2 tight" style="text-align:left">
<div class="card o">
<div class="e">💯</div><b>Qualité</b>
<span>avec LMArena ⚔️</span>
<ol class="arena">
<li>Posez n'importe quelle question sur <a href="https://lmarena.ai">lmarena.ai</a></li>
<li>Deux modèles <em>anonymes</em> répondent</li>
<li>Vous votez pour la meilleure réponse</li>
<li>Des millions de votes → un classement public</li>
</ol>
</div>
<div class="card t">
<div class="e">💶</div><b>Coûts</b>
<table class="costs">
<tr><td>Gratuit</td><td>0 €, usage limité</td></tr>
<tr><td>Abonnement</td><td>≈ 20 € / mois</td></tr>
<tr><td>API</td><td>par million de tokens :<br>de &lt; 1 € à ~10 €</td></tr>
</table>
<span class="muted" style="font-size:.85em">1 million de tokens ≈ 750 000 mots</span>
</div>
</div>

## Bonnes pratiques

<div class="bp">
<div>
<img src="figures/fake_reference-fr.svg" alt="Une référence inventée">
<div class="msg">Dans une étude ancienne (2023), 55 % des références produites par <span style="white-space:nowrap">GPT-3.5</span> étaient inventées, 18 % pour GPT-4.</div>
</div>
<div class="fragment">
<div class="card r"><b>🚫 Données</b> : ne jamais donner de données patient identifiantes à un outil d'IA public</div>
<div class="card g"><b>✅ Rôle</b> : ajouter « Tu es un formateur en soins infirmiers expérimenté… » à la demande.</div>
<div class="card t"><b>💡 Public</b> : ajouter « explique à un adolescent » à la demande.</div>
</div>
</div>

<div class="src">Walters WH & Wilder EI, « Fabrication and errors in the bibliographic citations generated by ChatGPT », Scientific Reports 13, 14045 (2023). <a href="https://doi.org/10.1038/s41598-023-41032-5">doi:10.1038/s41598-023-41032-5</a></div>

## Ateliers pratiques {.divider}

## Atelier 1 : recherche web et mémoire

<div class="cards c3 tight">
<div class="card r"><div class="e">🚫</div><b>Sans recherche web</b>questions sur l'actualité récente : sait‑il, ou invente‑t‑il ?</div>
<div class="card g"><div class="e">🌐</div><b>Avec recherche web</b>mêmes questions, avec des sources à vérifier</div>
<div class="card o"><div class="e">🧠</div><b>Mémoire</b>ce qui est enregistré, où, et comment l'effacer</div>
</div>

<div class="msg">Fiche : workshops/01_search_memory-fr</div>

## Atelier 2 : votre base de connaissances IA

<div class="cards c3">
<div class="card t"><div class="e">📂</div><b>Importer</b>des documents dans NotebookLM</div>
<div class="card o"><div class="e">❓</div><b>Poser</b>des questions en langage courant</div>
<div class="card r"><div class="e">🔗</div><b>Remonter</b>de chaque réponse à sa source</div>
</div>

<div class="msg">Fiche : workshops/02_knowledge_base-fr</div>

## Atelier 3 : concevoir un cours

<div class="cards c4">
<div class="card t"><div class="e">🎯</div><b>1. Objectifs et plan</b>définir les objectifs, demander un plan de séance</div>
<div class="card o"><div class="e">🔁</div><b>2. Itérer sur le plan</b>avant d'écrire le moindre support</div>
<div class="card g"><div class="e">🧩</div><b>3. Supports</b>diapositives, pages interactives, exercices, quiz</div>
<div class="card r"><div class="e">🔁</div><b>4. Itérer sur les supports</b>jusqu'à ce qu'ils soient satisfaisants</div>
</div>

<div class="msg">Fiche : workshops/03_course_design-fr</div>

## À retenir

<ol class="retenir">
<li class="fragment"><div>Un LLM <b>prédit du texte</b>, token par token.</div></li>
<li class="fragment"><div>Ses réponses dépendent de son <b>contexte</b>.</div></li>
<li class="fragment"><div>Le <b>RAG</b> et les <b>outils</b> vont chercher l'information automatiquement.</div></li>
<li class="fragment"><div><b>Vérifiez</b> les sources.</div></li>
<li class="fragment"><div><b>Protégez</b> les données des patients.</div></li>
</ol>

## Sources

<div style="text-align:left; font-size:20px; max-width:1150px; margin:0 auto; line-height:1.55">

- Walters WH, Wilder EI. *Fabrication and errors in the bibliographic citations generated by ChatGPT*. Scientific Reports 13, 14045 (2023). <https://doi.org/10.1038/s41598-023-41032-5>
- Singhal K et al. *Large language models encode clinical knowledge*. Nature 620, 172–180 (2023). <https://doi.org/10.1038/s41586-023-06291-2>
- Thirunavukarasu AJ et al. *Large language models in medicine*. Nature Medicine 29, 1930–1940 (2023). <https://doi.org/10.1038/s41591-023-02448-8>
- Lewis P et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. <https://arxiv.org/abs/2005.11401>
- Organisation mondiale de la santé. *WHO Guidelines on Hand Hygiene in Health Care* (2009).
- Démonstrations interactives adaptées de la conférence « IA & société » (P. Dubois, 2026).

</div>
