x = [[5,9,6],[11,5,2]]
dp=[[-1 for x in range(len(x[0]))] for  y in range(len(x))]
def up(m,n):
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i==0 or j ==0:
                print(i,j)
                dp[i][j] = x[i][j]
            # if i==0 and j == 0:
            #     dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + x[i][j]
    return dp[m-1][n-1]
print(up(len(x),len(x[0])))

