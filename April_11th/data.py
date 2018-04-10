import numpy as np
import pandas as pd


sales = pd.read_csv("data.csv")
print(sales.columns)

#prints min max mean std of a dataframe
print(sales.describe())


print(sales['Unit_price'].describe())

cols = sales.columns

for x in range(len(cols)):
	print("The data type used for %s field is- %s" %(cols[x],type(sales[cols[x]][0])))

print("\n")
print("----Customers data with only Name and Ext_price -----\n")

customers = sales[['Name','Ext_price']]
print(customers)