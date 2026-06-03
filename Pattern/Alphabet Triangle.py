# for i in range(5):
#     for j in range(i):
#         print(chr(65+i-1),end="")
#     print()

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(chr(j+64),end="")
    print()