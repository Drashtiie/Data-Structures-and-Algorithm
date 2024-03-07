# only possible in directed acycic graphs
# if there is an edge bet u and v, u appears in sort befor v
# dfs
adj = [[],[],[3],[1],[0,1],[0,2]]
V = 5
v= [0 for x in range(V+1)]
s= []
def dfs(x):
    print(x)
    v[x] = 1
    for t in adj[x]:
        if v[t]==0:
            dfs(t)

    s.append(x)
    print(s)

for i in range(V+1):
    if v[i] == 0:
        dfs(i)
print(s)