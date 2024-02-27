n = 3
m = [-1 for x in range(n+1)]
def fun(n,a,l):
    print(n,a,l)
    if n < 0:
        return 0
    p0 = 0
    p1 = 0
    p2 = 0
    
    if l!= 0:
            p0 = a[n-1][0] + fun(n-2,a,0)
    if l!= 1:
            p1 = a[n-1][1] + fun(n-2,a,1)
    if l != 2:
        p2 = a[n-1][2] + fun(n-2,a,2)
    return max(p0,p1,p2)
    
print(fun(2,[[1,2,1],[2,1,1]], -1))   
print(fun(3,[[1,2,5],[3,1,1],[3,3,3]], -1))