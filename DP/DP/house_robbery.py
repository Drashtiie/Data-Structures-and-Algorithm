n = 4
dp = [-1 for x in range(n+1)]
def sub(n,arr):
    dp[0] = 0
    dp[1] = arr[0]
    dp[2] = max(arr[0],arr[1])
    for i in range(3,n+1):
       dp[i] = max(dp[i-1], arr[i-1] + dp[i-2])
    return dp[n]
            
    # print(a,arr)
    # if a == 0:
    #     return 0
    # if a < 0:
    #     return 0
    # print(arr[a-1])
    # if m[a-2]!= -1:
    #     p1 = m[a-1] + arr[a-1]
    # else: 
    #  p1 = arr[a-1] + sub(a-2,arr)
    # if m[a-1] != -1:
    #   np = m[a-2]
    # else:   
    #     np = sub(a-1,arr)
    # print(p1,np)
    # m[a] = max(p1,np)
    
    # return m[a]
print(sub(4,[2,1,4,9])) 