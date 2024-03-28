adj = []
            l=[]
            # print(alien_dict[0])
            x=0
            while x in range(N-1):
                i = 0
                # j = 0
                while i < len(alien_dict[x]) and i < len(alien_dict[x+1]) and alien_dict[x][i] == alien_dict[x+1][i]  :
                    i+=1
                adj.append([ord(alien_dict[x][i])-97 , ord(alien_dict[x+1][i])-97])
                x+=1
            # print(adj)
            adjm = [[] for x in range(K)]
            for t in adj:
                adjm[t[0]].append(t[1])
            i = [ 0  for x in range(K)]
            # print(adjm)
            for x in adjm:
                for t in x:
                    i[t] += 1
            # print(i)
            q=[]
            for g in range(K):
                if i[g] == 0:
                    q.append(g)
            s = []
            # print(q)
            while q:
                x = q[0]
                s.append(chr(x+97))
                
                for t in adjm[x]:
                    i[t] -= 1
                    if i[t] == 0:
                        q.append(t)
                        # print(q,"q")
                q.pop(0)
            
            return (s)