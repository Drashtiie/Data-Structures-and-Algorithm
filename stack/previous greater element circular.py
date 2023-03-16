def nge(l):
        nums= l
        
        l=l+l
        ans=[]
        s=[]
        for i in range(len(l)):
            while len(s)>0 and s[-1] <= l[i]:
                s.pop()
            if len(s)==0:
                ans.append(-1)
            else:
                ans.append(s[-1])
            s.append(l[i])
      
        return ans[len(nums):]
        
print(nge([6,7,1,2,3,4,5,2]))
