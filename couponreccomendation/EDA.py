import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data =  pd.read_csv('clean_invehicle_dataset2.csv')

X_train = data.iloc[:,:-1]
y_train = data.iloc[:,-1]



# data.drop(['Bar'], axis=1, inplace = True)
# data.drop(['CoffeeHouse'], axis=1, inplace = True)
# data.drop(['CarryAway'], axis=1, inplace = True)
# data.drop(['RestaurantLessThan20'], axis=1, inplace = True)
# data.drop(['Restaurant20To50'], axis=1, inplace = True)
# data.drop(['toCoupon_GEQ5min'], axis=1, inplace = True)
# data.drop(['toCoupon_GEQ15min'], axis=1, inplace = True)
# data.drop(['toCoupon_GEQ25min'], axis=1, inplace = True)
# data.drop(['direction_same'], axis=1, inplace = True)
# data.drop(['direction_opp'], axis=1, inplace = True)

# data.to_csv('clean_invehicle_dataset3.csv', index = False)

y = data['Y']
X = data.iloc[:,:-1]


colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(X.astype(float).corr(),linewidths=0.1,vmax=1.0, 
            square=True, cmap=colormap, linecolor='white', annot=True)

cat_vars = ['destination','passanger','weather','temperature','time',
            'coupon','expiration','gender','age','maritalStatus','has_children',
            'education','occupation','income','toCoupon_GEQ15min','toCoupon_GEQ25min']

#Gender

accept = data[(data['Y'] == 1)]
for i in cat_vars: 
    plt.figure(figsize=(14,6))
    sns.set_palette(sns.color_palette(('grey','blue')))
    sns.countplot(data=X, x= data[i], hue= data['Y'])
    
    

colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(data.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)

plt.show()



