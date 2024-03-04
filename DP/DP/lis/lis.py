nums = [10,9,2,5,3,7,101,18]
m = [[-1 for y in range(len(nums) + 1)]for x in range(len(nums))]
for i in range(len(nums)+1):
    m[i][0] = 0
    m[0][i] = 0
for i in range(1,len(nums)+1):
    for j in range(1,len(nums)+1):
        pass

def rec(i,lp):
    if i <0 :
        return 0
    p = 0
    if lp == -1:
        p = rec(i-1,i-1) + 1
    if m[i][lp] != -1:
        return m[i][lp]
    elif nums[i-1] < nums[lp]:
        p = rec(i-1, i)+1
    np = rec(i-1,lp) 
    m[i][lp] = max(p,np)
    return m[i][lp]
print(rec(len(nums),-1))
