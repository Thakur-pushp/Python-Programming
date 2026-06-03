# tup = (1, 5, 4, 6)
# print(type(tup))

# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])

# print(tup[1:4]) #tuple slicing


countries = ("India","Spain","Japan","England")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[1]="France"
countries = tuple(temp)
print(countries)