s1= "abcdgh"
s2="abedfhr"
n = len(s1)
m = len(s2)
dp = [[0 for x in range(m+1)] for y in range(n+1)]
ans = 0
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans,dp[i][j])
        else:
            dp[i][j] = 0
print(ans)

 