V = 5 
adj = [[2,3,1] , [0], [0,4], [0], [2]]

ans = []
v = [0 for x in range(V)]
def dfs(n):
    ans.append(n)
    v[n] = 1
    for t in adj[n]:
        print(t)
        if v[t] == 0:
            print(t)
            dfs(t)
dfs(0)
print(ans)


