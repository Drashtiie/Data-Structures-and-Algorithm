s1= "abcdgh"
s2="abedfhr"
n = len(s1)
m = len(s2)
dp = [[0 for x in range(m+1)] for y in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[n][m])

               
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
# print(lcs(s1,s2,n,m))