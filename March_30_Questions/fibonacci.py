def fibonacci(n):
	fib = [0,1,1]
	for i in range(3,n+1):
		fib.append(fib[i-1]+fib[i-2])
	return fib

	
num = int(input())
fib_series = fibonacci(num)	
print(fib_series)