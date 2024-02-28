def LongestRepeatingSubsequence(str1):
		# Code here
		s1 = str1
		s2 = str1
        n = len(s1)
        m = len(s2)
        dp = [[0 for x in range(m+1)] for y in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1] and i!=j:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return (dp[n][m])
print(LongestRepeatingSubsequence("abcd"))