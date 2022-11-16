from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score,KFold
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures

import time


start_time = time.time()

#Linear Regression

class LR:
    #load data
    CA_housing =fetch_california_housing(as_frame=True)
    df_all = CA_housing.frame
    df_all = df_all.rename(columns = {'MedHouseVal': 'MEDV'})

    X = df_all[['MedInc', 'HouseAge','AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']].values
    y = df_all[['MEDV']].values
    
    #train and test split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=3)
    
    #standardise the data
    sc = StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.transform(X_test)
    y_train=sc.fit_transform(y_train)
    y_test=sc.transform(y_test)
    
    #fitting the model
    
    lreg=LinearRegression()
   

    
    
    lreg.fit(X_train,y_train)
    
    y_pred = lreg.predict(X_test)
         
    y_pred1 = lreg.predict(X_train)
    
    #MSE calculation
    
    print("Mean squared error for training data Linear Regression: %.2f" % mean_squared_error(y_train,y_pred1))
    
    print("Mean squared errorfor testing data Linear Regression: %.2f" % mean_squared_error(y_test,y_pred))
print("--- %s seconds for Linear Regression ---" % (time.time() - start_time))    
    
start_time = time.time()

#RANSAC
class RANSACRegressor:
    CA_housing =fetch_california_housing(as_frame=True)
    df_all = CA_housing.frame
    df_all = df_all.rename(columns = {'MedHouseVal': 'MEDV'})

    X = df_all[['MedInc', 'HouseAge','AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']].values
    y = df_all[['MEDV']].values
    
    #train and test split

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

    sc = StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.transform(X_test)
    y_train=sc.fit_transform(y_train)
    y_test=sc.transform(y_test)
    
    
    #fitting the model
    ransac = RANSACRegressor(LinearRegression(), 
                             loss='absolute_loss',
                             residual_threshold=5.0, random_state=1)
    
    ransac.fit(X_train,y_train)
    

    
    
    
    y_pred = ransac.predict(X_test)
    
     
    y_pred1 = ransac.predict(X_train)
    
    
    #MSE calculation
    
    print("Mean squared error for training data RANSAC: %.2f" % mean_squared_error(y_train,y_pred1))
    
    print("Mean squared error for testing data RANSAc: %.2f" % mean_squared_error(y_test,y_pred))
    
print("--- %s seconds for Ransac ---" % (time.time() - start_time))  
start_time = time.time()  

#Lasso  
class LASSO:
    CA_housing =fetch_california_housing(as_frame=True)
    df_all = CA_housing.frame
    df_all = df_all.rename(columns = {'MedHouseVal': 'MEDV'})

    X = df_all[['MedInc', 'HouseAge','AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']].values
    y = df_all[['MEDV']].values
    
    
    #train and test split

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=4)

    sc = StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.transform(X_test)
    y_train=sc.fit_transform(y_train)
    y_test=sc.transform(y_test)
    #fitting the model
    ls = Lasso(alpha=1.0)
    ls.fit(X_train,y_train)
    y_pred = ls.predict(X_test)
     
    y_pred1 = ls.predict(X_train)
    

    
    
    
    y_pred = ls.predict(X_test)
    
     
    y_pred1 = ls.predict(X_train)
    
    
    #MSE calculation
    
    print("Mean squared error for training data Lasso: %.2f" % mean_squared_error(y_train,y_pred1))
    
    print("Mean squared error for testing data Lasso: %.2f" % mean_squared_error(y_test,y_pred))
print("--- %s seconds for Lasso ---" % (time.time() - start_time))  

start_time = time.time()  

#Ridge
class Ridge:
    CA_housing =fetch_california_housing(as_frame=True)
    df_all = CA_housing.frame
    df_all = df_all.rename(columns = {'MedHouseVal': 'MEDV'})

    X = df_all[['MedInc', 'HouseAge','AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']].values
    y = df_all[['MEDV']].values
    
    #train and test split

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

    sc = StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.transform(X_test)
    y_train=sc.fit_transform(y_train)
    y_test=sc.transform(y_test)
    
    
    #fitting the model
    ridge = Ridge(alpha=4.0)
    ridge.fit(X_train,y_train)
    y_pred = ridge.predict(X_test)
    
     
    y_pred1 = ridge.predict(X_train)

    
    
    

    
    #MSE calculation
    
    print("Mean squared error for training data Ridge: %.2f" % mean_squared_error(y_train,y_pred1))
    
    print("Mean squared error for testing data Ridge: %.2f" % mean_squared_error(y_test,y_pred))
    
print("--- %s seconds for Ridge ---" % (time.time() - start_time)) 

start_time = time.time()  
#Non linear
class Nonlinear:
    CA_housing =fetch_california_housing(as_frame=True)
    df_all = CA_housing.frame
    df_all = df_all.rename(columns = {'MedHouseVal': 'MEDV'})

    X = df_all[['MedInc', 'HouseAge','AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']].values
    y = df_all[['MEDV']].values
    
    
    #train and test split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
     #linear
    lr_linear = LinearRegression()
    lr_linear.fit(X_train,y_train)
    y_pred_linear_train = lr_linear.predict(X_train)
    y_pred_linear_test = lr_linear.predict(X_test)
    MSE_linear_test = mean_squared_error(y_test,y_pred_linear_test)
    MSE_linear_train = mean_squared_error(y_train,y_pred_linear_train)
    
     #polynomial 2nd degree (quadratic)
    quadratic = PolynomialFeatures(degree=2) 
    X_quadratic_train = quadratic.fit_transform(X_train)
    X_quadratic_test = quadratic.fit_transform(X_test)
    lr_quadratic = LinearRegression()
    lr_quadratic.fit(X_quadratic_train,y_train)
    y_pred_quadratic_train=lr_quadratic.predict(X_quadratic_train) 
    y_pred_quadratic_test=lr_quadratic.predict(X_quadratic_test) 
    MSE_quadratic_train = mean_squared_error(y_train,y_pred_quadratic_train)
    MSE_quadratic_test = mean_squared_error(y_test,y_pred_quadratic_test)
    
    cubic = PolynomialFeatures(degree=3) 
    X_cubic_train = cubic.fit_transform(X_train)
    X_cubic_test = cubic.fit_transform(X_test)
    lr_cubic = LinearRegression()
    lr_cubic.fit(X_cubic_train,y_train)
    y_pred_cubic_train=lr_cubic.predict(X_cubic_train) 
    y_pred_cubic_test=lr_cubic.predict(X_cubic_test) 
    MSE_cubic_train = mean_squared_error(y_train,y_pred_cubic_train)
    MSE_cubic_test = mean_squared_error(y_test,y_pred_cubic_test)
    
    print("MSE linear train : %.3f , quadratic train %.3f , cubic train : %.3f "
    %(MSE_linear_train , MSE_quadratic_train , MSE_cubic_train ) )
    
    print("MSE linear test: %.3f , quadratic test %.3f , cubic test: %.3f "
    %(MSE_linear_test , MSE_quadratic_test , MSE_cubic_test ) )
    
    

        
print("--- %s seconds for non linear regression ---" % (time.time() - start_time))
    