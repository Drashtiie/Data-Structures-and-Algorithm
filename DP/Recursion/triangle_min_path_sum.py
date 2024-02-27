class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def rec(m,n):
            if m == len(triangle):
                return 0
            dd1 = rec(m+1,n) + triangle[m][n]
            dd2 = rec(m+1,n+1)+ triangle[m][n]
            return min(dd1,dd2)
        return rec(0,0)