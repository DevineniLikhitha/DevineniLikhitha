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
from sklearn import tree



class perceptron:
    digits =load_digits()
    #creating features
    X = digits.data
    #creating target
    y=digits.target
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    ppn = Perceptron(max_iter=10,eta0=0.0001, random_state=1)
    ppn.fit(X_train_std, y_train)
    
    y_pred = ppn.predict(X_test)
    print('Misclassified examples -digits: %d' % (y_test != y_pred).sum())
    
    
    
    accuracy = metrics.accuracy_score(y_test,y_pred)
    print('Accuracy for digits',accuracy)
    
    
    
    #predictions
    
    sample = random.sample(range(len(X_train)),10)
    for i in sample:
        print(i,ppn.predict([X_train[i]]))
        
    #classification report for training data
    
    print(classification_report(ppn.predict(X_train),y_train))
    
    #classificaton report for rest data
    
    
class perceptron2:
    data=pd.read_csv('mobileprice.csv')
    y=data['price_range']
    X=data.drop('price_range',axis=1)
    
   
    
    # Splitting data into 70% training and 30% test data:
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    ppn = Perceptron(max_iter=10,eta0=0.0001, random_state=1)
    ppn.fit(X_train_std, y_train)
    
    y_pred = ppn.predict(X_test)
    print('Misclassified examples-mobile price(perceptron): %d' % (y_test != y_pred).sum())
    
    
    
    accuracy = metrics.accuracy_score(y_test,y_pred)
    print('Accuracy for mobile price classification(perceptron) ',accuracy)
    
    
class linearSVM1:
    digits =load_digits()
    #creating features
    X = digits.data
    #creating target
    y=digits.target
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    lsvm = svm.SVC(kernel='linear')
    
    lsvm.fit(X_train,y_train)
    score = lsvm.score(X_train_std,y_train)
    print('Accuracy score for svm-digits ',score)
    
    #cross_val_score
    
    c_v_score = cross_val_score(lsvm,X_train,y_train, cv=10)
    print("CV score-svm-digits: %.2f" % c_v_score.mean())
    
    y_pred= lsvm.predict(X_test)
    
    #confusion matrix
    
    c_m = confusion_matrix(y_test, y_pred)
    print(f"confusion matrix-linearsvm-digits:\n{c_m}")
    
    #classification report
    
    print(classification_report(y_test,y_pred))
   

 
class linearSVM:
     data=pd.read_csv('mobileprice.csv')
     y=data['price_range']
     X=data.drop('price_range',axis=1)
     
     print('Class labels:', np.unique(y))
     
     # Splitting data into 70% training and 30% test data:
     
     
     
     
     X_train, X_test, y_train, y_test = train_test_split(
         X, y, test_size=0.2, random_state=1, stratify=y)
     
     
     sc = StandardScaler()
     sc.fit(X_train)
     X_train_std = sc.transform(X_train)
     X_test_std = sc.transform(X_test)
     
     #Train the model
     lsvm = svm.SVC(kernel='linear')
     
     lsvm.fit(X_train_std,y_train)
     score = lsvm.score(X_train,y_train)
     print('Accuracy score for svm-mobileprice ',score)
     
     #cross_val_score
     
     c_v_score = cross_val_score(lsvm,X_train,y_train, cv=10)
     print("CV score-linearsvm-mobileprice: %.2f" % c_v_score.mean())
     
     y_pred= lsvm.predict(X_test)
     
     #confusion matrix
     
     c_m = confusion_matrix(y_test, y_pred)
     print(f"confusion matrix-linearsvm-mobileprice-:\n{c_m}")
     
     #classification report
     
     print(classification_report(y_test,y_pred))
     


class rbfkerneldigits:
    digits =load_digits()
    #creating features
    X = digits.data
    #creating target
    y=digits.target
    
    
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
    print('Accuracy score-kernelrbf-digits',score)
    
    #cross_val_score
    
    c_v_score = cross_val_score(svm,X_train,y_train, cv=10)
    print("CV score-kernelrbf-digits: %.2f" % c_v_score.mean())
    
    y_pred= svm.predict(X_test)
    
    #confusion matrix
    
    c_m = confusion_matrix(y_test, y_pred)
    print(f"confusion matrix-kernelrbf-digits-:\n{c_m}") 
    
    #classification report
    
    print(classification_report(y_test,y_pred))
    
class kernelrbfmobileprice:
    data=pd.read_csv('mobileprice.csv')
    y=data['price_range']
    X=data.drop('price_range',axis=1)
     
    
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
    print('Accuracy score-kernelrbf-mobileprice',score)
    
    #cross_val_score
    
    c_v_score = cross_val_score(svm,X_train,y_train, cv=10)
    print("CV score-kernelrbf-mobileprice: %.2f" % c_v_score.mean())
    
    y_pred= svm.predict(X_test)
    
    #confusion matrix
    
    c_m = confusion_matrix(y_test, y_pred)
    print(f"confusion matrix-kernelrbf-mobileprice-:\n{c_m}") 
    
    #classification report
    
    print(classification_report(y_test,y_pred))
    
    
class decisiontreedigits:
    digits =load_digits()
    #creating features
    X = digits.data
    #creating target
    y=digits.target
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    
    tree_model = DecisionTreeClassifier(criterion='gini', 
                                        max_depth=4, 
                                        random_state=1)
    
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    tree_model.fit(X_train_std,y_train)
    
    pred_y=tree_model.predict(X_test)
    
    accuracy = metrics.accuracy_score(y_test,pred_y)
    print("Accuracy for digits-Dtree:",accuracy)
    
    
    c_m = confusion_matrix(y_test, pred_y)
    print(f"confusion matrix-dtree-digits-:\n{c_m}") 
    
    #classification report
    
    print(classification_report(y_test,pred_y))
    
    tree.plot_tree(tree_model)

    plt.show()
    
    
class decisiontreemobileprice:
    data=pd.read_csv('mobileprice.csv')
    y=data['price_range']
    X=data.drop('price_range',axis=1)
     
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    
    tree_model = DecisionTreeClassifier(criterion='gini', 
                                        max_depth=4, 
                                        random_state=1)
    
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    tree_model.fit(X_train_std,y_train)
    
    pred_y=tree_model.predict(X_test)
    
    accuracy = metrics.accuracy_score(y_test,pred_y)
    print("Accuracy for mobileprice-Dtree:",accuracy)
    
    
    c_m = confusion_matrix(y_test, pred_y)
    print(f"confusion matrix-dtree-mobileprice-:\n{c_m}") 
    
    #classification report
    
    print(classification_report(y_test,pred_y))
    
    tree.plot_tree(tree_model)

    plt.show()
    
    

    
    
    
    
    