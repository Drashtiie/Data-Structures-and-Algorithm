s1= "babgbag"
s2="bag"
n = len(s1)
m = len(s2)
# def lcs(s1,s2,n,m):
#     if m < 0:
#         return 1
#     if n<0:
#         return 0
    
    
#     if s1[n-1] == s2[m-1]:
        
#         return lcs(s1,s2,n-1,m-1)+lcs(s1,s2,n-1,m)
#     else:
#         return lcs(s1,s2,n-1,m)
# print(lcs(s1,s2,n,m))

#memoized code
dp = [[-1 for x in range(m+1)] for y in range(n+1)]
def solve(i,j):
            if j<0:
                
                return 1
            if i<0:
                return 0
            if dp[i][j] != -1:
                  return dp[i][j]
            if s[i]==t[j]:
                 dp[i][j] = solve(i-1,j-1) + solve(i-1,j)
                 return  dp[i][j]
            else:
                dp[i][j] = solve(i-1,j)
                return  dp[i][j]
s=s1
t=s2
n,m=len(s1),len(s2)
print(solve(n-1,m-1))

#dp code
s= "babgbag"
t="bag"
dp = [[-1 for x in range(m+1)] for y in range(n+1)]
n,m=len(s1),len(s2)
for i in range(n+1):
    for j in range(m+1):
            if j == 0:
                  dp[i][j] = 1
            elif i == 0:
                  dp[i][j] = 0
            if s[i-1] == t[j-1]:
                 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                  dp[i][j] = dp[i-1][j]
print(dp[n][m])




s= "babgbag"
t="bag"
dn,m=len(s),len(t)
dp=[[-1 for j in range(m+1)] for i in range(n+1)] #Shifting the indexes
for i in range(n+1):
    dp[i][0]=1
for j in range(1,m+1): # we are starting it from 1 because for j<1 we have to return 1
    dp[0][j]=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1] + dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][m])