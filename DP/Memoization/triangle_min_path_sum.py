class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mm = [[-1 for x in range(len(triangle))] for y in range(len(triangle))]
        def rec(m,n):
            if m == len(triangle):
                return 0
            if mm[m][n] != -1:
                return mm[m][n]
            dd1 = rec(m+1,n) + triangle[m][n]
            dd2 = rec(m+1,n+1)+ triangle[m][n]
            mm[m][n] = min(dd1,dd2)
            return mm[m][n]
        return rec(0,0)