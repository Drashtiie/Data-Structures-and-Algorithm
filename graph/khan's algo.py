# basically toposort ,based bfs : use indegree

adj = [[],[],[3],[1],[0,1],[0,2]]
V = 5
i = [ 0  for x in range(V+1)]

for x in adj:
    for t in x:
        i[t] += 1
print(i)
q=[]
for g in range(V+1):
    if i[g] == 0:
        q.append(g)
s = []
print(q)
while q:
    x = q[0]
    s.append(x)
    for t in adj[x]:
        i[t] -= 1
        if i[t] == 0:
            q.append(t)
    q.pop(0)
print(s)
