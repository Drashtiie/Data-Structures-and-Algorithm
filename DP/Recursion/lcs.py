s1= "abcdgh"
s2="abedfhr"
n = len(s1)
m = len(s2)
def lcs(s1,s2,n,m):
    if n==0 or m==0:
        return 0
    if s1[n-1] == s2[m-1]:
        return 1 + lcs(s1,s2,n-1,m-1)
    else:
        return max(lcs(s1,s2,n-1,m) , lcs(s1,s2,n,m-1))
print(lcs(s1,s2,n,m))