import numpy as np
import operator
import pandas as pd

names = pd.read_csv("input_for_q2.csv",names=['Name','age','gender','height','weight'])
print(names)

#Sorting according to height
df = names.sort_values('height')
print(df)

#Calculating BMI
names['BMI'] = (names['weight'])/((names['height']*0.01)**2)
print(names)

print(names.groupby('BMI').mean())

healthy = names[(names['BMI']>18) & (names['BMI']<25)]
over = names[(names['BMI']>=25) & (names['BMI']<29)]
obese = names[(names['BMI']>=30)]

print("--Healthy students--")
print(healthy[['Name','BMI']])
print("--Over  Weight Students --")
print(over[['Name','BMI']])
print("--Obese Students --")
print(obese[['Name','BMI']])
