from sklearn import datasets
import pandas as pd
import numpy as np
from random import sample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier as Dtree
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import KernelPCA as KPCA
import time

start_time = time.time()
class PCA:
    iris = datasets.load_iris()
    X = iris.data[:, :2]  
    y = iris.target
    
    #train and test split
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=1, stratify=y)
    
    #standardisation
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    
    tree_model = Dtree(criterion='gini',max_depth=4,random_state=1, max_features=None)
    
    '''PCA'''
    pca = PCA(n_components = 2)
    #train 
    X_train_pca = pca.fit_transform(X_train_std)
    #fitting into decision tree
    tree_model.fit(X_train_pca,y_train)
    #test
    X_test_pca = pca.transform(X_test_std)
    y_pred_pca = tree_model.predict(X_test_pca)
    #shape
    print("PCA-iris",X_train_pca.shape)
    
    #Accuracy
    acc = accuracy_score(y_pred_pca,y_test)
    print("PCA Accuracy",acc)
    #classification report
    print(classification_report(y_test,y_pred_pca))
    #precision
    print('Precision-pca: %.3f' % precision_score(y_test, y_pred_pca,average='macro'))
    #f1 score
    print('F1 Score-pca: %.3f' % f1_score(y_test, y_pred_pca,average='macro'))
    #recall
    print('Recall-pca: %.3f' % recall_score(y_test, y_pred_pca,average='macro'))
    #running time
print("--- %s seconds for PCA ---" % (time.time() - start_time))

#LDA
start_time = time.time()
class LDA:
    iris = datasets.load_iris()
    X = iris.data[:, :2]  
    y = iris.target
    
    #train and test split
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=1, stratify=y)
    
    #standardisation
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    
    tree_model = Dtree(criterion='gini',max_depth=4,random_state=1, max_features=None)
    lda = LDA(n_components=2)
    X_train_lda = lda.fit_transform(X_train_std,y_train)
    tree_model.fit(X_train_lda,y_train)
    X_test_lda = lda.transform(X_test_std)
    y_pred_lda = tree_model.predict(X_test_lda)
    
    #Accuracy
    acc_lda = accuracy_score(y_pred_lda,y_test)
    print("LDA accuracy",acc_lda)
    #classification report
    print(classification_report(y_test,y_pred_lda))
    #precision
    print('Precision-lda: %.3f' % precision_score(y_test, y_pred_lda,average='macro'))
    #f1 score
    print('F1 Score-lda: %.3f' % f1_score(y_test, y_pred_lda,average='macro'))
    #recall
    print('Recall-lda: %.3f' % recall_score(y_test, y_pred_lda,average='macro'))
    #running time
print("--- %s seconds for lda ---" % (time.time() - start_time))


#KCPA
start_time = time.time()
class KPCA:
    iris = datasets.load_iris()
    X = iris.data[:, :2]  
    y = iris.target
    
    #train and test split
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=1, stratify=y)
    
    #standardisation
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    
    tree_model = Dtree(criterion='gini',max_depth=4,random_state=1, max_features=None)
    

    kpca = KPCA(n_components =2, kernel='rbf',gamma=15)
    X_train_kpca = kpca.fit_transform(X_train)
    tree_model.fit(X_train_kpca,y_train)
    X_test_kpca = kpca.transform(X_test_std)
    y_pred_kpca = tree_model.predict(X_test_kpca)
    #Accuracy
    acc_kpca = accuracy_score(y_pred_kpca,y_test)
    print("KPCA accuracy",acc_kpca)
    #classification report
    print(classification_report(y_test,y_pred_kpca))
    #precision
    print('Precision-kpca: %.3f' % precision_score(y_test, y_pred_kpca,average='macro'))
    #f1 score
    print('F1 Score-kpca: %.3f' % f1_score(y_test, y_pred_kpca,average='macro'))
    #recall
    print('Recall-kpca: %.3f' % recall_score(y_test, y_pred_kpca,average='macro'))
#running time
print("--- %s seconds for kpca ---" % (time.time() - start_time))

