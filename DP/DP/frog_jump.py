n = 4
dp = [-1 for x in range(n)]
def fj(a,arr):
    print(n)
    for i in range(n):
        if i == 0:
            dp[i] = 0
        else:
            rs = 1000
            ls = dp[i-1] + abs(arr[i-1] - arr[i])
            if i>2:
                rs =  dp[i-2] + abs(arr[i-2] - arr[i])
            dp[i] = min(ls,rs)
    
    return dp[n-1]

print(fj(4,[10,20,30,10]))