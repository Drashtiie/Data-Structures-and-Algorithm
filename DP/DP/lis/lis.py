from bisect import bisect_left
nums = [10,9,2,5,3,7,101,18]
m = [[0 for y in range(len(nums) + 1)]for x in range(len(nums) + 1)]
ans = 0
for i in range(len(nums)-1,-1,-1):
    for j in range(i-1,-2,-1):

        if j == -1 or nums[i] > nums[j]:
            ans = max(ans,1+m[i+1][i+1])
        m[i][j+1] = ans
print("here,", m[0][0])

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
# dp

def lisdp(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
#  binary search optimizes time

def lis_binary(nums):
    s = [-100000]
    sl= 1
    for x in nums:
        if x>s[-1]:
            s.append(x)
            sl+=1
        else:
            print(s,x)
            t = bisect_left(s,x,1,len(s))
            print(t)
            s[t] = x
    return sl - 1
print(lis_binary(nums))
            
       