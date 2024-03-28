def leveloredr(root):
    q=[]
    q.append([root, 0 ])
    ans=[]
    while len(q) > 0:
        x=q[0][0]
        y=q[0][1]
        if x!= None:
            if len(ans) > y:
                ans[y].append(x.val)
            else:
                ans.append( [x.val] )
            #ans.append(x.val)
            #print(ans)
            if x.left!=None:
                q.append([x.left, y+1])
            if x.right!=None:
                q.append([x.right,y+1])
        q.pop(0)
        #print("q =",q)
    return ans