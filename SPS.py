print("Press\n1 for Stone\n2 for Paper\n3 for Scissors")
P=int(input("Enter Your Choise: "))
import random
C=random.randint(1,3)
if(P>0 and P<4):
    print(f"Your Choise {P},Computer's Choise {C}")
    if(C==1 and P==2 or C==2 and P==3 or C==3 and P==1):
     print("Congratulations! You Win:D")
    else:
        print("Alas! You Lost:(")
else:
    print("Error")