V = 5
E = 4
adj = [[1,2,3],[],[4],[],[]]
q = [0]
v = [0 for x in range(V)]
ans = []
while q:
    x = q.pop(0)
    v[x] = 1
    ans.append(x)
    for y in adj[x]:
        if v[y]!= 1:
            q.append(y)
print(ans)
    
