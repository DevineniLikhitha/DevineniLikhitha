#!/usr/bin/env python
# coding: utf-8

# In[76]:


import numpy as np
import pandas as pd
import os
import sklearn
from sklearn.multiclass import  OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import gc


# In[77]:


data = pd.read_csv('iris.data.txt')

data


# In[78]:


data.Species.value_counts()


# In[79]:


data.describe().transpose()


# In[80]:


data.head()


# In[81]:


data['Species'] = data['Species'].astype('category').cat.codes
features = data.select_dtypes('float').columns
target = ['Species']

# Feature& Target  Dataset
X = data[features]
y = data[target]
test_size = 0.3

#Dataset Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0) 

#Feature Scaling
#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)

#Reset Index
X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)


# In[82]:


model = SVC(gamma='scale',random_state=0)


# In[83]:



ovr = OneVsRestClassifier(model)

#fit model to training data
ovr.fit(X_train, y_train)

#Predications
ovr_pred = ovr.predict(X_test)

#Adding Predictions to Test Dataset
ovr_df = X_test.copy()
ovr_df.insert(4,"Actual",y_test, True)
ovr_df.insert(5,"Predicted",ovr_pred, True)


# In[84]:


ovr_df.head()


# In[85]:


ovr_df


# In[98]:


from sklearn.metrics import accuracy_score,f1_score


# In[87]:


#sgd


# In[88]:


from sklearn.linear_model import SGDClassifier
clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf.fit(X, y)
SGDClassifier(max_iter=5)


# In[89]:


clf.predict([[5.0,3.4,1.5,0.2]])


# In[93]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,ovr_pred)


# In[96]:


accuracy_score(y_test,ovr_pred)


# In[99]:


f1_score(y_test,ovr_pred)

