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


i = n
j = m
ans = ""
while i>=0 or j>=0:
    if s1[i-1] == s2[j-1]:
        ans+=(s1[i-1])
        i-=1
        j-=1
    else:
        if dp[i-1][j] >= dp[i][j-1]:
            i-=1
        else:
            j-=1
print(ans[::-1])