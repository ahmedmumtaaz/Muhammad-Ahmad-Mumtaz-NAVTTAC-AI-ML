# Week 10: model optimization, performance, drift check, deployment design
import time, numpy as np, pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
digits=load_digits(); X,y=digits.data,digits.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
for name,trees,depth in [("Baseline",200,None),("Compact",40,8)]:
    m=RandomForestClassifier(n_estimators=trees,max_depth=depth,random_state=42,n_jobs=-1)
    start=time.perf_counter(); m.fit(X_train,y_train); train_time=time.perf_counter()-start
    start=time.perf_counter(); p=m.predict(X_test); predict_time=time.perf_counter()-start
    print(name,"accuracy",round(accuracy_score(y_test,p),3),"train sec",round(train_time,3),"predict sec",round(predict_time,3))
# Simple drift proxy: shifts the first feature in simulated new data.
shifted=X_test.copy(); shifted[:,0]+=2
delta=np.abs(X_train.mean(axis=0)-shifted.mean(axis=0))
print("Features with mean shift > 1:",int((delta>1).sum()))
# Explain pruning, quantization, distillation; TensorRT accelerates optimized GPU inference.
# Deployment outline: API, validation, logging, monitoring, model registry, retraining, rollback.
# NOTE: this is a simple drift illustration, not a production monitoring solution.