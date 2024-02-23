class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for x in range(len(triangle))] for y in range(len(triangle))]
        def rec(m,n):
            
            for i in range(m):
                for j in range(n):
                    if i==0 and j==0:
                        dp[i][j] = triangle[i][j]
                    elif i==j:
                        dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
            
        return min(dp[m])