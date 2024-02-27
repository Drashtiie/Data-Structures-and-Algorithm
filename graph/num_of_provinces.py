V = 3
adj = [
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]
c = 0
v = [0 for x in range(V)]
def dfs(n):
            v[n] = 1
            for y in range(len(adj[n])):
                if adj[n][y] == 1 and v[y] == 0:
                    dfs(y)
                
for i in range(V):
            if v[i] == 0:
                c+=1
                dfs(i)
print(c)
