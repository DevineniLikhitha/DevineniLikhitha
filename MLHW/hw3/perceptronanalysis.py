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



class perceptron:
    #loading iris dataset
    
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    print('Class labels:', np.unique(y))
    
    # Splitting data into 70% training and 30% test data:
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    
        
    # ## Training a perceptron via scikit-learn
    
    
    ppn = Perceptron(max_iter=10,eta0=0.1, random_state=1)
    ppn.fit(X_train, y_train)
    
    y_pred = ppn.predict(X_test)
    print('Misclassified examples: %d' % (y_test != y_pred).sum())
    
    
    accuracy = metrics.accuracy_score(y_test,y_pred)
    print('Accuracy for digits',accuracy)



print("--- %s seconds ---" % (time.time() - start_time))