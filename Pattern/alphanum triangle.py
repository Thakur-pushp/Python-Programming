for i in range (5):
    for j in range(i):
        if i%2==0:
            print(chr(j+65),end="")
        else:
            print(i,end="")
    print()