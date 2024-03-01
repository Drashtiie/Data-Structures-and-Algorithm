
#recursion

prices = [7,1,5,3,6,4]
# m = [[-1 for x in range(len(prices))] for y in range(2)]
def rec(i,b):
    if i == len(prices):
        return 0
    
    else:
        if b == 0:
            b1 = rec(i+1,1) - prices[i]
            nb = rec(i+1,0)
            return max(b1,nb)
        else:
            s1 = rec(i+1,0) + prices[i]
            ns = rec(i+1,1)
            return max(s1,ns)
print(rec(0,0))

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


#dp
prices = [7,1,5,3,6,4]
n = len(prices)
m = [[-1 for x in range(2)] for y in range(len(prices) + 1)]
m[n][0] = m[n][1] = 0
# print("here")
for i in range(n-1,-1,-1):
    for j in range(0,2):
        # print(i,j)
        if j == 0:
            b1 = m[i+1][1]  - prices[i]
            nb = m[i+1][0]
            m[i][j] = max(b1,nb)
        else:
            s1 = m[i+1][0] + prices[i]
            ns = m[i+1][1]
            m[i][j] = max(s1,ns)
print(m[0][0])



#another solution:

h,nh = -float('inf'), 0
for x in prices:
    ph,pnh= h,nh
    h = max(ph, pnh - x)
    nh = max(pnh, ph + x)
print (nh)