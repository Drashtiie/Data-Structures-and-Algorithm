def cs(n):
    if n == 1 or n == 0:
        return 1
    return cs(n-1) + cs(n-2)
print(cs(5))