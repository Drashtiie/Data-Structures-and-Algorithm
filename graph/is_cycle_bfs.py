def dfscycle(V,adj):
    p = [-1 for x in range(V)]
    v = [0 for x in range(V)]
    # q = [0]
    cycle = 0
    def bfs(q):
        nonlocal cycle
        # t = q[0]
        
        print(q,"p1")
        while q:
            t = q[0]
            v[t] = 1
            print(adj[t])
            for x in adj[t]:
                print(x)
                if v[x] == 0:
                    # v[x] = 1
                    p[x] = t
                    q.append(x)
                    print(q)
                    # q.pop(0)
                elif v[x] == 1 and p[t] == x:
                    pass
                else:
                    print(cycle)
                    cycle = 1
                    return 
                    
                    break
            q.pop(0)
        return 
                
    for x in range(V):
            if v[x] == 0:
                bfs([x])
    return cycle
print(dfscycle(4,[[],[2],[1,3],[2]]))

