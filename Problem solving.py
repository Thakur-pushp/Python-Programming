amount=int(input("Enter value (must be>100) "))
amount-=100
r_2000=amount//2000
amount%=2000
r_500=amount//500
amount%=500
r_100=(amount//100)+1
print(f"Rs.2000 Notes= {r_2000}\nRs.500 Notes= {r_500}\nRs.100 Notes= {r_100}")