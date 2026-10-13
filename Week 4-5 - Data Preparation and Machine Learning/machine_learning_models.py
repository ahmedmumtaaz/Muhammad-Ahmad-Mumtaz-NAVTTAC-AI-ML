"""Introductory regression and classification examples using scikit-learn."""

from sklearn.datasets import make_regression, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
)
import numpy as np


def regression_example() -> None:
    X, y = make_regression(n_samples=250, n_features=2, noise=15, random_state=7)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=7
    )
    model = LinearRegression().fit(X_train, y_train)
    pred = model.predict(X_test)
    print("\n=== Linear regression ===")
    print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, pred)):.2f}")
    print(f"R²: {r2_score(y_test, pred):.3f}")


def classification_example() -> None:
    X, y = make_classification(
        n_samples=300, n_features=6, n_informative=4, n_redundant=0,
        random_state=17
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=17, stratify=y
    )
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    pred = model.predict(X_test)
    print("\n=== Logistic classification ===")
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print(f"Precision: {precision_score(y_test, pred, zero_division=0):.3f}")
    print(f"Recall: {recall_score(y_test, pred, zero_division=0):.3f}")
    print(f"F1: {f1_score(y_test, pred, zero_division=0):.3f}")
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))


if __name__ == "__main__":
    regression_example()
    classification_example()
