import pandas as pd
import pandas as pd
import numpy as np


# df = pd.read_csv("data-test.csv")

# empty_cols = [col for col in df.columns if df[col].isnull().all()]
# # Drop these columns from the dataframe
# df.drop(empty_cols,
#         axis=1,
#         inplace=True)
# df.drop(['ID'], axis=1, inplace=True)
# df.drop(['Start time'], axis=1, inplace=True)
# df.drop(['Completion time'], axis=1, inplace=True)
# df.drop(['Email'], axis=1, inplace=True)
# #df.drop(['Unnamed: 0'], axis=1, inplace=True)

# df.to_csv('data-test-clean.csv', index = None)


import pandas as pd
import pandas as pd
import numpy as np


data = pd.read_csv('data-test-clean.csv')




data = data.replace({'Bar':{'Never': 0, 'Less1': 1,'Less than 2':1, '1 to 3 times': 2, '4 to 8 times': 3, 'gt8': 4},
                    'CoffeeHouse':{'Never': 0, 'Less than 1': 1,'Less than 2':1, '1 to 3 times': 2, '4 to 8 times': 3, 'gt8': 4}, 
                    'CarryAway':{'Never': 0, 'Less than 1': 1,'Less than 2':1, '1 to 3 times': 2, '4 to 8 times': 3, 'gt8': 4}, 
                    'RestaurantLessThan20':{'Never': 0, 'Less than 1': 1,'Less than 2':1, '1 to 3 times': 2, '4 - 8 times': 3, 'gt8': 4},
                    'Restaurant20To50':{'Never': 0, 'Less than 1': 1,'Less than 2':1, '1 to 3 times': 2, '4 - 8 times': 3, 'gt8': 4},
                    'time':{'6PM': 18,'7AM': 7,'10AM':10,'2PM':14,'10PM':22,'7PM':19},
                    'expiration':{'In 1 day':1,'In 2 hours':2},
                    'age':{21:21,26:26,31:31,'50plus':51,36:36,41:41,46:46,'below21':20},
                    'gender' :{'Male': 0, 'Female':1},
                    'weather': {'Sunny': 0, 'Snowy': 1, 'Rainy': 2},
                    'destination':{'No Urgent Place':0,'Home':1, 'Work':2},
                    'passanger':{'Alone':0,'With friends':1,'With my partners':2, 'Kid(s)':3},
                    'coupon':{'Coffee House':0,'Restaurant (<$20)':1,'Carry Out $ Take Away':2,'Carry Out & Take Away':2,'Bar':3,
                              'Restaurant ($20-$50)':4},
                    'maritalStatus':{'Married':0,'Single':1,'Unmarried partner':2,'Divorced':3,
                                     'Widowed':4},
                    'education':{'Bachelors degree':0,'Some college - no degree':1,'Graduate degree (Masters or Doctorate)':2,
                                 'Associates degree':3,'High School Graduate':4,'Some High School':5},
                    'occupation':{'Unemployed':0,'Student ':1,'Student':1,'student':1,'Computer & Mathematical':2, 'Sales & Related':3,
                                  'Education&Training&Library':4, 'Management':5,'Arts Design Entertainment Sports & Media':6,
                                  'Retired':7,'Office & Administrative Support':8,'Business & Financial':9,
                                  'Food Preparation & Serving Related':10,'Healthcare Support':11,'Transportation & Material Moving':12,
                                  'Healthcare Practitioners & Technical':13,'Life Physical Social Science':14,'Legal':15,
                                  'Community & Social Services':16,'Personal Care & Service':17,'Architecture & Engineering':18,
                                  'Protective Service':19,'Construction & Extraction':20,'Production Occupations':21,
                                  'Installation Maintenance & Repair':22,'Building & Grounds Cleaning & Maintenance':23,
                                  'Farming Fishing & Forestry':24,'Data entry operator':25,'Chick-fil-a Employee':26,'Student Researcher':27,
                                  'Software ':28,'office worker':29,'Technician':30,'Employed':31,'SDE':32,'Working ':33},
                    'income':{'Less than $12500':0,'$12500 - $24999':1,'$25000 - $37499':2,'$37500 - $49999':3,
                              '$50000 - $62499':4,'$62500 - $74999':5,'$75000 - $87499':6,'$87500 - $99999':7,
                              '$100000 or More':8},
                    'has_children':{'Yes':1,'No':0},
                    'toCoupon_GEQ15min':{'Yes':1,'No':0},
                    'toCoupon_GEQ25min':{'Yes':1,'No':0},
                    'direction_same':{'Yes':1,'No':0},
                    'direction_opp':{'Yes':1,'No':0},
                    'Y':{'Yes':1,'No':0}
                    
                    
                    })
data.fillna(data.mode().iloc[0],inplace=True)
                    
data.to_csv('data-test-clean22.csv')
