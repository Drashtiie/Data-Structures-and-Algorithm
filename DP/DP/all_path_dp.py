x = [3,2]
dp=[[-1 for x in range(x[1] + 1)] for  y in range(x[0]+1)]
def up(m,n):
    dp[0][0] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j ==0:
                dp[i][j] = 1
            # if i==0 and j == 0:
            #     dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
print(up(3,2))

