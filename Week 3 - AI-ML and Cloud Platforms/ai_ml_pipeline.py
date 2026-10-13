"""A reproducible, local ML pipeline: sample data -> split -> train -> evaluate."""

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def main() -> None:
    X, y = make_regression(
        n_samples=300, n_features=3, noise=12.0, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Train rows:", len(X_train))
    print("Test rows:", len(X_test))
    print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, predictions)):.2f}")
    print(f"R²: {r2_score(y_test, predictions):.3f}")
    print("Learned coefficients:", model.coef_)
    print("Intercept:", round(float(model.intercept_), 3))


if __name__ == "__main__":
    main()
