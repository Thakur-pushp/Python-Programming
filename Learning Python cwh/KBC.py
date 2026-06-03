name = input("Enter Your Name : ")
import time
t = time.strftime("%H")
if (int(t)<12):
    print("Good Morning", name)
elif(int(t)>12 and int(t)<16):
    print("Good Afternoon", name)
else:
    print("Good Evening", name)

money = 0

time.sleep(1)
print("Welcome to kaun banega Coropati!")
time.sleep(1)
print("Use a, b, c, or d (\"Only Small\") to answer")
time.sleep(1)

Question = [1,"Q Who came first?\na. Hen     b. Egg\nc. Pikachu     d. None of these",2,"Q Lagawelu jab lipstick hilela kaun sa district?\na. Ara     b. Munger\nc. Darbhanga     d. Motihari\n",3,"Q 2nd October ko Vijay aur uska pariwar kha gya tha?\na. Pune     b. Mumbai\nc. Panji     d.Murder kr rhe the\n"]
print (Question[1])
CA1 = "c"
CA2 = "a"
CA3 = "d"
time.sleep(1)
Ans1 = input()
if Ans1 != CA1:
    print("You Lost!\n Total Money Won ",money)
else:
    money += 10000000
    print("Correct Answer!\nTotal Money Won ",money)
    
    time.sleep(1)
    Ans2 = input(Question[3])
    if Ans2 != CA2:
        print("You Lost!\n Total Money Won ",money)
    else:
        money += 20000000
        print("Correct Answer!\nTotal Money Won ",money)
        
        time.sleep(1)
        Ans3 = input(Question[5])
        if Ans3 != CA3:
            print("You Lost!\n Total Money Won ",money)
        else:
            money += 30000000
            print("Correct Answer!\nTotal Money Won ",money)

time.sleep(1)            
print("Thankyou So Much",name, "for Playing KBC")
time.sleep(1)
print("Total Prize Money You Won ",money)