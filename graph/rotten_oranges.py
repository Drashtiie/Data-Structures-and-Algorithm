def ro(grid):     
        v=[[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        q=[]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append([x,y,0])
        mx = 0
        while q:
            x,y,t = q.pop(0)
            l1 = [0,0,-1,1]
            l2 = [-1,1,0,0]
            
            for g in range(4):
                x1 = x + l1[g]
                y1 = y +l2[g]
                if x1>=0 and y1>=0 and x1<len(grid) and y1<len(grid[0]) and grid[x1][y1] == 1 and v[x1][y1] == 0:
                    mx = max(mx, t+1)
                    q.append([x1,y1,t+1])
                    grid[x1][y1] = 2
                    v[x1][y1]=1
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return -1
        return mx

grid = [[2,1,1],[1,1,0],[0,1,0]]
print(ro(grid))      