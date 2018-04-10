import pandas as pd
import numpy as np

marks = {"Name":["A","B","C","D"],"mks_s1":[65,78,54,70],
"mks_s2":[59,65,43,38],"mks_s3":[69,97,98,78],"mks_s4":[88,98,64,76]}

marks_df = pd.DataFrame(marks)

marks_df.index = [1,2,3,4]
marks_df.index.name = 'RollNo'

print(marks_df)

marks_df['high_marks'] = marks_df[['mks_s1',"mks_s2","mks_s3","mks_s4"]].max(axis=1)

print("----Highest marks of each student ---")
print(marks_df[['Name','high_marks']])

marks_df['percentage'] = (marks_df['mks_s1']+marks_df['mks_s2']+marks_df['mks_s3']+marks_df['mks_s4'])/4.0

top_percentage = marks_df['percentage'].max()

print("Toper among the 4 students is ")
print(marks_df.loc[marks_df['percentage']==top_percentage])


print("Marks of students of first two roll numbers--")
print(marks_df.loc[0:2,['mks_s1','mks_s2','mks_s3','mks_s4']])

print("\n")
marks_df = marks_df.drop(['high_marks','percentage'],axis = 1)

#print(marks_df)
'''
roll_5 = pd.DataFrame(["E",75,43,87,91])
roll_6 = pd.DataFrame(["F",76,71,56,49])
'''
print("After adding 5th and 6th student - ")

marks_df.loc[5] = ["E",75,43,87,91]
marks_df.loc[6] = ["F",76,71,56,49]
print(marks_df)