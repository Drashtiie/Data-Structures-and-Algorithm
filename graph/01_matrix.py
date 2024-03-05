mat = [[0,0,0],[0,1,0],[1,1,1]]
v = [[-1 for x in range(len(mat[0]))]for y in range(len(mat))]
def bfs(i,j,d):
    v[i][j] = 0
    q = [[i,j,d]]
    while q:
        i,j,d = q[0]
        l1 = [1,0,-1,0]
        l2 = [0,1,0,-1]
        for x in range(4):
            i1 = i + l1[x]
            j1 = j + l2[x]
            if i1>=0 and i1 < len(mat) and j1>=0 and j1 < len(mat) and mat[i1][j1]!= 0:
                if v[i1][j1] == -1:
                    v[i1][j1] = d
                    q.append([i1,j1,d+1])
                else:
                    if d < v[i1][j1]:
                        q.append([i1,j1,d+1])
                    v[i1][j1] = min(d,v[i1][j1])
                
                print(q)
        q.pop(0)


q= []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            q.append([i,j,1])
for x in q:
    bfs(x[0],x[1],x[2])
print(v)