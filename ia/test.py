import os
from mistralai import Mistral
import json

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

parcelles = [
    {
        "id": 1,
        "nom": "Parcelle A",
        "ville": "Paris",
        "proximite_commerces": "élevée",
        "attractivite_ville": "forte",
        "pollution": "modérée",
        "prix_m2": 12000
    },
    {
        "id": 2,
        "nom": "Parcelle B",
        "ville": "Lyon",
        "proximite_commerces": "moyenne",
        "attractivite_ville": "moyenne",
        "pollution": "faible",
        "prix_m2": 8000
    },
    {
        "id": 3,
        "nom": "Parcelle C",
        "ville": "Marseille",
        "proximite_commerces": "élevée",
        "attractivite_ville": "moyenne",
        "pollution": "élevée",
        "prix_m2": 5000
    }, 
    {
        "id": 4,
        "nom": "Parcelle D",
        "ville": "Bordeaux",
        "proximite_commerces": "moyenne",
        "attractivite_ville": "forte",
        "pollution": "faible",
        "prix_m2": 10000
    }
]

centres_interet = ["proximite_commerces", "pollution", "prix_m2", "attractivite_ville"]


roles = {
    "investisseur": "Tu es un expert en investissement immobilier. Analyse les parcelles sous l'angle de la rentabilité financière, du potentiel de croissance et de la valorisation immobilière.",
    "bien-être": "Tu es un conseiller en qualité de vie et bien-être résidentiel. Analyse les parcelles sous l'angle du confort de vie, de l'environnement, des nuisances et des services à proximité.",
    "ecologiste": "Tu es un expert en écologie et développement durable. Analyse les parcelles sous l'angle de l'impact environnemental, de la pollution, de la biodiversité locale et des infrastructures écologiques disponibles (espaces verts, transports durables, gestion des déchets, etc.)."
}


role_utilisateur = "investisseur"

parcelles_filtrees = [
    {k: v for k, v in parcelle.items() if k in ["nom", "ville"] + centres_interet}
    for parcelle in parcelles
]

parcelles_json = json.dumps(parcelles_filtrees, indent=2, ensure_ascii=False)

prompt = f"""
{roles.get(role_utilisateur, "Tu es un expert en immobilier.")}

L'utilisateur souhaite comparer des parcelles en fonction des critères suivants : {", ".join(centres_interet)}.
Présente une analyse claire et argumentée.

Voici les données filtrées des parcelles :
{json.dumps(parcelles_filtrees, indent=2, ensure_ascii=False)}

Compare ces parcelles sur les critères donnés et donne une recommandation finale.

 **FORMAT STRICT DE RÉPONSE (respecte cet ordre) :**  
 **Introduction** : Brève explication des critères analysés.  
 **Analyse détaillée** : Comparaison des parcelles en langage naturel.  
 **Tableau comparatif** : Un tableau **formaté en texte brut** avec une **note sur 5** pour chaque critère.

 **Exemple de format du tableau attendu :**

```markdown

```
| Critère                 | Parcelle A | Parcelle B |
|-------------------------|-----------|-----------|
| Proximité commerces    | 5/5       | 3/5       |
| Pollution              | 2/5       | 4/5       |
| Transports publics     | 4/5       | 3/5       |
```

```

Donne une réponse détaillée **en respectant strictement ce format**.
"""


chat_response = client.chat.complete(
    model= model,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
print(chat_response.choices[0].message.content)



