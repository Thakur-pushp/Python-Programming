

tasks = []
menu = '''
1. Show Tasks
2. Add Tasks
3. Mark Tasks as Completed
4. Delete Task
5. Exit
'''
while(True):
    menuinput = int(input(f"{menu}\n"))
    if menuinput == 1:
        # for index, task in enumerate(task, start=1):
        #     print(f"{index}.{task['Task']}{status}")
        i = 1
        for task in tasks:
            status = "✓" if task["Done"] else"✕"
            print('     YOUR TASKS\n--------------------------------')
            print(f"{i}. {task["Task"]} [{status}]")
            i += 1
    elif menuinput == 2:
        work = input("Enter Task: ")
        task1 = {
            "Task":work,
            "Done":False
        }
        tasks.append(task1)
    elif menuinput == 3:
        com = int(input("Enter Task no.: "))
        tasks[com - 1]["Done"] = True
    elif menuinput == 4:
        rem = int(input("Enter Task No.: "))
        tasks.pop(rem - 1)
    elif menuinput == 5:
        print("Exiting...")
        break



