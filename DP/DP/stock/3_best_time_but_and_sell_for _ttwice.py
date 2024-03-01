
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



#dp

prices = [7,1,5,3,6,4]
n = len(prices)
m = [[[-1 for z in range(3)] for x in range(2)] for y in range(len(prices) + 1)]

# print("here")
for i in range(n,-1,-1):
    for j in range(0,2):
        for k in range(0,3):
        # print(i,j)
            if k == 2:
                m[i][j][k] = 0
            elif i == n:
                m[i][j][k] = 0
            else:

                if j == 0:
                    b1 = m[i+1][1][k] - prices[i]
                    nb = m[i+1][0][k]
                    m[i][j][k] = max(b1,nb)
                else:
                    s1 = m[i+1][0][k+1] + prices[i]
                    ns = m[i+1][1][k]
                    m[i][j][k] = max(s1,ns)
print(m[0][0][0])