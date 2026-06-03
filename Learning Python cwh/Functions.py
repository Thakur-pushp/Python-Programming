# a = 9
# b = 4
# mean1=(a*b)/(a+b)
# print(mean1)

# c = 4
# d = 6
# mean2=(c*d)/(c+d)
# print(mean2)

#and so on for e,f,g,h,...

#or You can do is 

def calculatemean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if a>b:
        print("First Number is greater")
    elif a<b:
        print("Second Number is Greater")
    else:
        print("Both Number are same")
def islesser(a,b):
    pass #I'll Write the body later 


a = 9
b = 4
isgreater(a,b)
calculatemean(a,b)

c = 4
d = 6
isgreater(c,d)
calculatemean(c,d)

def name(fname, lname):
    print("Hello",fname,lname)


fname,lname = input("Enter Your First Name "),input("Enter your Last Name ")
name(fname,lname)