num = 0
digits = [1,2,3]
final =[]
for i in digits:
    num = (num * 10)+i
num += 1
temp = str(num)
for i in temp:
    final+=[int(i)] 
print(final)