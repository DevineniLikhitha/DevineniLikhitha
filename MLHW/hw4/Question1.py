from sklearn.datasets import load_wine
from sklearn.datasets import make_moons
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import KernelPCA as KPCA

wine = load_wine()
X = wine.data[:,0:13]
y = wine.target



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
print(X_pca.shape)

#LDA


lda = LDA(n_components = 2)
lda.fit(X_train_std,y_train)
X_lda = lda.transform(X_train_std)
print(X_lda.shape)


#KPCA
X,y = make_moons(n_samples=100,noise=0.1)


#train and test split
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)




kpca = KPCA(n_components =2, kernel='rbf',gamma=15)
X_train_kpca = kpca.fit_transform(X_train)
print(X_train_kpca.shape)