i = int(input("Enter Number "))
j = str(i)
num = i 
sum = 0

while num > 0:
    digit = num%10
    sum += digit ** len(j)
    num //= 10

if sum == i:
    print("It is an Armstron Number")
else:
    print("It's not an Armstrong Number")