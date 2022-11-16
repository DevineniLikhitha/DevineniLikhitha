from sklearn.datasets import load_wine
from sklearn.datasets import make_moons
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier as Dtree
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



#tree
tree_model = Dtree(criterion='gini',max_depth=3,random_state=1, max_features=None)

'''PCA'''
pca = PCA(n_components = 3)
#train 
X_train_pca = pca.fit_transform(X_train_std)
#fitting into decision tree
tree_model.fit(X_train_pca,y_train)
#test
X_test_pca = pca.transform(X_test_std)
y_pred = tree_model.predict(X_test_pca)

#Accuracy
acc = accuracy_score(y_pred,y_test)
print("Decision Tree+ PCA Accuracy",acc)

'''LDA'''


tree_model = Dtree(criterion='gini',max_depth=4,random_state=1,min_samples_split=2, min_weight_fraction_leaf=0.0)
lda = LDA(n_components=2)
X_train_lda = lda.fit_transform(X_train_std,y_train)
tree_model.fit(X_train_lda,y_train)

X_test_lda = lda.transform(X_test_std)
y_pred_lda = tree_model.predict(X_test_lda)
acc_lda = accuracy_score(y_pred_lda,y_test)
print("Decision Tree+ LDA accuracy",acc_lda)


'''KCPA'''

X,y = make_moons(n_samples=100,noise=0.1)
tree_model2 = Dtree(criterion='entropy',max_depth=6,random_state=1)

#train and test split
train_X, test_X, train_y, test_y = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)

kpca = KPCA(n_components =4, kernel='rbf',gamma=15)
X_train_kpca = kpca.fit(train_X)
X_test_kcpa = kpca.transform(test_X)

tree_model2.fit(train_X,train_y)
y_pred_kpca = tree_model2.predict(test_X)
acc_kpca = accuracy_score(y_pred_kpca,test_y)
print("Decision tree + KPCA accuracy",acc_kpca)


