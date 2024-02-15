def sub(a,arr):
    print(a,arr)
    if a == 0:
        return 0
    if a < 0:
        return 0
    print(arr[a-1])
    p1 = arr[a-1] + sub(a-2,arr)
    np = sub(a-1,arr)
    print(p1,np)
    return max(p1,np)
print(sub(4,[2,1,4,9]))