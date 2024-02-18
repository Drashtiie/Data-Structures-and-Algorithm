n = 5
dp = [-1 for x in range(n+1)]
def fib(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
    

print(fib(5))