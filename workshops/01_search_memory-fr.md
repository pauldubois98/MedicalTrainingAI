---
title: "Atelier 1 — Recherche web et mémoire"
---

# Atelier 1 : recherche web et mémoire

**Outil :** votre assistant IA (ChatGPT, Claude, Gemini, Le Chat…)

**Objectif :** voir par vous-même ce qu'un modèle sait seul, ce qu'apporte la recherche web, et ce qu'est vraiment la « mémoire ».

<div class="tip">

Les interfaces changent souvent, et les menus peuvent être en anglais. Si vous ne trouvez pas un réglage, cherchez sur Google (par exemple : « Comment désactiver la recherche web dans cette application ? »).

</div>

## Exercice 1 : un modèle sans recherche web

### Étape 1 : désactiver la recherche web

| Assistant | Comment désactiver la recherche web |
|---|---|
| **ChatGPT** | Paramètres → Personnalisation → Avancé → désactiver **Recherche web** |
| **Claude** | Menu « Recherche et outils » (sous la zone de message) → désactiver **Recherche web** |
| **Le Chat (Mistral)** | Menu des outils (sous la zone de message) → désactiver **Recherche web** |
| **Gemini** | Impossible dans l'application Gemini. Utilisez plutôt [Google AI Studio](https://aistudio.google.com) (gratuit, même compte Google) : l'option « Grounding with Google Search » est désactivée par défaut |

Ouvrez ensuite une **nouvelle conversation**.

### Étape 2 : posez des questions sur des faits postérieurs à son entraînement

Posez quelques-unes de ces questions, **une par nouvelle conversation** :

```
Qui a gagné les élections de mi-mandat américaines de 2026 ?
Donne-moi les résultats définitifs pour la Chambre et le Sénat.
```

```
Qui a reçu le prix Nobel de physiologie ou médecine 2026,
et pour quelle découverte ?
```

```
Quelle équipe a gagné la Coupe du monde de football 2026,
et quel était le score de la finale ?
```

```
Quels sont les principaux changements de la dernière mise à jour
de [une recommandation que vous enseignez, par exemple celle de
la HAS sur l'hypertension artérielle] ?
```

**Observez et notez :**

- Dit-il qu'il **ne sait pas** (en mentionnant sa date de coupure) ?
- **Devine**-t-il, ou invente-t-il une réponse assurée ?
- S'il invente : est-ce convaincant ? Un étudiant s'en rendrait-il compte ?

<div class="warn">

Les connaissances d'un modèle sont **figées à sa date de coupure**. Sans outil, il ne peut pas savoir ce qui s'est passé ensuite, mais il peut quand même répondre comme s'il le savait. (Les modèles récents ont des dates de coupure plus tardives : si une question obtient une bonne réponse, essayez-en une plus récente.)

</div>

## Exercice 2 : des modèles avec recherche web

### Étape 1 : réactiver la recherche web

Utilisez le même menu qu'à l'exercice 1 (dans Google AI Studio : activez **Grounding with Google Search**). Ouvrez une **nouvelle conversation**.

### Étape 2 : posez à nouveau les mêmes questions

Posez les mêmes questions, en ajoutant :

```
Donne tes sources, avec les liens.
```

**Observez :** la réponse est-elle différente ? Cite-t-il maintenant des sources ?

### Étape 3 : vérifiez les sources

Pour **deux** des réponses, ouvrez au moins **deux** des liens :

- La page existe-t-elle, et dit-elle **ce que l'IA affirme** ?
- La source est-elle **fiable** : organisme officiel, revue ou média reconnu, plutôt qu'un blog anonyme ou un forum ?
- L'information est-elle **à jour** (vérifiez la date de la page) ?

<div class="key">

**Qu'est-ce qui a changé ?** Le modèle est le même. La recherche web est un **outil** : le modèle cherche, les résultats sont ajoutés à son **contexte**, et il répond à partir d'eux. C'est la boucle d'agent vue ce matin. Les sources rendent la réponse **vérifiable**, pas automatiquement **juste**.

</div>

## Exercice 3 : des modèles avec mémoire

Beaucoup d'assistants peuvent **se souvenir** de choses sur vous d'une conversation à l'autre. Voyons ce que cela veut vraiment dire.

### Étape 1 : vérifiez que la mémoire est activée

| Assistant | Où trouver la mémoire |
|---|---|
| **ChatGPT** | Paramètres → Personnalisation → **Mémoire** (« Mémoires enregistrées », « Historique des conversations ») |
| **Claude** | Paramètres → Fonctionnalités → **Mémoire** |
| **Gemini** | Paramètres → **Contexte personnel** / Infos enregistrées |
| **Le Chat (Mistral)** | Paramètres → **Mémoires** |

Si votre assistant n'a pas de mémoire sur un compte gratuit, mettez-vous en binôme avec quelqu'un dont l'assistant en a une.

### Étape 2 : présentez-vous

Dans une conversation, écrivez :

```
Retiens ceci pour nos prochaines conversations :
- J'enseigne aux [étudiants infirmiers de 2e année] à l'École des
  sciences de la santé Saint-Aldric.
- Ma matière est [la prévention des infections].
- Je préfère des réponses courtes, avec des tableaux si possible.
```

Vérifiez qu'il confirme l'avoir enregistré (dans ChatGPT, un message « Mémoire mise à jour » apparaît).

### Étape 3 : ouvrez une nouvelle conversation

Ouvrez une **nouvelle** conversation et demandez, sans autre précision :

```
Propose-moi une activité de 10 minutes pour commencer mon prochain cours.
```

**Observez :** l'activité est-elle adaptée à vos étudiants, à votre matière et à votre format ? Puis demandez :

```
Que sais-tu de moi ?
```

### Étape 4 : consultez, modifiez et effacez la mémoire

Retournez dans les réglages de la mémoire et **ouvrez la liste des mémoires enregistrées** :

- Qu'est-ce qui a été enregistré exactement ? Est-ce **mot pour mot** ce que vous avez écrit, ou un résumé ?
- **Effacez** un élément (par exemple votre matière), ouvrez une nouvelle conversation et reposez la même question. Qu'est-ce qui a changé ?

### Étape 5 : une conversation sans mémoire

Ouvrez une **conversation temporaire** (ChatGPT : *Discussion temporaire* ; Claude : *Conversation incognito* ; Gemini : *Discussion temporaire*) et reposez la même question. La réponse est-elle encore personnalisée ?

<div class="key">

**Qu'est-ce que la mémoire ?** Les mémoires enregistrées ne sont que du **texte que l'assistant ajoute au contexte** au début de chaque conversation, comme une note que vous colleriez vous-même. Le modèle lui-même ne change pas et n'apprend pas : effacez la note, et la « mémoire » disparaît.

</div>

<div class="warn">

**N'enregistrez jamais** d'informations sur des patients, ni d'informations personnelles sur des étudiants ou des collègues, dans la mémoire d'un assistant. Relisez régulièrement vos mémoires enregistrées, et effacez ce que vous avez ajouté aujourd'hui si vous ne voulez pas le garder.

</div>

## Pour aller plus loin

**Instructions personnalisées :** la plupart des assistants ont aussi un champ pour des instructions permanentes (ChatGPT : *Personnaliser ChatGPT* ; Claude : *Préférences personnelles*).
