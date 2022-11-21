import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import metrics

data = pd.read_csv('clean_invehicle_dataset2.csv')
# Assign values to the X and y variables:
y = data['Y']
X = data.iloc[:,:-1]
# Split dataset into random train and test subsets:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20) 
r = np.corrcoef(data['age'],data['Y'])

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
cols = ['age', 'gender', 'income', 'weather', 'Y']
correlation_coefficient = np.corrcoef(data[cols].values.T)
#print(correlation_coefficient)

sns.heatmap(correlation_coefficient, annot=True, yticklabels = cols, xticklabels=cols)
plt.show()




classifier_dt = DecisionTreeClassifier(max_depth = 24)
# steps = [
#     #('scalar', StandardScaler()),
#     ('model', DecisionTreeClassifier())
# ]
# dt_pipe = Pipeline(steps)
# parameters = [ { "model__max_depth": np.arange(1,25),
#                  "model__min_samples_leaf": [1, 5, 10, 20, 50, 100],
#                  "model__min_samples_split": np.arange(2, 11),
#                  "model__criterion": ["gini"],
#                  "model__random_state" : [42]}
#             ]

# classifier_dt = GridSearchCV(estimator = dt_pipe,
#                            param_grid  = parameters,
#                            cv = 3,
#                            n_jobs = -1)

#training the model
classifier_dt = classifier_dt.fit(X_train, y_train.ravel())

#fit on training
import time
start_time = time.time()
y_pred_dt_train = classifier_dt.predict(X_test)
# accuracy_dt_train = accuracy_score(y_test, y_pred_dt_train)
# print("Training set: ", accuracy_dt_train)
# cm_dt_train = metrics.confusion_matrix(y_test, y_pred_dt_train)
# cm_lr_display = ConfusionMatrixDisplay(cm_dt_train).plot()
# plt.show()
# #fit on testing

   
result = metrics.confusion_matrix(y_test, y_pred_dt_train)
print("Decision Tree Confusion Matrix:")
print(result)
result1 = metrics.classification_report(y_test, y_pred_dt_train)
print("Decision Tree Classification Report:",)
print (result1)
y_pred_dt_test = classifier_dt.predict(X_test)
accuracy_dt_test = accuracy_score(y_test, y_pred_dt_test)
print("Decision Tree accuracy testing set: ", accuracy_dt_test)
print("--- %s seconds ---" % (time.time() - start_time))



# cm_dt_test = confusion_matrix(y_test, y_pred_dt_test)
# cm_lr_display = ConfusionMatrixDisplay(cm_dt_test).plot()
# plt.show()



# from sklearn.linear_model import LogisticRegression

# lr = LogisticRegression(random_state=0, penalty = 'l2')
# lt_fit = lr.fit(X_train, y_train)
# y_pred_lr_test = lr.predict(X_test)
# accuracy_lr_test = accuracy_score(y_test, y_pred_lr_test)
# print('Decision Tree Accuracy testing set: ',accuracy_lr_test)
# cm_lr = confusion_matrix(y_test, y_pred_lr_test)
# cm_lr_display = ConfusionMatrixDisplay(cm_lr).plot()
# plt.show()
#test

# y_pred_lr_test = lr.predict(X_test)
# accuracy_lr_test = accuracy_score(y_test, y_pred_lr_test)
# print(accuracy_lr_test)
# cm_lr_test = confusion_matrix(y_test, y_pred_lr_test)
# cm_lr_display = ConfusionMatrixDisplay(cm_lr_test).plot()
# plt.show()
#ROC

# y_pred_test_proba = lr.predict_proba(X_test)[::,1]
# fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_test_proba)
# auc = metrics.roc_auc_score(y_test, y_pred_test_proba)

# plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
# plt.legend(loc=4)
# plt.show()

# models = [('Decision Tree', accuracy_dt_train ),
#          ('Logistic Regression', accuracy_lr_train)]
# outcomes = pd.DataFrame(data = models, columns = ['Model' ,'Testing Accuracy','Training Accuracy'])
# print(outcomes)


#KNN
print('K Nearest Neighbour: ')
y = data['Y']
X = data.iloc[:,:-1]

start_time = time.time()
# Standardize features by removing mean and scaling to unit variance:
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test) 

# # Use the KNN classifier to fit data:
# classifier = KNeighborsClassifier(n_neighbors=5)
# classifier.fit(X_train, y_train) 

# # Predict y data with classifier: 
# y_predict = classifier.predict(X_test)

# # Print results: 
# print('Confusion matrix for KNN: ',confusion_matrix(y_test, y_predict))
# print('Classification results: ',classification_report(y_test, y_predict)) 

from sklearn import metrics
range_k = range(1,15)
scores = {}
scores_list = []
distortion = []
for k in range_k:
   classifier = KNeighborsClassifier(n_neighbors=k)
   classifier.fit(X_train, y_train)
   y_pred = classifier.predict(X_test)
   scores[k] = metrics.accuracy_score(y_test,y_pred)
   scores_list.append(metrics.accuracy_score(y_test,y_pred))
  


result = metrics.confusion_matrix(y_test, y_pred)
print("KNN Confusion Matrix:")
print(result)
result1 = metrics.classification_report(y_test, y_pred)
print("KNN Classification Report:",)
print (result1)
accuracy_knn_train = accuracy_score(y_test, y_pred)


import matplotlib.pyplot as plt
plt.plot(range_k,scores_list)
plt.xlabel("Value of K")
plt.ylabel("Accuracy")
print('KNN Accuracy testing set: ',accuracy_knn_train)
print("--- %s seconds ---" % (time.time() - start_time))

#Random Forest
print('Random Forest algorithm: ')

data =  pd.read_csv('clean_invehicle_dataset2.csv')
# Putting feature variable to X
X = data.drop('Y',axis=1)
# Putting response variable to y
y = data['Y']

# Splitting the data into train and test

classifier_rf = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=5,
                                       criterion='gini',max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, oob_score=True)
start_time = time.time()
classifier_rf.fit(X_train, y_train)
y_pred_train=classifier_rf.predict(X_train)
y_pred=classifier_rf.predict(X_test)
print("Testing Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Training Accuracy:",metrics.accuracy_score(y_train, y_pred_train))
print('OOB score',classifier_rf.oob_score_)

accuracy_rf_train = accuracy_score(y_test, y_pred)


# View confusion matrix for test data and predictions

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))
print('Random Forest Accuracy testing set: ',accuracy_rf_train)
print("--- %s seconds ---" % (time.time() - start_time))

#classifier_rf.best_params_


fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(classifier_rf.estimators_[0],
               feature_names =X.columns, 
              
               filled = True);
fig.savefig('rf_individualtree.png')
#print(classifier_rf.predict([[1,0,3,0,80,10,3,1,1,21,2,1,1,0,3,0,0,2,3,2,1,0,0,0,0]]))
