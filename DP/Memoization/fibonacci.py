n = 5
m = [-1 for x in range(n+1)]
def fib(n):
    print("cal fib")
    if n == 1 or n == 0:
        return n
    if m[n-1] != -1 and m[n-2] != -1:
        return m[n-1] + m[n-2]
        
    m[n] = fib(n-1) + fib(n-2)
    return m[n]

print(fib(5))