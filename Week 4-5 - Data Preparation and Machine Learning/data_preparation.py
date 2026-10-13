"""Demonstrates a safe preprocessing pipeline on a small synthetic dataset."""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    df = pd.DataFrame({
        "age": [21, 25, None, 35, 29, 42, 31, 25],
        "monthly_spend": [1200, 1800, 900, None, 2100, 2500, 1700, 1800],
        "city": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi", None, "Lahore", "Karachi"],
        "renewed": [0, 1, 0, 1, 1, 1, 0, 1],
    })
    print("Raw data:\n", df)
    print("\nMissing values:\n", df.isna().sum())
    print("Duplicate rows:", int(df.duplicated().sum()))
    df = df.drop_duplicates()

    X = df.drop(columns="renewed")
    y = df["renewed"]
    numeric_features = ["age", "monthly_spend"]
    categorical_features = ["city"]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    X_train_ready = preprocessor.fit_transform(X_train)
    X_test_ready = preprocessor.transform(X_test)
    print("\nTransformed training shape:", X_train_ready.shape)
    print("Transformed test shape:", X_test_ready.shape)
    print("Training labels:", y_train.tolist())
    print("Test labels:", y_test.tolist())
    print("\nImportant: fit preprocessing on training data only to avoid leakage.")


if __name__ == "__main__":
    main()
