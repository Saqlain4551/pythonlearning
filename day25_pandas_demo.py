import pandas as pd
import numpy as np 

#Creating Pandas Series with Default Index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)
#output
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

#Creating Pandas Series with custom index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums , index=[1,2,3,4,5])
print(s)
#output
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# dtype: int64

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)
#ouput
# 1    Orange
# 2    Banana
# 3     Mango
# dtype: object

#Creating Pandas Series from a Dictionary

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)
#output
# name       Asabeneh
# country     Finland
# city       Helsinki
# dtype: object

#Creating a Pandas Series Using Linspace

s = pd.Series(np.linspace(5 , 20 , 30))
print(s)
#output
# 0      5.000000
# 1      5.517241
# 2      6.034483
# 3      6.551724
# 4      7.068966
# 5      7.586207
# 6      8.103448
# 7      8.620690
# 8      9.137931
# 9      9.655172
# 10    10.172414
# 11    10.689655
# 12    11.206897
# 13    11.724138
# 14    12.241379
# 15    12.758621
# 16    13.275862
# 17    13.793103
# 18    14.310345
# 19    14.827586
# 20    15.344828
# 21    15.862069
# 22    16.379310
# 23    16.896552
# 24    17.413793
# 25    17.931034
# 26    18.448276
# 27    18.965517
# 28    19.482759
# 29    20.000000
# dtype: float64

# DATA FRAME

data = [
    ['saqlain', 'India', 'Mumbra'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data , columns= ['Name','Country','City'])
print(df)
#output
#    Name Country       City
# 0  saqlain   India     Mumbra
# 1    David      UK     London
# 2     John  Sweden  Stockholm

#Creating DataFrame Using Dictionary
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(data)

# Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
#output
#     Name      Country       City
# 0  Asabeneh  Finland   Helsinki
# 1     David       UK     London
# 2      John   Sweden  Stockholm

#Reading CSV File Using Pandas

df = pd.read_csv('weight-height.csv')
print(df)
#output
#       Gender     Height      Weight
# 0       Male  73.847017  241.893563
# 1       Male  68.781904  162.310473
# 2       Male  74.110105  212.740856
# 3       Male  71.730978  220.042470
# 4       Male  69.881796  206.349801
# ...      ...        ...         ...
# 9995  Female  66.172652  136.777454
# 9996  Female  67.067155  170.867906
# 9997  Female  63.867992  128.475319
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103

# [10000 rows x 3 columns]

print(df.head())
#output
#  Gender     Height      Weight
# 0   Male  73.847017  241.893563
# 1   Male  68.781904  162.310473
# 2   Male  74.110105  212.740856
# 3   Male  71.730978  220.042470
# 4   Male  69.881796  206.349801

print(df.tail())
#output
#  Gender     Height      Weight
# 9995  Female  66.172652  136.777454
# 9996  Female  67.067155  170.867906
# 9997  Female  63.867992  128.475319
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103

print(df.shape)  # many row and columns are there so how we can know how many rows are there thats way use the (shape)
#output
# (10000, 3)

print(df.columns)   # if we want all column
#output Index(['Gender', 'Height', 'Weight'], dtype='object')  

Heights = df['Height']
print(Heights)
#output
# #0       73.847017
# 1       68.781904
# 2       74.110105
# 3       71.730978
# 4       69.881796
#           ...
# 9995    66.172652
# 9996    67.067155
# 9997    63.867992
# 9998    69.034243
# 9999    61.944246
# Name: Height, Length: 10000, dtype: float64

print(Heights.describe()) # give statisical information about height data
#output
# count    10000.000000
# mean        66.367560
# std          3.847528
# min         54.263133
# 25%         63.505620
# 50%         66.318070
# 75%         69.174262
# max         78.998742
# Name: Height, dtype: float6

# Modifying a DataFrame
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
#Adding a New Column

heights = [173, 175, 169]
df['Height'] = heights
print(df)
#output
#  Name  Country       City  Height
# 0  Asabeneh  Finland   Helsinki     173
# 1     David       UK     London     175
# 2      John   Sweden  Stockholm     169

weights = [74, 78, 69]
df['Weight'] = weights
df

def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()
df['BMI'] = bmi
df
