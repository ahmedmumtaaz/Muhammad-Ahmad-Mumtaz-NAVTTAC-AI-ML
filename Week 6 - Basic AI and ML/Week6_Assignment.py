# Week 6: Supervised Machine Learning
# Topics: Regression, classification, KNN, Decision Tree, Random Forest, SVM, evaluation metrics
import pandas as pd
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# PART 1: Regression
Xr, yr = make_regression(n_samples=300, n_features=4, noise=15, random_state=42)
Xr_train, Xr_test, yr_train, yr_test = train_test_split(Xr, yr, test_size=.25, random_state=42)
reg = LinearRegression().fit(Xr_train, yr_train)
reg_pred = reg.predict(Xr_test)
print("Regression MSE:", mean_squared_error(yr_test, reg_pred))
print("Regression R2:", r2_score(yr_test, reg_pred))

# PART 2: Classification model comparison
X, y = make_classification(n_samples=700, n_features=12, n_informative=7, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, stratify=y, random_state=42)
models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier(5)),
    "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=150, random_state=42),
    "SVM": make_pipeline(StandardScaler(), SVC())
}
scores = []
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    scores.append({"model":name, "accuracy":accuracy_score(y_test,pred),
                  "precision":precision_score(y_test,pred), "recall":recall_score(y_test,pred),
                  "f1":f1_score(y_test,pred)})
print(pd.DataFrame(scores).sort_values("f1",ascending=False).round(3))
# TODO: print the confusion matrix for your chosen model and explain false positives/negatives.
# QUESTIONS: 1) When is recall more useful than precision? 2) What is overfitting?
# 3) Explain bias-variance tradeoff. 4) Why do we split data into train/test?