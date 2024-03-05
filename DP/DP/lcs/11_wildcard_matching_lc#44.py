s= "a"
t = "aa"
def solve(i,j):
            if i <0 and j<0:
                  return True
            if j<0:
                  return False
            if i<0:
                print(True)
                while j>0 and ( t[j] == "*" or t[j] == "+"):
                    j-=1
                if j >= 0:
                  return False
            if t[j] == '?':
                  return solve(i-1,j-1)
            if t[j] == "*":
                  return solve(i-1,j-1) or solve(i-1,j)      
            if s[i]==t[j]:
                return solve(i-1,j-1) 
            else:
                return False
        # n,m=len(s),len(t)
n,m=len(s),len(t)
print(solve(n-1,m-1))

