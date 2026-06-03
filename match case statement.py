#Its just like Switch Case in C
#break statement isn't necessary
i=int(input("Enter the value of i: "))
match i:
    case 0:#if i=0
        print("i is 0")
    case 4:#if i=4
        print("i is 4") 
    case _ if i!=90 :#case  with if-condition
        print(i,"is not 90")
    case _:#default case
        print(f"i is {i}")
