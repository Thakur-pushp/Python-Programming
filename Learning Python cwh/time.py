import time
timestamp= time.strftime("%H")
if (int(timestamp)<12):
    print("Good Morning Sir!")
elif(int(timestamp)>12 and int(timestamp)<16):
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")