---
title: "Aide-mémoire — Utiliser l'IA quand on enseigne la santé"
---

# Aide-mémoire : utiliser l'IA quand on enseigne la santé

## Comment fonctionne l'IA

1. Un **LLM prédit du texte**, token par token : sa réponse est la suite la plus *plausible*, pas forcément la plus *vraie*.
2. Il ne sait que ce qu'il a appris pendant son **entraînement** (figé à une date de coupure) et ce qui est dans son **contexte** (la conversation).
3. Le **RAG** ajoute automatiquement au contexte les passages pertinents d'une base de connaissances, et la réponse les cite.
4. Les **agents** utilisent des outils (recherche web, PubMed, documents, e-mail) pour aller chercher des informations ou agir, et ajoutent les résultats à leur contexte.

## Bien formuler une demande

| | Exemple |
|---|---|
| **Rôle** | « Tu es un formateur en soins infirmiers expérimenté. » |
| **Contexte** | « Mes étudiants sont en 1re année, avant leur premier stage. » |
| **Tâche** | « Écris 10 QCM sur l'hygiène des mains. » |
| **Format** | « Sous forme de tableau : question, 4 propositions, réponse, explication en une ligne. » |
| **Sources** | « Appuie-toi uniquement sur la recommandation jointe, et cite la section. » |
| **Itérer** | « Rends les questions 3 et 7 plus difficiles. Ajoute un cas clinique. » |

## Demandes utiles

- **Expliquer :** « Explique [notion] à un étudiant de 1re année, avec une analogie, puis vérifie ma compréhension avec 3 questions. »
- **Visuel :** « Fais un schéma de [processus] » · « Compare [A, B, C] dans un tableau » · « Place [étapes] sur une frise chronologique. »
- **Interactif :** « Crée une page interactive / un quiz / des cartes mémo sur [thème] pour mes étudiants. »
- **Littérature :** « Trouve des revues systématiques des 10 dernières années sur [thème], avec DOI/PMID et liens. »
- **Lecture critique :** « Joue le rôle d'un relecteur critique de cet article : risques de biais, limites, questions à se poser. »
- **Conception de cours :** « Écris 5 objectifs pédagogiques mesurables pour [séance] » · « Transforme ces objectifs en plan de séance de 2 heures, sous forme de tableau » · « Chaque objectif est-il enseigné et évalué ? »
- **Supports :** « Transforme ces notes de cours en cas clinique avec 3 points de décision. »

## Check-list avant d'utiliser une réponse

- [ ] Ai-je **ouvert et lu** les sources ? (DOI → le *bon* article ? Dit-il ce que l'IA affirme ?)
- [ ] Les **chiffres, doses, dates et noms** sont-ils exacts ?
- [ ] Est-ce cohérent avec les **recommandations en vigueur** et les règles de mon établissement ?
- [ ] Ai-je retiré toutes les **données patients et personnelles** avant d'utiliser l'outil ?
- [ ] Serais-je à l'aise de signer ce document de **mon nom** ?

## Outils cités aujourd'hui

| Besoin | Outils (version gratuite disponible) |
|---|---|
| Assistant généraliste | Claude, ChatGPT, Gemini, Le Chat, Copilot |
| Recherche bibliographique | PubMed, Consensus, Elicit, Semantic Scholar, Google Scholar |
| Références | Zotero |
| Base de connaissances (RAG) | NotebookLM ; Projets dans Claude / ChatGPT |
| Conception de cours | N'importe quel assistant, avec vos notes de cours dans un projet (Claude, ChatGPT) ou un notebook NotebookLM |
