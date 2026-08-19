# Carte de décision personnelle — M4-B1

> **Ton ébauche perso** de la grille de décision C4, **avant** la
> restitution collective de mercredi. À confronter aux propositions des
> autres pour construire la grille commune.
> Auteur : `<prénom>` — Date : `<date>`

## Critères que je mobilise (mon ordre de priorité)

1. Performance prédictive : MAE / RMSE faibles et R² élevé
2. Robustesse des performances selon les périodes
3. Latence d'inférence et coût de calcul
4. Explicabilité du modèle

## Modèles que j'ai benchmarkés

> Liste rapide.

- Famille A : Ridge
- Famille B : RandomForestRegressor
- Famille C : HistGradientBoostingRegressor

## Pour quel cas je choisirais chaque famille ?

> Si Inès me demandait *« et pour un cas X, vous prendriez quoi ? »*.


| Cas | Famille recommandée | Pourquoi |
|---|---|---|
| **Mistral Bike Sharing (saisonnalité forte)** | HistGradientBoosting | Meilleures performances du benchmark : MAE 49,84, RMSE 74,03 et R² 0,805 |
| **Cas similaire mais 100 lignes seulement** | Ridge | Modèle simple, peu de paramètres et risque de surapprentissage plus facile à maîtriser sur un très petit dataset |
| **Cas avec exigence d'explicabilité réglementaire** | Ridge | Les coefficients permettent de comprendre directement l'influence des variables sur la prédiction |
| **Cas avec latence < 5 ms imposée** | Ridge ou HistGradientBoosting | Les deux respectent la contrainte dans le benchmark ; HistGradientBoosting serait privilégié si la précision reste prioritaire |

## Analyse éthique et réglementaire (C2)

> ~5 lignes. Le geste : **évaluer s'il existe réellement des risques**, puis
> **conclure**. Conclure « risque faible » est une réponse valide et
> professionnelle — pas besoin d'inventer un problème.

- Le dataset contient-il des **données personnelles** ? 
- - Le dataset ne semble pas contenir de données personnelles directement identifiantes.

- Utilise-t-on un **attribut sensible** / y a-t-il un risque de **biais** envers une population ?
- - Les variables utilisées ne correspondent pas à des attributs sensibles concernant des individus.

- Y a-t-il un enjeu **RGPD / confidentialité** ? 
- - Le risque RGPD et de discrimination directe est donc faible dans le cadre de cet usage.
- Quel **impact sociétal** de l'usage du modèle (destinataires directs/indirects) ? 
- - Le modèle peut toutefois influencer indirectement des décisions opérationnelles de tarification ou de disponibilité.

- **Conclusion** : ... (ex. *« données agrégées, pas de PII → risque faible ;
  si on exploitait des trajets individuels, il faudrait une analyse RGPD +
  minimisation + réidentification »*)

## Ouverture — Robustesse d'une solution d'IA (hors C2, prépare M7)

> Cette activité **ne relève pas de C2**. C'est un **complément à ta décision
> C4** et une ouverture vers **M7** (menaces sur les systèmes d'IA) : un réflexe
> pro = évaluer les limites d'un modèle au-delà de ses performances. Une ligne
> suffit. Cf. mini-cours `06_Menaces_robustesse_essentiel.md`.

- **Vulnérabilité identifiée** : le modèle peut produire des prédictions peu fiables sur des situations très différentes de celles observées pendant l'entraînement.
- **Garde-fou envisagé** : contrôler les bornes des variables d'entrée et signaler les données hors distribution.

## Ce que je veux apporter à la grille collective

> 1-2 contributions ou questions à pousser pendant la restitution.

- La performance seule ne suffit pas : intégrer systématiquement explicabilité, latence et robustesse dans le choix final.
- Définir les critères de décision en fonction du contexte métier plutôt que désigner un modèle comme systématiquement meilleur.

---

*Carte personnelle à compléter avant la restitution collective mercredi 11h30.*
