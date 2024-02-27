grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
v = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
c = 0
        
def dfs(x,y):
            print(x,y)
            v[x][y] = 1
            for t in range(-1,2):
                for u in range(-1,2):
                    x = x+t
                    y = y+u
                    if x >=0 and x < len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] == "1" and v[x][y] == 0:
                        dfs(x,y)
            
for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and v[i][j] == 0:
                    # print(i,j)
                    c+=1
                    dfs(i,j)
       
print(c)