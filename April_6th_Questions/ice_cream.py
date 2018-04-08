import numpy as np
import matplotlib.pyplot as plt

def find_coeffs(x,y):
	mean_x = sum(x)/len(x)
	mean_y = sum(y)/len(y)
	numerator = 0
	denominator = 0

	for i in range(len(x)):
		numerator += (x[i]-mean_x)*(y[i]-mean_y)
		denominator += (x[i]-mean_x)**2

	b2 = numerator/denominator
	b1 = mean_y - b2*mean_x

	y_calc = []
	for i in range(len(x)):
		y_calc.append(b1+(b2*x[i]))

	return y_calc

temp = [14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1]
sales = [215,325,185,332,406,522,412,614]

sales_new = find_coeffs(temp,sales)

plt.plot(temp,sales,'ro')
plt.plot(temp,sales_new)
plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.show()