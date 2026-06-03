import time
import sys

password = input("Enter 6-digit password: ")

total = 1000000

for i in range(total):
    guess = str(i).zfill(6)

    # Progress calculation
    progress = (i / total) * 100

    # Show progress every 50000 attempts
    if i % 50000 == 0:
        bar_length = 20
        filled = int(bar_length * i // total)
        bar = "█" * filled + "-" * (bar_length - filled)

        print(f"\r[{bar}] {progress:.2f}%", end="")

    if guess == password:
        print("\nCracking password...")
        time.sleep(1)
        print(f"Password found: {guess}")
        print(f"Attempts: {i}")
        break