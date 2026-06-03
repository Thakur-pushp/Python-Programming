import tkinter as tk
import random



root = tk.Tk()
root.title('BestFriend')
root.geometry('300x150')
root.configure(bg='pink')


question = tk.Label(root,text='Who is your best friend?',bg= 'pink',fg='white',font=('bold'))
question.pack()

ipbox = tk.Entry(root,bg='white',fg='black',relief= tk.RAISED,bd=5)
ipbox.pack(pady=5)

result = tk.Label(root,text='',bg='pink',fg='white',font=('bold'))
result.pack()

def answer():
    ans = ipbox.get().lower().strip()
    ipbox.delete(0, tk.END)
    per = random.randint(1,100)
    result.config(text=f'Friendship Percentage = {per}%')
    # if ans == 'pushp' or ans == 'pushp raj':
    #     result.config(text='You\'re also Pushp\'s bestfriend')
    # else:
    #     result.config(text="Change!")
    

btn = tk.Button(root,text='Check friendship',command=answer)
btn.pack()

root.mainloop()