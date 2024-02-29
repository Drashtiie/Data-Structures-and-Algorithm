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