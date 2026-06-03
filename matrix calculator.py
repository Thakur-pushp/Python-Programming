print("Matrix Calculator")
a11,a12,a21,a22 = int(input("a11= ")),int(input("a12= ")),int(input("a21= ")),int(input("a22= "))
b11,b12,b21,b22=int(input("b11= ")),int(input("b12= ")),int(input("b21= ")),int(input("b22= "))
print("What Operation do you want to Perform")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
O=int(input())
if O==1:
    print(f"The Sum of the given Matices is = {a11+b11}   {a12+b12}\n                                  {a21+b21}   {a22+b22}")
elif O==2:
    print(f"The Difference of the given Matices is = {a11-b11}   {a12-b12}\n                                         {a21-b21}   {a22-b22}")
elif O==3:
    print(f"The Product of the given Matices is = {a11*b11}   {a12*b12}\n                                      {a21*b21}   {a22*b22}")
elif O==4:
    print(f"The Division of the given Matices is = {a11/b11}   {a12/b12}\n                                       {a21/b21}   {a22/b22}")
