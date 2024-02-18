def uniquePaths(m, n):
	# Write your code here.

	if m == 0 and n == 0:
		return 1
	elif m <0 or n<0:
		return 0
	lp = uniquePaths(m-1,n)
	rp = uniquePaths(m,n-1)
	return lp+rp

t = int(input())

print(t)
for i in range(t):
	x = input()
	x=x.split()

	print(uniquePaths(int(x[0]) - 1,int(x[1]) -1))	