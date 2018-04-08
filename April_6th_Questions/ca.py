import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name = ['Year','Appeared_g1','Passed_g1','pass_g1_p','Appeared_g2','Passed_g2','pass_g2_p','Appeared_bg','Passed_bg','pass_bg_p']

d = {'Appeared_g1':np.int32,'Passed_g1':np.int32,'pass_g1_p':np.float,'Appeared_g2':np.int32,'Passed_g2':np.int32,'pass_g2_p':np.float,'Appeared_bg':np.int32,'Passed_bg':np.int32,'pass_bg_p':np.float}


data = pd.read_csv('ca_results.csv',names=name,dtype=d,skiprows = 2)

#print(type(data['Appeared_g1'][0]))
w = 0.35
ind = np.arange(8)
fig,ax = plt.subplots()
rects1 = ax.bar(ind,data['Appeared_g1'],width=w,color='b',align='center')

rects2 = ax.bar(ind+w,data['Passed_g1'],width=w,color='g',align='center')
ax.legend((rects1[0],rects2[0]),('Appeared','Passed'))
ax.set_ylabel('Number of CA students')
ax.set_title('Group I - Appeared VS Passed - Yearwise')
ax.set_xticks(ind + w / 2)
ax.set_xticklabels(tuple(data['Year']))

plt.show()