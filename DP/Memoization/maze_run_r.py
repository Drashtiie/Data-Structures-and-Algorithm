def uniquePaths(m, n, a):
	# Write your code here.
	if m>0 and n>0 and a[m][n] == -1:
		return 0

	if m == 0 and n == 0:
		return 1
	elif m <0 or n<0:
		return 0
	
	lp = uniquePaths(m-1,n,a)
	rp = uniquePaths(m,n-1,a)
	return lp+rp



print(uniquePaths(2,2,[[0,0,0],[0,-1,0],[0,0,0]]))	