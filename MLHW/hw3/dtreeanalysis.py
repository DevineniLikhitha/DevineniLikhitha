
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


class decisontree:
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    


    
    tree_model = DecisionTreeClassifier(criterion='gini', 
                                        max_depth=4, 
                                        random_state=1)
    
    tree_model.fit(X_train,y_train)
    
    pred_y=tree_model.predict(X_test)
    
    accuracy = metrics.accuracy_score(y_test,pred_y)
    print("Accuracy :",accuracy)
    
    
    c_m = confusion_matrix(y_test, pred_y)
    print(f"confusion matrix:\n{c_m}") 
    
    #classification report
    
    print(classification_report(y_test,pred_y))
    

print("--- %s seconds ---" % (time.time() - start_time))
