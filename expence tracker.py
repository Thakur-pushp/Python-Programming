expences = []

menu = '''
1. Add expense
2. Show expenses
3. Show total
4. Category-wise total
5. Exit
'''
while (True):
    try:
        menuinput = int(input(f"{menu}\nChoose Option: "))
    except:
        print("Invalid input")
        continue
    if menuinput == 1:
        try:
            addex = int(input("Enter Expend money: "))
        except:
            print("Invalid Input")
            continue
        cat = input("Enter Expend Catagory: ").strip().lower().isalpha()
        add = {
            "Expence" : addex,
            "Catagory" : cat
        }
        expences.append(add)

    elif menuinput == 2:
        print("\n___________________________\n     YOUR EXPENCE(S)\n___________________________")
        if not expences:
            print("No Expence(s) available")
        else:
            i = 1
            for expence in expences:
                print(f"{i}. {expence['Expence']} | {expence['Catagory']}")
                i += 1

    elif menuinput == 3:
        a = 0
        for expence in expences: 
            a = a+expence['Expence'] 
        print (f"Total Expence = Rs.{a}") 

    elif menuinput == 4:
        total = {}
        for expence in expences:
            catagory = expence['Catagory']
            amount = expence['Expence']
            if catagory in total:
                total[catagory] += amount
            else:
                total[catagory] = amount
        for catagory,amount in total.items():
            print(f'{catagory} {amount}')
    elif menuinput == 5:
        print("Exiting.........") 
        break

    else:
        print("Error⌀")

