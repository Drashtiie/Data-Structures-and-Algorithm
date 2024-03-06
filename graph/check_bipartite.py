V = 4
adj =[[2, 3], [3], [0, 3], [0, 1, 2]]
c = [ 0 for x in range(V)]
bp = 1
q = [0]
c[0] = 1
while q:
    x = q.pop(0)
    for t in adj[x]:
        print(t,c)
        if c[t] == c[x]:
            print(0)
        else:
            if c[t] == 0:
                q.append(t)
            c[t] = -1 * c[x]
            

print(1)