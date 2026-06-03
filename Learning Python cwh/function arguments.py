def average(a=9, b=1):#default value of a and b is 9 & 1 respectively
    print("The average is ", (a+b)/2)

average()#use the default value of a and b
average(4, 2)#replace value of a and b from 9 & 1 to 4 & 2 respectively
average(7)#replace value of a with 7, while a remains same. Can also be written as average(a=7)
average(b=7)#replace value of b with 7, while the a remains same.

def ave(*numbers):#touple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average is ", sum/len(numbers))


ave(5, 6, 5, 9)


def name(**name):#dictionary
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(fname = "Pushp", mname = "Raj", lname = "Thakur")