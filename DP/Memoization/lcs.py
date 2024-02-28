s1= "abcdgh"
s2="abedfhr"
n = len(s1)
m = len(s2)
mt = [[0 for x in range(m+1)] for y in range(n+1)]
def lcs(s1,s2,n,m):
    if n==0 or m==0:
        return 0
    if mt[n][m] != 0:
        return mt[n][m]
    if s1[n-1] == s2[m-1]:
        mt[n][m] = 1 + lcs(s1,s2,n-1,m-1)
        return mt[n][m]  
    else:
        mt[n][m] = max(lcs(s1,s2,n-1,m) , lcs(s1,s2,n,m-1))
        return mt[n][m] 
print(lcs(s1,s2,n,m))