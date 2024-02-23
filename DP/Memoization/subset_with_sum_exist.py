arr = [3 ,34, 4, 12, 5, 2]
k = 30
N = len(arr)
m = [[-1 for x in range(N+1)]for x in range(sum+1)]
def rec(t,i):
            if t == 0:
                return 1
            if i == -1:
                return 0
            if m[t][i] != -1:
                return m[t][i]
            lr = 0
            if arr[i] <= t:
                lr = rec(t - arr[i],i-1)
            rr = rec(t,i-1)
            m[t][i] = lr or rr
            return lr or rr
print( rec(k,len(arr)-1))
        



