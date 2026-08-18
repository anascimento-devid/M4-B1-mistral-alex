"""M4-B1 — Preprocessing Bike Sharing.

Tu décides :
- Quelles features tu gardes (attention aux fuites — `casual_riders` et
  `registered_riders` sont des composantes de la cible)
- Comment tu encodes `season` (OneHot ou ordinal cyclique)
- Comment tu encodes `hour`/`month` (laisser numérique ou cyclique sin/cos ?)
- Si tu fais du feature scaling (pas obligatoire pour arbres/boosting)
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# TODO — Sélectionne tes features (exclure les fuites !)

FEATURES: list[str] = [
    "season",
    "year",
    "month",
    "hour",
    "is_holiday",
    "weekday",
    "is_working_day",
    "weather",
    "temperature_norm",
    "temperature_feels_norm",
    "humidity_norm",
    "windspeed_norm",
]

TARGET: str = "total_rentals"

CATEGORICAL_FEATURES = [
    "season",
    "weather",
    "weekday",
]

NUMERIC_FEATURES = [
    "year",
    "month",
    "hour",
    "is_holiday",
    "is_working_day",
    "temperature_norm",
    "temperature_feels_norm",
    "humidity_norm",
    "windspeed_norm",
]


def build_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES,
            ),
            (
                "num",
                StandardScaler(),
                NUMERIC_FEATURES,
            ),
        ]
    )


def load_dataset(path: Path) -> tuple[pd.DataFrame, pd.Series]:
    """Charge le CSV Bike Sharing, retourne (X, y).

    Args:
        path: Chemin du CSV.

    Returns:
        (X, y) avec X = features sélectionnées, y = total_rentals.
    """
    df = pd.read_csv(path)
    missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
    if missing:
        raise KeyError(f"Colonnes attendues absentes : {missing}")
    y = df[TARGET]
    X = df[FEATURES].copy()
    return X, y


def add_cyclic_features(X: pd.DataFrame) -> pd.DataFrame:
    """Optionnel — encodage cyclique sin/cos pour hour et month.

    Capter la saisonnalité circulaire (heure 23 proche de l'heure 0).
    À utiliser pour la régression linéaire ; les arbres n'en ont pas besoin.

    Args:
        X: DataFrame avec colonnes `hour` et `month`.

    Returns:
        DataFrame avec colonnes `hour_sin`, `hour_cos`, `month_sin`, `month_cos`.
    """
    X = X.copy()
    if "hour" in X.columns:
        X["hour_sin"] = np.sin(2 * np.pi * X["hour"] / 24)
        X["hour_cos"] = np.cos(2 * np.pi * X["hour"] / 24)
    if "month" in X.columns:
        X["month_sin"] = np.sin(2 * np.pi * X["month"] / 12)
        X["month_cos"] = np.cos(2 * np.pi * X["month"] / 12)
    return X
