for i in range(9):
    if i<5:
        for j in range(5-i):
            print(" ",end=" ")
        for k in range(i):
            print("* ",end=" ")
        print()
    else:
        for j in range(i-4):
            print(" ",end=" ")
        for k in range(9-i):
            print("* ",end=" ")
        print()

        
    
