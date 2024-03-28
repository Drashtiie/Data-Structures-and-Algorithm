grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
v = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
c = 0
        
def dfs(x,y):
            # print(x,y)
            v[x][y] = 1
            l1 = [1,0,-1,0]
            l2 = [0,1,0,-1]
            for t in range(4):
                
                    x1 = x+l1[t]
                    y1 = y+l2[t]
                    print(x,y)
                    if x1 >=0 and x1 < len(grid) and y1>=0 and y1<len(grid[0]) and v[x1][y1] == 0:
                        if grid[x1][y1] == "1" :
                            print(v)
                            dfs(x1,y1)
                            
                        # else:
                        #        v[x][y] = 1
            
for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i,j,v)
                if grid[i][j] == "1" and v[i][j] == 0:
                    print(i,j)
                    c+=1
                    dfs(i,j)
       
print(c)