# Week 9: Reproducible pipeline, saving, versioning and automation concepts
import os, json
from joblib import dump, load
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
data=load_breast_cancer(as_frame=True); X,y=data.data,data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
pipe=Pipeline([("scaler",StandardScaler()),("model",LogisticRegression(max_iter=2000))])
pipe.fit(X_train,y_train); pred=pipe.predict(X_test)
metrics={"accuracy":float(accuracy_score(y_test,pred)),"f1":float(f1_score(y_test,pred))}
print("Metrics:",metrics)
os.makedirs("artifacts",exist_ok=True)
dump(pipe,"artifacts/week9_pipeline.joblib")
loaded=load("artifacts/week9_pipeline.joblib")
print("Loaded model sample predictions:",loaded.predict(X_test.iloc[:5]).tolist())
with open("artifacts/week9_metrics.json","w") as f: json.dump(metrics,f,indent=2)
# MLOps plan: version data and model, test code, schema-check, train, evaluate against threshold,
# save artifact, approval gate, deploy, monitor, rollback. Discuss Kubeflow/Cloud Composer.