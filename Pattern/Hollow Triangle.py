for i in range(1,9,1):
    for j in range(1,i+1):
        if (i>2 and i<8 and j>1 and j<i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()