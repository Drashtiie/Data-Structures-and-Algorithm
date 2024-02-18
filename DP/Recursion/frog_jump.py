def fj(a,arr):
    if a==0:
        return 0
    lr = fj(a-1,arr) +abs(arr[a] - arr[a-1])
    rr = 10000
    if a>1:
        rr = fj(a-2,arr) +abs(arr[a] - arr[a-2])
    return min(lr,rr)

print(fj(3,[10,20,30,10]))