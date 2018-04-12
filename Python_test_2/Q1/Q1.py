import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

camera = pd.read_csv("camera_1.csv", sep=";")
					

print(camera.head())

print(camera.columns)
cols = camera.columns

print(camera.describe())

cols = camera.columns

for x in range(len(cols)):
	print("The data type used for %s field is- %s" %(cols[x],type(camera[cols[x]][0])))

	
df = camera.loc[0:25,['Model','Release_date','Price']]
print(df)

print(camera['Price'].describe())

price = camera[camera['Price']>1000]


plt.plot(camera['Release_date'],camera['Max_resolution'],'ro')
plt.xlabel('Relsease Date')
plt.ylabel('Max_resolution')
plt.title('Year vs Max_resolution')
plt.show()

plt.plot(camera['Max_resolution'],camera['Normal_focus_range'],'ro')
plt.xlabel('Max_resolution')
plt.ylabel('Normal focus range')
plt.title("Max resolution Vs Focus Range")
plt.show()


camera.Max_resolution.hist()
plt.xlabel('Max_resolution')
plt.title("Histogram of Max_resolution")
plt.show()
