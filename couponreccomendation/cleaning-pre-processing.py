import pandas as pd
import pandas as pd
import numpy as np


data = pd.read_csv('in-vehicle-coupon-recommendation.csv')
data.drop(['toCoupon_GEQ5min'], axis=1, inplace = True)
print(data.head())

#data description
#shape of the dataset
print('Data shape: ',data.shape)
#all columns:
print('All columns: ',data.info())
#data summary
print('Data Summary: ',data.describe())

#checking null values
x=data.isnull().sum()
print('Total missing values for each column: ',x)

data.drop(['car'], axis=1, inplace=True)


data['age']= np.where(data['age']=='50plus','51',data['age'])
data['age']= np.where(data['age']=='below21','20',data['age'])

data = data.replace({'Bar':{'never': 0, 'less1': 1, '1~3': 2, '4~8': 3, 'gt8': 4},
                    'CoffeeHouse':{'never': 0, 'less1': 1, '1~3': 2, '4~8': 3, 'gt8': 4}, 
                    'CarryAway':{'never': 0, 'less1': 1, '1~3': 2, '4~8': 3, 'gt8': 4}, 
                    'RestaurantLessThan20':{'never': 0, 'less1': 1, '1~3': 2, '4~8': 3, 'gt8': 4},
                    'Restaurant20To50':{'never': 0, 'less1': 1, '1~3': 2, '4~8': 3, 'gt8': 4},
                    'time':{'6PM': 18,'7AM': 7,'10AM':10,'2PM':14,'10PM':22},
                    'expiration':{'1d':1,'2h':2},
                    'age':{21:21,26:26,31:31,'50plus':51,36:36,41:41,46:46,'below21':20},
                    'gender' :{'Male': 0, 'Female':1},
                    'weather': {'Sunny': 0, 'Snowy': 1, 'Rainy': 2},
                    'destination':{'No Urgent Place':0,'Home':1, 'Work':2},
                    'passanger':{'Alone':0,'Friend(s)':1,'Partner':2, 'Kid(s)':3},
                    'coupon':{'Coffee House':0,'Restaurant(<20)':1,'Carry out & Take away':2,'Bar':3,
                              'Restaurant(20-50)':4},
                    'maritalStatus':{'Married partner':0,'Single':1,'Unmarried partner':2,'Divorced':3,
                                     'Widowed':4},
                    'education':{'Bachelors degree':0,'Some college - no degree':1,'Graduate degree (Masters or Doctorate)':2,
                                 'Associates degree':3,'High School Graduate':4,'Some High School':5},
                    'occupation':{'Unemployed':0,'Student':1,'Computer & Mathematical':2, 'Sales & Related':3,
                                  'Education&Training&Library':4, 'Management':5,'Arts Design Entertainment Sports & Media':6,
                                  'Retired':7,'Office & Administrative Support':8,'Business & Financial':9,
                                  'Food Preparation & Serving Related':10,'Healthcare Support':11,'Transportation & Material Moving':12,
                                  'Healthcare Practitioners & Technical':13,'Life Physical Social Science':14,'Legal':15,
                                  'Community & Social Services':16,'Personal Care & Service':17,'Architecture & Engineering':18,
                                  'Protective Service':19,'Construction & Extraction':20,'Production Occupations':21,
                                  'Installation Maintenance & Repair':22,'Building & Grounds Cleaning & Maintenance':23,
                                  'Farming Fishing & Forestry':24},
                    'income':{'Less than $12500':0,'$12500 - $24999':1,'$25000 - $37499':2,'$37500 - $49999':3,
                              '$50000 - $62499':4,'$62500 - $74999':5,'$75000 - $87499':6,'$87500 - $99999':7,
                              '$100000 or More':8},
                    
                    
                    })
data.fillna(data.mode().iloc[0],inplace=True)
                    
data.to_csv('clean_invehicle_dataset2.csv')