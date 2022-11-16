import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
import sklearn.metrics as metrics
from sklearn.svm import SVC

data=pd.read_csv('man_masses.txt',header=None,sep=",",na_values='?')
data.columns=["BI_RADS","age","shape","margin","denisty","severity"]
print(data.isnull().values.any())
#handling missing values
#checking for null values and calculating no.of null values that existed in a columns
print(data.isnull().sum())
data.fillna(data.mean())

#relacing ? with np.nan
df = data.replace("?", np.nan) 

#dropping the rows that have null values
df = data.dropna() 
print(df)
#checking for null values in the new data frame
print(df.isnull().sum())

# taking X and y
X=df[['BI_RADS','age','shape','margin','denisty']]
y=df[['severity']]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=3,stratify=y)

#standardise the data
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

'''Decision Tree'''
tree = DecisionTreeClassifier(criterion='entropy', max_depth=None,random_state=1)
tree.fit(X_train_std,y_train)
y_pred1 = tree.predict(X_train_std)
y_pred = tree.predict(X_test_std)
     
print('Accuracy sore for testing data decision tree ',metrics.accuracy_score(y_test, y_pred))

print('Accuracy sore for training decision tree',metrics.accuracy_score(y_train, y_pred1))


'''SVM'''
model = SVC(kernel='rbf', C=0.01, random_state=1)
model.fit(X_train_std,y_train)
y_pred1_svm = model.predict(X_train_std)
y_pred_svm = model.predict(X_test_std)

print('Accuracy sore for testing data SVM ',metrics.accuracy_score(y_test, y_pred_svm))

print('Accuracy sore for training SVM',metrics.accuracy_score(y_train, y_pred1_svm))

'''Bagging classifier'''
bag = BaggingClassifier(base_estimator=SVC(),n_estimators=500, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=False, n_jobs=1, random_state=0)

bag.fit(X_train_std,y_train)
y_pred_bag = bag.predict(X_train_std)
y_pred_tbag = bag.predict(X_test_std)

     
print('Accuracy sore for testing data bagging classifier ',metrics.accuracy_score(y_test, y_pred_tbag))

print('Accuracy sore for training data bagging classifier',metrics.accuracy_score(y_train, y_pred_bag))

'''Random forest'''
clf=RandomForestClassifier(n_estimators=300,criterion='entropy', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None)


clf.fit(X_train_std,y_train)
y_pred_clf = clf.predict(X_train_std)
y_pred_tclf = clf.predict(X_test_std)

     
print('Accuracy sore for testing data random ',metrics.accuracy_score(y_test, y_pred_tclf))

print('Accuracy sore for training data random tree',metrics.accuracy_score(y_train, y_pred_clf))

ada = AdaBoostClassifier(base_estimator=tree,n_estimators=100, learning_rate=0.1,random_state=1)

'''ADABoost'''
ada.fit(X_train_std,y_train)
y_pred_ada = ada.predict(X_train_std)
y_pred_tada = ada.predict(X_test_std)

     
print('Accuracy sore for testing data ADA',metrics.accuracy_score(y_test, y_pred_tada))

print('Accuracy sore for training ADA',metrics.accuracy_score(y_train, y_pred_ada))
