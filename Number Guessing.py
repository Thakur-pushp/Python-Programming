import time
print("____________________\nNUMBER GUESSING GAME\n____________________")
time.sleep(1)
start=int(input("press 1. Play\n      2. Exit   => "))
time.sleep(1)
if start==2:
    print("Exiting...")
    time.sleep(1)
elif start==1:
    print("Starting...")
    time.sleep(1)
    import random
    num=random.randint(1,100)
    print("Hey! Guess the number I have thought between 1 - 100")
    time.sleep(1)
    if(num>50):
        print("Hint! Number is Greater than 50")
        time.sleep(1)
    else:
        print("Hint! Number is less than 50")
        time.sleep(1)

    attempt=1
    max_guess=5
    while attempt<=max_guess:   
        guess=int(input(f"Guess the NO. Attempt ( {attempt}/{max_guess} ) - "))
        
    
        if num>guess:
            print("Try Higher!")
        elif num<guess:
            print("Try Lower!")
        else:
            print("Gottcha!")
            break
        attempt+=1
    else:
        print("Out of attempts! the Number was ",num)      
else:
    print("Error!")