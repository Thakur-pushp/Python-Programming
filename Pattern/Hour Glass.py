for i in range(7):
    if i<4:
        for j in range(i):
            print(" ",end=" ")
        for k in range(4-i):
            print("* ",end=" ")
    else:
        for l in range(5,i-1,-1):
            print(" ",end=" ")
        for m in range(0,i-2,1):
            print("* ",end=" ")
    print()
