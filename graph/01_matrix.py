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



"""

 if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        queue = deque()
        MAX_VALUE = m * n
        
        # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1
        
        return mat



"""