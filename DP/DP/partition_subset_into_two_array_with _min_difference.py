nums = [1,2,4,2]
s=sum(nums)

print(s)
def call(nums,s):

    
        s//=2
        dp = [[0 for x in range(s  + 1)] for y in range(len(nums)+1)]

        for y in range(len(nums)+1):
            dp[y][0] = 1
        for i in range(1,len(nums)+1):
            for j in range(1,s+ 1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        print(dp)

        t = dp[-1]
        for j in range(len(dp[-1])-1,0,-1):
             print(j)
             if dp[-1][j] > 0:
                  print(j)
                  return sum(nums) - 2 *j
             
             
        # return dp[len(nums)][s]   
print(call(nums,s))
                