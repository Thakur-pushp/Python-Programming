import tkinter as tk

tasks = []

def update_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["Done"] else "✕"
        listbox.insert(tk.END, f"{i}. {task['Task']}  [{status}]")

def add_task():
    work = entry.get().strip()
    if work:
        tasks.append({"Task": work, "Done": False})
        entry.delete(0, tk.END)
        update_list()

def complete_task():
    try:
        index = listbox.curselection()[0]
        tasks[index]["Done"] = True
        update_list()
    except:
        print("Select a task")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_list()
    except:
        print("Select a task")

# Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Input field
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Complete Task", command=complete_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

# Task display
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

root.mainloop()