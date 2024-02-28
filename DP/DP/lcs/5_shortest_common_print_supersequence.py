# to be solved, partly done, running for some test cases
s1 = "bbbaaaba"
s2 = "bbababbb"

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
# print(dp[n][m])

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
print("lcs ",ans[::-1])

# i = n
# j = m
# ans = ""
# while i>=0 and j>=0:
#     if s1[i-1] == s2[j-1]:
#         ans+=(s1[i-1])
#         i-=1
#         j-=1
#     else:
#         if dp[i-1][j] >= dp[i][j-1]:
#             ans += s1[i-1]
#             i-=1
            
#         else:
#             ans+= s2[j-1]
#             j-=1
# print(ans[::-1])
ss = ""
p=len(ans)
i=0
j=0
k=0
while i<n and j<m and k<p:
    if s1[i] == ans[k] and s2[j] == ans[k]:
         ss += ans[k]
         k+=1
         i+=1
         j+=1
    else:
        if s1[i] != ans[k]:
            while i<n and s1[i] != ans[k]:
                ss+=s1[i]
                i+=1
        if s2[j] == ans[k]:
             while j<m and s2[j] != ans[k]:
                ss+=s2[j]
                j+=1
        ss+=ans[k]
        k+=1
        i+=1
        j+=1
print(ss)
     



# leetcode solution

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if str1[ind1-1] == str2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = 0 + max(dp[ind1-1][ind2], dp[ind1][ind2-1])
        
        i = n
        j = m
        ans = ""
        while i>0 and j>0:
            if str1[i-1] == str2[j-1]:
                ans+=str1[i-1]
                i -=1
                j -=1
            elif dp[i-1][j] > dp[i][j-1]:# up
                ans+=str1[i-1]
                i-=1
            else:
                ans+=str2[j-1]
                j-=1
        while i > 0:
            ans += str1[i - 1]
            i -= 1
        while j > 0:
            ans += str2[j - 1]
            j -= 1

        
        return ans[::-1]
            

        