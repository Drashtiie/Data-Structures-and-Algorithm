prices = [7,1,5,3,6,4]
mx = 0
mn = 1000000
for i in prices:
    mx = max(mx, i - mn)
    mn = min(mn,i)
print(mx)