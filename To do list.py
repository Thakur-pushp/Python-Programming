todo = '''
--------------
  To Do List
--------------'''
print(todo)
T_1 = input("Enter task 1: ")
T_2 = input("Enter task 2: ")
T_3 = input("Enter task 3: ")
T_4 = input("Enter task 4: ")
T_5 = input("Enter task 5: ")
emp =[]
pending = [T_1,T_2,T_3,T_4,T_5]
while(True):
    print("Pending tasks")
    for i in pending:
        print(i)
    completed = input("Completed task: ")
    if (completed in pending) and (pending != emp):
        
        pending.remove(completed)
        
    else:
        print("error")
    if (pending == emp):
            print("Todays work is done")
            break