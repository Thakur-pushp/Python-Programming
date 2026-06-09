list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
l1,l2 = set(list1),set(list2)
temp = list(l1.intersection(l2))
res = {}
for i in temp:
    a = (list1.index(i)+list2.index(i))
    res[i] = a
minimum = min(res.values())
result = [key for key, val in res.items() if val == minimum]
print(result)
