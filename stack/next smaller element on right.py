def nse(l):
        nums= l
        
        
        ans=[]
        s=[]
        for i in range(len(l)-1,-1,-1):
            while len(s)>0 and s[-1] >= l[i]:
                s.pop()
            if len(s)==0:
                ans.append(-1)
            else:
                ans.append(s[-1])
            s.append(l[i])
        ans.reverse()
        return ans[:len(nums)]
        
print(nse([7,1,2,3,4,5,2]))
