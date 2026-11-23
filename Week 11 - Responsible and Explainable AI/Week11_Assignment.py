# Week 11: Fairness, bias and explainability (synthetic demonstration)
import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import accuracy_score,precision_score,recall_score
rng=np.random.default_rng(7); n=1200
group=rng.integers(0,2,n); f1=rng.normal(group*.35,1,n); f2=rng.normal(size=n)
p=1/(1+np.exp(-(-.2+f1+.6*f2-group*.25))); target=rng.binomial(1,p)
df=pd.DataFrame({"group":group,"feature1":f1,"feature2":f2,"target":target})
model=RandomForestClassifier(n_estimators=120,random_state=7).fit(df[["feature1","feature2"]],target)
df["pred"]=model.predict(df[["feature1","feature2"]])
for g,part in df.groupby("group"):
    print("Group",g,"n",len(part),"positive rate",round(part.pred.mean(),3),
          "accuracy",round(accuracy_score(part.target,part.pred),3),
          "precision",round(precision_score(part.target,part.pred,zero_division=0),3),
          "recall",round(recall_score(part.target,part.pred,zero_division=0),3))
imp=permutation_importance(model,df[["feature1","feature2"]],target,n_repeats=10,random_state=7)
print("Permutation importance:",dict(zip(["feature1","feature2"],imp.importances_mean.round(3))))
# Explain SHAP (Shapley-based attribution), LIME (local surrogate), What-If Tool (interactive scenario testing).
# Discuss fairness metrics, privacy, representative data, documentation, human review and appeals.
# Synthetic exercise only; subgroup metrics are indicators, not proof of fairness or causality.