import statistics

liquid_weight = [11.95,11.91,11.86,11.94,12.00,11.93,12.00,11.94,12.10,11.95,11.99,11.94,11.89,12.01,11.99,11.94]

lis = sorted(liquid_weight)
size = len(liquid_weight)
mean = sum(liquid_weight)/size
median = lis[size//2] if size%2!=0 else (lis[size//2]+lis[size//2+1])/2
mod = statistics.mode(lis)

intervals = ['11.86-11.89','11.90-11.93','11.94-11.97','11.98-12.01','12.02-12.05','12.06-12.09','12.10-12.13']
freq = {}
for x in range(size):
	for y in range(7):
		low,high = map(lambda x: float(x),intervals[y].split("-"))
		if(liquid_weight[x]>= low and liquid_weight[x]<=high):
			if (low,high) not in freq:
				freq[(low,high)] = 1
			else:
				freq[(low,high)] += 1



print("FREQUENCY DISTRIBUTION")
print("-----------------------")
print("RANGE        COUNT")
for x,y in freq.items():
	print(str(x) + "   " + str(y))

print("-------------------------")
print("Mean = " + str(mean))
print("Median = "+ str(median))
print("Mode = "+ str(mod))
