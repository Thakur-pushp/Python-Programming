# dic = {
#     1: "monday",2:"tuesday",3:"Wednesday" 
# }

# print(dic[1]) 

info = {"name": "Karan","age":19,"eligiblity":True}
print(info)
# print(info['name2']) # It'll show an error becuse name2 don't exist
print(info.get('name2'))
print(info.keys())
print(info.values())
print(info.items())
print(str(info.keys()))