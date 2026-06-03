nums = [1,1,0,1,1,1]
temp = []
count = 0
for i in nums:
    if i == 0 :
        temp += [count]
        count = 0
    else:
        count += 1
temp += [count]
print(max(temp))