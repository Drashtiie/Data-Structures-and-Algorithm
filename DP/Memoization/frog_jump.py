n = 3
m = [-1 for x in range(n+1)]
def fj(a,arr):
    if a==0:
        return 0
    if m[a] != -1:
        return m[a]
    lr = fj(a-1,arr) +abs(arr[a] - arr[a-1])
    rr = 10000
    if a>1:
        rr = fj(a-2,arr) +abs(arr[a] - arr[a-2])
    m[a] = min(lr,rr)
    return m[a]

print(fj(3,[10,20,30,10]))