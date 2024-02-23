a = [1,2,3,4]
k = 4
def rec(a,k,cs,i):
    if cs == k:
        return True
    if i == -1:
        return False
    lr = rec(a, k, cs +a[i],i-1)
    rr = rec(a, k, cs,i-1)
    return lr or rr
print(rec(a,k,0,3))

