
def matrixMult(A, B):
	result = []
	for i in range(0,3):
		row = []
		for j in range(0,3):
			x = 0 
			for k in range(0,3):
				x += A[i][k]*B[k][j]
			row.append(x)
		result.append(row)
	return result

	
	
A = [[3,5,6],[4,8,10],[2,1,8]]
I = [[1,0,0],[0,1,0],[0,0,1]]
mult = matrixMult(A,I)
print("The result of multiplying A and I is ")
print(mult)
 
 
