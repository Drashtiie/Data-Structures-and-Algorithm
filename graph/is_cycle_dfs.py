# if you are reaching to same node again its cycle 
cycle = 0

v = 4
vis = [0 for x in range(v)]
p = [-1 for x in range(v)]
adj = [[], [2], [1, 3], [2]]

def iscycdfs(a):
    # nonlocal cycle
    # print(a,p,adj[a])
    vis[a] = 1
    for g in adj[a]:
        # print(a,p,adj[a],g,vis)
        if vis[g] == 1 and p[a] == g:
            pass
        elif vis[g] == 1:
            cycle = 1
            return
        else:
            p[g] = a
            iscycdfs(g)




for i in range(v):
    if vis[i] == 0:
        iscycdfs(i)
print(cycle)
