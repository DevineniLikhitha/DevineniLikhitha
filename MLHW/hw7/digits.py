from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn.metrics as metrics
from sklearn.svm import SVC
import pandas as pd

digits = load_digits()
X= digits.data
Y=digits.target

#Handling missing values
X = pd.DataFrame(data=digits.data, columns=digits.feature_names)
y=pd.DataFrame(Y)

print(X.isnull().sum())
print(y.isnull().sum())



X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=3,stratify=y)

#standardise the data
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
'''Decision tree'''

tree = DecisionTreeClassifier(criterion='entropy', max_depth=None,random_state=1)
tree.fit(X_train_std,y_train)
y_pred1 = tree.predict(X_train_std)
y_pred = tree.predict(X_test_std)
     
print('Accuracy sore for testing data decision tree ',metrics.accuracy_score(y_test, y_pred))

print('Accuracy sore for training decision tree',metrics.accuracy_score(y_train, y_pred1))

'''SVM'''

model = SVC(kernel='linear', C=1E10)
model.fit(X_train_std,y_train)
y_pred1_svm = model.predict(X_train_std)
y_pred_svm = model.predict(X_test_std)

print('Accuracy sore for testing data SVM ',metrics.accuracy_score(y_test, y_pred_svm))

print('Accuracy sore for training SVM',metrics.accuracy_score(y_train, y_pred1_svm))

'''Bagging classifier  tree'''
bag = BaggingClassifier(base_estimator=SVC(),n_estimators=300, max_samples=1.0, max_features=1.0, n_jobs=1, random_state=0)

bag.fit(X_train_std,y_train)
y_pred_bag = bag.predict(X_train_std)
y_pred_tbag = bag.predict(X_test_std)

     
print('Accuracy sore for testing data bagging classifier ',metrics.accuracy_score(y_test, y_pred_tbag))

print('Accuracy sore for training data bagging classifier',metrics.accuracy_score(y_train, y_pred_bag))



'''Random'''


clf=RandomForestClassifier(n_estimators=300,criterion='entropy', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features='auto')


clf.fit(X_train_std,y_train)
y_pred_clf = clf.predict(X_train_std)
y_pred_tclf = clf.predict(X_test_std)

     
print('Accuracy sore for testing data random ',metrics.accuracy_score(y_test, y_pred_tclf))

print('Accuracy sore for training data random tree',metrics.accuracy_score(y_train, y_pred_clf))

ada = AdaBoostClassifier(base_estimator=tree,n_estimators=300, learning_rate=0.001,random_state=1)

'''ADA boost'''

ada.fit(X_train_std,y_train)
y_pred_ada = ada.predict(X_train_std)
y_pred_tada = ada.predict(X_test_std)

     
print('Accuracy sore for testing data ADA',metrics.accuracy_score(y_test, y_pred_tada))

print('Accuracy sore for training ADA',metrics.accuracy_score(y_train, y_pred_ada))

