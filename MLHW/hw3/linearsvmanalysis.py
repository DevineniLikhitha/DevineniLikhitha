
from sklearn import datasets
from sklearn.datasets import load_digits
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
from sklearn.metrics import classification_report
from sklearn.datasets import make_classification
from sklearn import svm
from sklearn.svm import SVC
from distutils.version import LooseVersion
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import matplotlib
import random
import pandas as pd
import time

start_time = time.time()
class linearSVC:
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    print('Class labels:', np.unique(y))
    
    # Splitting data into 70% training and 30% test data:
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    #Train the model
    lsvm = svm.SVC(kernel='linear')
    
    lsvm.fit(X_train,y_train)
    score = lsvm.score(X_train,y_train)
    print('Accuracy score',score)
    
    #cross_val_score
    
    c_v_score = cross_val_score(lsvm,X_train,y_train, cv=10)
    print("CV score: %.2f" % c_v_score.mean())
    
    y_pred= lsvm.predict(X_test)
    
    #confusion matrix
    
    c_m = confusion_matrix(y_test, y_pred)
    print(c_m)
    
    #classification report
    
    print(classification_report(y_test,y_pred))
    
    

print("--- %s seconds ---" % (time.time() - start_time))