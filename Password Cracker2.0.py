import getpass
import time
total = 1000000 
while True:
    password = getpass.getpass("Enter 6-digit password")

    if password.isdigit() and len(password)==6:
        break
    else:
        print("Invalid input, Enter 6 digits only")

for i in range(1000000):
    h = str(i).zfill(6)
   # Progress calculation
    progress = (i / total) * 100

    # Show progress every 50000 attempts
    if i % 50000 == 0:
        bar_length = 20
        filled = int(bar_length * i // total)
        bar = "█" * filled + "-" * (bar_length - filled)

        print(f"\r[{bar}] {progress:.2f}%", end="")
    if h == password:
        print("\nCracking Password...")
        time.sleep(1)
        print(f"{h} is your password")
        break