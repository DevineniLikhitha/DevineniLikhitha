from sklearn import datasets
from sklearn.datasets import fetch_openml
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
from random import sample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import KernelPCA as KPCA

class iris:
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



    
    #PCA

    pca = PCA(n_components = 2)
    pca.fit(X_train_std)
    X_pca = pca.transform(X_train_std)
    print("PCA-iris",X_pca.shape)

    #LDA


    lda = LDA(n_components = 2)
    lda.fit(X_train_std,y_train)
    X_lda = lda.transform(X_train_std)
    print("LDA-iris",X_lda.shape)
    
    #KCPA
    
    kpca = KPCA(n_components =2, kernel='rbf',gamma=15)
    X_train_kpca = kpca.fit_transform(X_train)
    print("KPCA-iris",X_train_kpca.shape)
    

class digits:
    mist = fetch_openml('mnist_784', version=1)
    #print(mist.data.shape)
    
    
   

    X= mist.data
    y=mist.target
    

    
    X, y = make_blobs(n_samples=1500)
    
  

    
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=1, stratify=y)
    
    #standardisation
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)


    
    #PCA

    pca = PCA(n_components = 2)
    pca.fit(X_train_std)
    X_pca = pca.transform(X_train_std)
    print("PCA-Minist",X_pca.shape)
    
    lda = LDA(n_components = 2)
    lda.fit(X_train_std,y_train)
    X_lda = lda.transform(X_train_std)
    print("LDA-Minst",X_lda.shape)
    
    #KCPA
    
    kpca = KPCA(n_components =2, kernel='rbf',gamma=15)
    X_train_kpca = kpca.fit_transform(X_train)
    print("KCPA-Minst",X_train_kpca.shape)
    