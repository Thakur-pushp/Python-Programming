letter = "Hi my name is {} and I am from {}"
country = "India"
name = "Pushp"
print (letter.format(name, country))

print(f"Hi my name is {name} and I am from {country}")
print(f"We use f strings like this: Hi my name is {{name}} and I am from {{country}}")

price = 49.0999999
print(f"For only {price: .2f} dollars")