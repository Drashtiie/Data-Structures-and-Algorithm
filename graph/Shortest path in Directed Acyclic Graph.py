# toposort and relax weights
#N :num of vertices
N = 6
M = 7
edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
 # M : num of edges
 #N :num of vertices
adj = [[] for x in range(N)]
for i in edge:

        adj[i[0]].append([i[1],i[2]])
   
v = [0 ]* N
s=[]
def dfs(t):
        v[t] = 1
        for d in adj[t]:
                if v[d[0]] == 0:
                        dfs(d[0])
        s.append(t)

for t in range(N):
        if v[t] == 0:
                dfs(t)

ans  = [1000000000]*N
ans[0] = 0
i = N
while i >0:
        if s[-1] != 0:
                ans[s[-1]] = -1
                s.pop(-1)
        i-=1


print(v,s)