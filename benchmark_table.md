# Tableau comparatif — Benchmark Mistral Assurances

> Document à remettre à **Inès Tabet** (responsable actuariat). Doit être
> lisible par un actuaire, pas par un data scientist.
> Auteur : `<prénom>` — Date : `<date>`

## Méthodologie

- **Split** : `<TimeSeriesSplit n_splits=5>` *(ou KFold n_splits=5, justifié dans le notebook)*
- **Métriques** : MAE, RMSE, R² (moyennes sur N folds)
- **Mêmes folds, mêmes features** pour tous les modèles (règle d'or *comparabilité*)
- **Hyperparamètres** : par défaut + 1 variante raisonnable par famille
- **Référence** : baseline `mistral-tarif-v1` (LinearRegression 2024)

## Tableau (à compléter)

| Modèle                          |       MAE |      RMSE |        R² | Temps train (s) | Latence inférence (ms/1k) | Explicabilité (1-3)        | Mémoire (Mo) |
| ------------------------------- | --------: | --------: | --------: | --------------: | ------------------------: | -------------------------- | -----------: |
| **mistral-tarif-v1** (baseline) |     105.0 |     139.4 |      0.39 |            ~0.1 |                        ~1 | 3 (très explicable)        |         ~0.5 |
| **Ridge**                       |    115.01 |    153.54 |     0.264 |          0.0076 |                      2.42 | 3 (très explicable)        |    à mesurer |
| **RandomForest**                |     52.86 |     79.38 |     0.780 |          0.3566 |                     31.65 | 2 (moyennement explicable) |    à mesurer |
| **HistGradientBoosting**        | **49.84** | **74.03** | **0.805** |          0.1758 |                      3.59 | 1 (peu explicable)         |    à mesurer |


## Interprétation pour Inès

> HistGradientBoosting est le modèle le plus performant. Il présente l'erreur moyenne la plus faible (MAE = 49.84) et le meilleur R² (0.805), ce qui indique qu'il explique bien la variance des données. 
> A l'inverse, Ridge est le moins performant avec un MAE de 115.01 et un R² de 0.264, ce qui suggère qu'il n'est pas adapté à ce problème.
> RandomForest se situe entre les deux, offrant de bonnes performances mais avec un temps d'inférence plus élevé (31.65 ms/1k) par rapport à HistGradientBoosting (3.59 ms/1k).

> HistGradientBoosting offre le meilleur compromis entre précision et rapidité. En revanche, son fonctionnement est moins directement lisible qu’un modèle linéaire : il est plus difficile d’attribuer la prédiction finale à l’effet isolé d’une variable donnée. Des outils d’explicabilité peuvent néanmoins permettre d’identifier les facteurs qui contribuent le plus aux estimations.

## Recommandation

Voir `verdict.md` (5 lignes max).

---

*Document remis à Inès Tabet — `<date>`.*
