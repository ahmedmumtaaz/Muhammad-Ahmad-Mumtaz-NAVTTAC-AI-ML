# Week 7: Neural Networks and Advanced AI/ML concepts
# Runnable MLP experiments; conceptual CNN/RNN/Transformer and transfer-learning reflection
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
X,y=make_classification(n_samples=900,n_features=20,n_informative=10,n_redundant=5,random_state=21)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,stratify=y,random_state=21)
for name,hidden in [("Shallow",(32,)),("Deep",(64,32,16))]:
    m=make_pipeline(StandardScaler(),MLPClassifier(hidden_layer_sizes=hidden,alpha=.001,max_iter=500,early_stopping=True,random_state=21))
    m.fit(X_train,y_train)
    print(name,"Accuracy:",round(accuracy_score(y_test,m.predict(X_test)),3),"iterations:",m[-1].n_iter_)
# Try regularization strengths: alpha controls L2 penalty.
for alpha in [.0001,.001,.01,.1]:
    m=make_pipeline(StandardScaler(),MLPClassifier(hidden_layer_sizes=(64,32),alpha=alpha,max_iter=500,early_stopping=True,random_state=21))
    m.fit(X_train,y_train)
    print("alpha",alpha,"accuracy",round(accuracy_score(y_test,m.predict(X_test)),3))
# Written reflection:
# CNN: images/spatial patterns; RNN: sequential data; Transformer: self-attention and contextual sequences.
# Transfer learning: start from pretrained weights, train a task head, optionally unfreeze selected layers.
# Explain GPU/TPU usefulness, batch-size vs memory, dropout, regularization, learning rate, and validation.