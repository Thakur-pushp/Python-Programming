while True:
    password = input("Enter your password(6 digits) ").zfill(6)

    if password.isdigit() and len(password)==6:
        break
    else:
        print("Invalid input, Enter 6 digits only")

for i in range(1000000):
    h = str(i).zfill(6)
    print(h)

    if h == password:
        print(f"{h} is your password")
        break
