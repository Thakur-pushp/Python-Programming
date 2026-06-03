#strings are immutable
a="!! Pushp !!! Pushp"
print(len(a))
print(a.rstrip("!"))
print(a.upper())
print(a.lower())
# these will make a copy (new string) of a insetead of changing a
# because strings are immutable means they can't be changed
print(a.replace("Pushp","Thakur Ji"))
print(a.split(" "))
# Creates list of the elements of string "a"
Heading="introduction tO PythoN"
print(Heading.capitalize())
str1="Welcome to Python!!"
print(str1.center(50))
print(a.count("Pushp"))
print(str1.endswith("!!"))
str2="He's name is Dan. He is an honest man"
print(str2.find("is"))
print(str2.find("ishh"))
# print(str2.index("ishh"))
print(str2.index("is"))
str3="WelcomeToPython"
print(str3.isalnum())#alphanumeric
print(str2.islower())
print(str2.isupper())
str4="Welcome To Python\n"
print(str4.isprintable())#"\n"is not a printable character
str5= "     "
print(str5.isspace())
print(str4.istitle())
print(str4.startswith("Welcome"))
print(str4.swapcase())
print(str2.title())
