arr = [1,2,4,2]
k = 6
N = len(arr)
m = [[-1 for x in range(N+1)]for x in range(k+1)]
dp = [[-1 for x in range(k+1)] for y in range(N+1)]
dp[0] = [0 for x in range(k+1)]
dp[0][0] = 1
for i in range(1,N+1):
            for j in range(k+1):
                        print(i,j)
                        
                        if j == 0:
                                dp[i][j] = 1
                                print(dp)
                        if j < arr[i-1]:
                                dp[i][j] = dp[i-1][j]
                        # if arr[i-1] <= j:
                        #         dp[i][j] = dp[i-1][j-arr[i]]
                        
                        else:
                                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            print(dp)
print(dp)                       
                            
                    
        



