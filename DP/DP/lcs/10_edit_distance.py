s= "horse"
t = "ros"
def solve(i,j):
            if j<0:
                return i+1
            if i<0:
                return j + 1
            if s[i]==t[j]:
                return solve(i-1,j-1) 
            else:
                ins = solve(i,j-1) + 1
                dl = solve(i-1,j) + 1
                rep = solve(i-1,j-1) + 1
                return min(ins,dl,rep)
n,m=len(s),len(t)
print(solve(n-1,m-1))



#memoize_code

n,m=len(s),len(t)
dp = [[-1 for x in range(m+1)] for y in range(n+1)]
def solve(i,j):
    if j<0:
        return i+1
    if i<0:
        return j + 1
    if dp[i][j] != -1:
        return dp[i][j]

    if s[i]==t[j]:
        dp[i][j] = solve(i-1,j-1) 
        return dp[i][j]
    else:
        ins = solve(i,j-1) + 1
        dl = solve(i-1,j) + 1
        rep = solve(i-1,j-1) + 1
        dp[i][j] =  min(ins,dl,rep)
        return dp[i][j]

print(solve(n-1,m-1))