print("Enter student marks in the following format - Name sub1 sub2 sub3")

Names = []
sub1 = []
sub2 = []
sub3 = []

for i in range(10):	
	row = input()
	x = row.split(" ")
	Names.append(x[0])
	sub1.append(int(x[1]))
	sub2.append(int(x[2]))
	sub3.append(int(x[3]))

mean_s1 = sum(sub1)/10
mean_s2 = sum(sub2)/10
mean_s3 = sum(sub3)/10

s1 = sorted(sub1)
s2 = sorted(sub2)
s3 = sorted(sub3)

median_1 = (s1[5]+s1[6])/2
median_2 = (s2[5]+s2[6])/2
median_3 = (s3[5]+s3[6])/2
print("Mean for the three subjects is " + str(mean_s1)+ " "+str(mean_s2)+" "+str(mean_s3))
print("Medians for the three subjects are " + str(median_1)+ " "+str(median_2)+" "+str(median_3))

percentage = []
# Calculating the percentages of student marks to get top 3 students

for x in map(lambda l1,l2,l3:(l1+l2+l3)/3 ,sub1,sub2,sub3):  
	percentage.append(x)

top3 = []
	
for i in range(3):
	top1 = max(percentage)
	std1 = percentage.index(top1)
	top3.append(Names[std1])
	percentage[std1] = -1
	
print("Top 3 students are -"+ str(top3))



	