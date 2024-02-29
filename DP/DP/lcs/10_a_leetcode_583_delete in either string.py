s= "sea"
t = "eat"
def solve(i,j):
            if j<0:
                return i+1
            if i<0:
                return j + 1
            if s[i]==t[j]:
                return solve(i-1,j-1) 
            else:
                ds2 = solve(i,j-1) + 1
                ds1 = solve(i-1,j) + 1
                
                return min(ds2,ds1)
n,m=len(s),len(t)
print(solve(n-1,m-1))


#memoize

n,m=len(s),len(t)
dp = [[-1 for x in range(m+1)] for y in range(n+1)]
def solve(i,j):
    if j<0:
        return i+1
    if i<0:
        return j + 1
    if dp[i][j] != -1:
        return dp[i][j]

    if s[i]==t[j]:
        dp[i][j] = solve(i-1,j-1) 
        return dp[i][j]
    else:
        ds2 = solve(i,j-1) + 1
        ds1 = solve(i-1,j) + 1
                
                 
        dp[i][j] =  min(ds2,ds1)
        return dp[i][j]


#dp
    

n,m=len(s),len(t)
dp = [[-1 for x in range(m+1)] for y in range(n+1)]
for j in range(m+1):
     dp[0][j] = j
for i in range(n+1):
     dp[i][0] = i
for i in range(1,n+1):
     for j in range(1,m+1):
          if s[i-1] == t[j-1]:
               dp[i][j] = dp[i-1][j-1]
          else:
               dp[i][j] = 1 + min(dp[i-1][j] , dp[i][j-1])
print(dp[n][m])