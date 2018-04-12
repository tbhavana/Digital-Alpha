import numpy as np
import operator
import pandas as pd

f = open('input_for_q2.txt','r')

names = pd.read_csv("input_for_q2.csv",names=['Name','age','gender','height','weight'])
print(names)

"""
Name = []
age = []
gender = []
height = []
weight = []
for line in f:
	x = line.split(',')
	Name.append(x[0])
	age.append(int(x[1]))
	gender.append(x[2])
	height.append(int(x[3]))
	weight.append(int(x[4]))

d = dict(zip(Name,height))

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print("Increasing order of height")
for x in sorted_d:
	print(x)
	
"""

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