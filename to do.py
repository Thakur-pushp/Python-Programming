print ('''
--------------
  To Do List
--------------''')


task = []
def add_task():
    print(f"Pending Task(s)",task)
    print("1. Add task\n2. remove task\n3. Completed task")
    a = int(input())
    if a == 1:
        work = input("Enter Task: ")
        task.append(work)
        return add_task()
    elif a==2:
        work = input("Enter Task: ")
        task.remove(work)
        return add_task()
    elif a==3:
        work = input("Enter Task: ")
        task.remove(work)
        return add_task()
    else:
        return 0    

x = add_task()
print(x)
