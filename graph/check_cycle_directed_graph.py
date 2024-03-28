
#  take two arrays vis and path visis
adj = [[1], [3, 0], [0], [1]]
V = 4
v = [0 for x in range(V)]
py = [0 for x in range(V)]
print(adj)
cyc = 0
# def callbfs(x):
#     global cyc
#     q = [x]
#     print(x,v)
#     while q:
#         t = q.pop(0)
#         for y in adj[t]:
#             print(y)
#             if v[y] == 1:
#                 print(y,t,v,"here")
#                 cyc = 1
#             else:
#                 v[y] = 1
#                 q.append(y)
#     print(v)    
    
# for x in range(V):
#     if v[x] == 0:
       
#         calldfs(x)

def cycdfs(x):
    global cyc
    v[x] = 1
    py[x] = 1
    for y in adj[x]:
        if v[y] == 0 and py[y] == 1:
            cyc = 1
            break
        if v[y] == 0 and py[y] == 0:
            v[y] = 1
            py[y] = 1
            cycdfs(y)
            py[y] = 0
    py[x] = 0
        
print(cyc)