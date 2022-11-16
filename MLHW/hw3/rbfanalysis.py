from sklearn import datasets
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
import matplotlib.pyplot as plt
import matplotlib
import sklearn.metrics as metrics
import random
import time
start_time = time.time()


class rbfkernel:
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
 

    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))


    svm = SVC(kernel='rbf', random_state=1, gamma=0.2, C=1.0)
    svm.fit(X_train_std, y_train)
    
    score = svm.score(X_train,y_train)
    print('Accuracy score',score)
    
    #cross_val_score
    
    c_v_score = cross_val_score(svm,X_train,y_train, cv=10)
    print("CV score: %.2f" % c_v_score.mean())
    
    y_pred= svm.predict(X_test)
    
    #confusion matrix
    
    c_m = confusion_matrix(y_test, y_pred)
    print(c_m)
    
    #classification report
    
    print(classification_report(y_test,y_pred))
    

print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
