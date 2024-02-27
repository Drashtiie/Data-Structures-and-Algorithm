class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[-1 for x in range(len(matrix))] for y in range(len(matrix))]
        def rec(m,n):
            prev = matrix[0]
            cur = [-1 for x in range(len(matrix[0]))]
            for i in range(1,m):
                for j in range(n):
                    # print(i,j)
                    if i==0:
                        dp[i][j] = matrix[i][j]
                    elif j == 0:
                        dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + matrix[i][j]
                    elif j == n-1:
                        dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]
                    else:
                        # print(i,j)
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + matrix[i][j]
            # print(dp)
            return min(dp[m-1])
        return rec(len(matrix),len(matrix[-1]))