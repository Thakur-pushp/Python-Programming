menu={
    "Pizza":150,"Burger":100,"Coffee":50,"Tea":50
}

print("Welcome To Falana Cafe!")
print("What do you want to order?")
print("Pizza-----150\nBurger----100\nCoffee----50\nTea-------50")

total_amount=0
quantity=0
item_1=input("Order: ")
quantity=int(input("Quantity: "))

if item_1 in menu:
    total_amount+=menu[item_1]*quantity
    print(f"{item_1} added to your cart. Total bill = {total_amount}")
else:
    print(f"{item_1} is not avaialable in our menu")

another_order=input("Do want anyting else (Yes/No): ")

if another_order=="Yes":
    item_2= input("What do you want : ")
    quantity=int(input("Quantity: "))
    
    if item_2 in menu:
        total_amount+=menu[item_2]*quantity
        print(f"{item_2} added to your cart. Total bill = {total_amount}")
    else:
        print(f"{item_2} is not avaialable in our menu")

else:
    print("Its Ok! Please visit again")



print(f"Your Cart is Full. Your Total Bill is {total_amount}")


print("Thankyou for odering!")
