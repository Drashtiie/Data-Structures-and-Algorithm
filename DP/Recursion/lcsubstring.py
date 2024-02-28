s1= "abcdgh"
s2="abedfhr"
n = len(s1)
m = len(s2)
ans = 0
def lcs(s1,s2,n,m):
    global ans
    if n==0 or m==0:
        return 0
    if s1[n-1] == s2[m-1]:
        t = 1 + lcs(s1,s2,n-1,m-1)
        ans = max(ans,t)
        return t
    else:
        return 0
lcs(s1,s2,n,m)
print(ans)