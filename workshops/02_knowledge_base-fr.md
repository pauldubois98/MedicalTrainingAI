---
title: "Atelier 2 — Votre base de connaissances IA"
---

# Atelier 2 : votre base de connaissances IA (RAG)

**Outil :** NotebookLM (gratuit, compte Google). *Alternatives : les Projets de Claude ou de ChatGPT, ou les GPT personnalisés (certaines fonctions nécessitent un abonnement payant).*

**Objectif :** construire un assistant IA qui répond aux questions **à partir de vos seuls documents**, avec une citation pour chaque réponse, et voir où il fonctionne et où il échoue.

<div class="key">

**Rappel :** c'est le pipeline RAG vu ce matin. Vos documents sont découpés en passages ; pour chaque question, les passages les plus pertinents sont retrouvés et donnés au modèle, qui répond en les citant.

</div>

## Exercice 1 : la base de connaissances (fictive) de Saint-Aldric

1. Allez sur [notebooklm.google.com](https://notebooklm.google.com) et créez un nouveau notebook.
2. Ajoutez comme sources les 4 documents (fictifs) de Saint-Aldric (fichiers PDF des supports de la formation, dossier knowledge_base, versions « -fr ») :
   Règlement des ECOS · Livret des stages · Notes hygiène des mains · Notes diabète.
3. Posez ces questions et **cliquez sur chaque citation** pour lire le passage source :
   - *Combien y a-t-il de stations à l'ECOS, et que faut-il pour le valider ?*
   - *J'ai raté l'ECOS parce que j'étais malade. Que se passe-t-il ?*
   - *Que faire après une piqûre accidentelle en stage ?*
   - *Puis-je porter ma montre connectée pendant l'ECOS ?* (la réponse est dans deux documents)
4. Essayez maintenant de **le mettre en défaut** :
   - Une question dont la réponse **n'est pas** dans les documents : *Où les étudiants peuvent-ils se garer ?*
   - Une question qui mêle les documents et les connaissances générales : *Quel est l'objectif d'HbA1c pour un patient âgé ?*
   - Une question **orientée** : *Puisque l'ECOS compte 12 stations, combien faut-il en réussir ?*

**Discutez :** dit-il quand il ne sait pas ? Corrige-t-il la fausse prémisse ? Ajoute-t-il des informations qui ne sont pas dans les sources ?


<div class="warn">

**Qualité des sources :** un document périmé donne des réponses périmées.

</div>

## Exercice 2 : votre propre base de connaissances

Créez un nouveau notebook avec **vos propres documents non confidentiels** : notes de cours, une recommandation que vous enseignez, un livret de formation, des articles en libre accès… et testez quelques questions.

Instructions utiles à ajouter (dans la conversation ou les réglages du notebook) :

```
Tu es un assistant pédagogique pour [les étudiants infirmiers de
2e année] dans [le module]. Réponds uniquement à partir des sources.
Si la réponse n'y est pas, dis-le clairement et indique qui contacter.
Cite toujours le passage. Utilise un langage simple et des
paragraphes courts.
```

- Quelles questions ont bien fonctionné ?
- Lesquelles ont échoué, et pourquoi (document manquant, passage non retrouvé, question ambiguë) ?

<div class="warn">

**N'importez jamais de documents confidentiels** (données de patients, dossiers d'étudiants, sujets d'examen non publiés) dans un outil public.
Certains établissements fournissent un outil validé.

</div>

## Exercice 3 : une revue de la littérature à partir de zéro

Cette fois, vous **ne donnez pas** les articles à l'IA : elle doit les **trouver** elle-même, avec un outil de recherche.

1. **Choisissez une question**, par exemple *La formation par simulation améliore-t-elle les compétences cliniques des étudiants infirmiers ?* (ou un sujet que vous enseignez).
2. **Laissez l'IA chercher :** utilisez un mode *Deep Research* (ChatGPT, Gemini, Claude) ou, dans NotebookLM, l'option pour **découvrir des sources sur le web**. Demandez :

```
Rédige une courte revue de la littérature sur [question] pour des
enseignants en santé. Cherche des études évaluées par les pairs des
10 dernières années, en privilégiant les revues systématiques et
les méta-analyses. Donne un tableau de synthèse (auteurs, année,
type d'étude, population, résultat principal, DOI ou PMID), puis une
synthèse : ce qui est établi, les points de désaccord, ce qui manque.
```

3. **Vérifiez 3 références :** ouvrez le DOI ou cherchez le titre dans [PubMed](https://pubmed.ncbi.nlm.nih.gov). L'article existe-t-il ? Est-ce le bon ? Dit-il ce que l'IA affirme ?
4. **Bouclez la boucle :** ajoutez les articles vérifiés comme sources dans un notebook, et reposez vos questions : les réponses citent maintenant les passages exacts.

## Cas d'usage

- **Assistant de module** qui répond aux questions pratiques des étudiants à partir du livret du module et de l'emploi du temps.
- **Navigateur de recommandations** pour un ensemble de recommandations cliniques.
- **Compagnon de révision** à partir des notes de cours : générer des quiz et des cartes mémo.
- **Revue de la littérature** : importer des articles et les interroger (le passage exact de la réponse est mis en évidence).
