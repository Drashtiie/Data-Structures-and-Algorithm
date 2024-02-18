
t = [[-1 for x in range(100)]for y in range(100)]
# print(t)

def uniquePaths(m, n):
	print(t[m][n])
	# Write your code here.

	if m == 0 and n == 0:
		return 1
	elif m <0 or n<0:
		return 0
	elif t[m][n] != -1 :
		return t[m][n]
	else:
		lp = uniquePaths(m-1,n)
		rp = uniquePaths(m,n-1)
		t[m][n] = lp+rp
		return t[m][n]

t1 = int(input())

print(t1)
for i in range(t1):
	x = input()
	x=x.split()

	print(uniquePaths(int(x[0]) - 1,int(x[1]) -1))	