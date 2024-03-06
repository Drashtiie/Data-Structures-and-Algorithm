

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

n = len(grid[0])
m = len(grid)
v = [[0 for x in range(n)] for y in range(m)]
q=[]
c = 0
t = 0
for x in grid:
    t += sum(x)
for i in range(m):
    if grid[i][0] == 1 and v[i][0] == 0:
        v[i][0] = 1
        q.append([i,0])
        c+=1
    if grid[i][n-1] == 1 and v[i][n-1] == 0:
        v[i][n-1] = 1
        q.append([i,n-1])
        c+=1
for j in range(n):
    if grid[0][j] == 1 and v[0][j] == 0:
        v[0][j] = 1
        q.append([0,j])
        c+=1
    if grid[m-1][j] == 1 and v[m-1][j] == 0:
        v[m-1][j] = 1
        q.append([m-1,j])
        c+=1

while q:
        x,y = q.pop(0)
        # print(x,y)
        v[x][y] = 1
        l1 = [-1,0,1,0]
        l2= [0,-1,0,1]
        for i in range(4):
            x1 = x + l1[i]
            y1 = y + l2[i]
            # print(x1,y1)
            if x1 > 0 and y1>0 and x1<m-1 and y1<n-1 and grid[x1][y1] == 1 and v[x1][y1] == 0:
                
                q.append([x1,y1])
                v[x1][y1] = 1
                c+=1


                

print(t - c)