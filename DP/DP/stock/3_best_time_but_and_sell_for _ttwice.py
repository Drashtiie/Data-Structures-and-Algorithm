
prices = [3,3,5,0,0,3,1,4]
m = [[[-1 for x in range(3)] for y in range(2)] for z in range(len(prices)+ 1)]
# print(m )
def rec(i,b,t):
    if t==0:
        return 0
    if i == len(prices):
        return 0
    if m[i][b][t] != -1:
        return m[i][b][t]
    
    else:
        print(i,b,t)
        if b == 0:
            b1 = rec(i+1,1,t) - prices[i]
            nb = rec(i+1,0,t)
            m[i][b][t] = max(b1,nb)
            return m[i][b][t]
        else:
            s1 = rec(i+1,0,t-1) + prices[i]
            ns = rec(i+1,1,t)
            m[i][b][t] =  max(s1,ns)
            return m[i][b][t]
print(rec(0,0,2))

#memoization


prices = [7,1,5,3,6,4]
m = [[-1 for x in range(2)] for y in range(len(prices) + 1)]
def rec(i,b):
    if i == len(prices):
        return 0
    if m[i][b] != -1:
        return m[i][b]
    else:
        if b == 0:
            b1 = rec(i+1,1) - prices[i]
            nb = rec(i+1,0)
            m[i][b] = max(b1,nb)
            return m[i][b]
        else:
            s1 = rec(i+1,0) + prices[i]
            ns = rec(i+1,1)
            m[i][b] = max(s1,ns)
            return m[i][b]
print(rec(0,0))
