ops = ["5","-2","4","C","D","9","+","+"]
record = []
for i in ops:
    if i == 'C':
        record.pop()
    elif i == 'D':
        record.append(2*(record[-1]))
    elif i == '+':
        record.append(record[-1]+record[-2])
    else:
        record.append(int(i))
print(sum(record))
