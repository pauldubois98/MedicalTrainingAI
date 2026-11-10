"""French text of the diagrams: English string (as written in figures.py) → French string.

figures.py draws every figure twice: once in English (figures/name.svg) and once with
these translations (figures/name-fr.svg). Strings missing from this table are drawn
unchanged, and listed by figures.py so that nothing is forgotten.
"""

FR = {
    # cats_ml
    "cat": "chat", "not a cat": "pas un chat",
    "thousands of labelled examples": "des milliers d'exemples étiquetés",
    "training": "entraînement", "cat: 97%": "chat : 97 %", "new image": "nouvelle image",
    # neuron
    "inputs": "entrées", "weights": "poids", "sum": "somme", "activation": "activation",
    "output": "sortie",
    # scale_params
    "Demo\nnetwork": "Réseau\nde démo", "Reading digits\n(1998)": "Lecture de\nchiffres (1998)",
    "60,000": "60 000", "1.5 billion": "1,5 milliard", "175 billion": "175 milliards",
    "Today's large\nmodels": "Grands modèles\nactuels", "~1,000 billion?": "~1 000 milliards ?",
    "number of weights (log scale)": "nombre de poids (échelle log)",
    # training_loop
    "Example\n(data)": "Exemple\n(données)", "Model's\nprediction": "Prédiction\ndu modèle",
    "Compare with\nthe right answer": "Comparaison avec\nla bonne réponse", "Error": "Erreur",
    "Adjust\nthe weights": "Ajustement\ndes poids", "× millions of times": "× des millions de fois",
    # tokens
    "Characters": "Caractères", "Words": "Mots", "Tokens": "Tokens", "units": "unités",
    "Characters:": "Caractères :", "Words:": "Mots :", "Tokens:": "Tokens :",
    "few symbols, but very long sequences": "peu de symboles, mais des séquences très longues",
    "short sequences, but an endless vocabulary (drug names, typos…)":
        "séquences courtes, mais vocabulaire sans fin (médicaments, fautes de frappe…)",
    "the compromise: frequent chunks, ~50,000 to 200,000 in total":
        "le compromis : des morceaux fréquents, ~50 000 à 200 000 au total",
    # temperature
    "Low temperature (0.3)": "Température basse (0,3)", "Normal (1)": "Normale (1)",
    "High (2.5)": "Élevée (2,5)",
    # conversation
    "What the user sees": "Ce que voit l'utilisateur",
    "Can you explain the WHO 5 moments?": "Explique-moi les 5 moments de l'OMS.",
    "Of course! Are you preparing\na lecture or a quick quiz?": "Bien sûr ! Tu prépares\nun cours ou un petit quiz ?",
    "A quiz for Year 1 students.": "Un quiz pour des 1re année.",
    "What the LLM sees": "Ce que voit le LLM",
    "A conversation between a user and a helpful assistant.": "Dialogue entre un utilisateur et un assistant.",
    "User: Can you explain the WHO 5 moments?": "Utilisateur : Explique-moi les 5 moments de l'OMS.",
    "Assistant: Of course! Are you preparing": "Assistant : Bien sûr ! Tu prépares",
    "   a lecture or a quick quiz?": "   un cours ou un petit quiz ?",
    "User: A quiz for Year 1 students.": "Utilisateur : Un quiz pour des 1re année.",
    "Assistant:": "Assistant :",
    "one long text, continued token by token": "un seul long texte, prolongé token par token",
    # knowledge_cutoff
    "✅ Seen during training": "✅ Vu pendant l'entraînement",
    "frozen at the cutoff date": "figé à la date de coupure",
    "Books, textbooks": "Livres, manuels", "Published articles": "Articles publiés",
    "Public websites": "Sites web publics", "Guidelines up to the cutoff": "Recommandations jusqu'à la coupure",
    "❌ Never seen": "❌ Jamais vu",
    "the model may still invent an answer": "le modèle peut quand même inventer une réponse",
    "After the cutoff": "Après la coupure",
    "new guidelines, recent studies": "nouvelles recommandations, études récentes",
    "Private": "Privé", "your regulations, course materials, emails": "vos règlements, supports de cours, e-mails",
    "time": "temps",
    # manual_context
    "1. Search": "1. Chercher", "PubMed, guidelines,\ncourse files…": "PubMed, recommandations,\nsupports de cours…",
    "2. Copy & paste": "2. Copier-coller", "into the\nconversation": "dans la\nconversation",
    "3. Ask": "3. Demander", "questions about\nthe documents": "des questions sur\nles documents",
    "✓ Works well for a few documents": "✓ Fonctionne bien pour quelques documents",
    # rag_pipeline
    "Once: build the knowledge base": "Une fois : construire la base de connaissances",
    "articles, guidelines, courses…": "articles, recommandations, cours…",
    "split": "découpage", "index": "indexation",
    "🗄️ Knowledge base": "🗄️ Base de\nconnaissances",
    "For each question": "Pour chaque question", "🔎 Search": "🔎 Recherche",
    "top k passages": "les k meilleurs passages",
    "✅ Answer grounded in the passages, with citations [1] [2]":
        "✅ Réponse fondée sur les passages, avec citations [1] [2]",
    # chatbot_vs_agent
    "User": "Utilisateur", "📝 Text": "📝 Texte",
    "stays in the world of text": "reste dans le monde du texte",
    "it can look things up, and act": "il peut chercher des informations, et agir",
    # human_vs_agent
    "👩‍⚕️ A teacher": "👩‍⚕️ Un enseignant", "“I don't know”": "« Je ne sais pas »",
    "Look it up\n(PubMed, guideline)": "Chercher\n(PubMed, recommandation)",
    "Read the\nresults": "Lire les\nrésultats", "Answer, citing\nthe source": "Répondre en\ncitant la source",
    "🤖 An AI agent": "🤖 Un agent IA", "Missing\ninformation": "Information\nmanquante",
    "Call a tool\n(search)": "Appeler un outil\n(recherche)",
    "Results added\nto its context": "Résultats ajoutés\nà son contexte",
    # knowledge_sources
    "Training": "Entraînement",
    "what it learned,\nfrozen at the\ncutoff date": "ce qu'il a appris,\nfigé à la date\nde coupure",
    "Pasted context": "Contexte collé",
    "documents you\ncopy into the\nconversation": "documents que vous\ncopiez dans la\nconversation",
    "passages retrieved\nautomatically from\na knowledge base": "passages retrouvés\nautomatiquement dans\nune base de connaissances",
    "Tools / agents": "Outils / agents",
    "searches the web,\nPubMed… when it\ndecides it needs to": "cherche sur le web,\ndans PubMed… quand\nil le juge utile",
    "more up to date, more specific… and more sources to check":
        "plus à jour, plus spécifique… et plus de sources à vérifier",
    # fake_reference (the reference itself stays in English, as in a real bibliography)
    "✓ plausible authors": "✓ auteurs plausibles", "✓ realistic title": "✓ titre réaliste",
    "✓ real journal": "✓ revue réelle", "✗ article does not exist": "✗ l'article n'existe pas",
    "🔎 DOI → doi.org · title → PubMed / Scholar": "🔎 DOI → doi.org · titre → PubMed / Scholar",
    "Fabricated example, made for this course": "Exemple inventé pour cette formation",
}

# Strings that are the same in French (not reported as missing)
SAME = {"Agent", "Chatbot", "Documents", "E-mail", "LLM", "PubMed", "RAG", "Web", "passages",
        "❓ Question", "🧠 LLM", "GPT-2\n(2019)", "GPT-3\n(2020)", "b", "f", "y", "Σ",
        "w₁", "w₂", "w₃", "x₁", "x₂", "x₃",
        # the fabricated reference is a (fake) English-language article
        "Martin L, Okafor C, Lindqvist S.", "Effect of high-fidelity simulation on nursing",
        "students' clinical judgement: a randomized", "controlled trial. J Nurs Educ. 2021;60(4):212-219.",
        "doi:10.3928/01484834-20210322-99"}
