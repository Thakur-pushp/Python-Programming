import tkinter as tk
import random
import time



l = {1:'Stone',2:'Paper',3:'Scissors'}
user_score = 0
comp_score = 0



root = tk.Tk()
root.title('Stone Paper Scissors')
root.geometry('400x400')
root.configure(bg='#212121')
root.grid_columnconfigure((0,1,2), weight=1,uniform='equal')




game = tk.Label(text='Stone Paper Scissors',bg='#212121',fg='white',font=('Arial',16,'bold'))
game.grid(row=0,column=0,columnspan=3,pady=20)

you = tk.Label(text='You:',bg='#212121',fg='white',font=('Arial',12,'bold'))
you.grid(row=1,column=0,pady=10)

choise = tk.Entry(root,relief=tk.RAISED,bd=5, state='readonly', readonlybackground='white')
choise.grid(row=1,column=1,columnspan=2)

computer = tk.Label(text='Computer:',bg='#212121',fg='white',font=('Arial',12,'bold'))
computer.grid(row=2,column=0,pady=10)

choisecomp = tk.Entry(root,relief=tk.RAISED,bd=5, state='readonly', readonlybackground='white')
choisecomp.grid(row=2,column=1,columnspan=2)

result = tk.Label(text='',bg='#212121',font=('Arial',18,'bold'),relief=tk.RAISED,bd=10,width=20)
result.grid(row=4,column=0,columnspan=3,pady=10)

user = tk.Label(text='You:',bg='#212121',fg= 'white',font=('Arial',10,'bold'))
user.grid(row=5,column=0,pady=5)
uscore = tk.Entry(root,relief=tk.RAISED,bd=5, state='readonly', readonlybackground='white')
uscore.grid(row=5,column=1,columnspan=2)

cpu = tk.Label(text='Computer:',bg='#212121',fg= 'white',font=('Arial',10,'bold'))
cpu.grid(row=6,column=0,pady=5)
cscore = tk.Entry(root,relief=tk.RAISED,bd=5, state='readonly', readonlybackground='white')
cscore.grid(row=6,column=1,columnspan=2)



def res(x):
    choise.config(state='normal')
    choisecomp.config(state='normal')

    choise.delete(0,tk.END)
    choise.insert(0,x)
    choisecomp.delete(0, tk.END)
    a = random.randint(1,3)
    choisecomp.insert(0,l[a])

    choise.config(state='readonly')
    choisecomp.config(state='readonly')

    if x == l[a]:
        result.config(text="It's a Tie!",bg='#BB86FC', fg="yellow")
    elif (x == 'Stone' and l[a] == 'Scissors') or \
         (x == 'Paper' and l[a] == 'Stone') or \
         (x == 'Scissors' and l[a] == 'Paper'):
        result.config(text="You Win! 🎉",bg='#BB86FC', fg="darkgreen")
        global user_score
        user_score += 1
        uscore.config(state='normal')
        uscore.delete(0,tk.END)
        uscore.insert(0,user_score)
        uscore.config(state='readonly')

    else:
        result.config(text="Computer Wins! 💀",bg='#BB86FC', fg="red")
        global comp_score
        comp_score += 1
        cscore.config(state='normal')
        cscore.delete(0,tk.END)
        cscore.insert(0,comp_score)
        cscore.config(state='readonly')

    if user_score == 5:
        result.config(text="Victory!", bg='#212121', fg="#FFD813")
        reset_game()
    if comp_score == 5:
        result.config(text="LOOSE!", bg='#212121', fg="#FF1313")
        reset_game()


btn1 = tk.Button(root,text='Stone',bg='#00ADB5',relief=tk.RAISED,bd=3,command=lambda : res('Stone'))
btn1.grid(row=3,column=0,pady=20)

btn2 = tk.Button(root,text='Paper',bg='#00ADB5',relief=tk.RAISED,bd=3,command=lambda : res('Paper'))
btn2.grid(row=3,column=1,pady=20)

btn3 = tk.Button(root,text='Scissors',bg='#00ADB5',relief=tk.RAISED,bd=3,command=lambda : res('Scissors'))
btn3.grid(row=3,column=2,pady=20)

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    
    for entry in [uscore, cscore, choise, choisecomp]:
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.config(state='readonly')
        
    result.config(text="Game Reset!", bg='#212121', fg="white")

reset_btn = tk.Button(root, text='Reset Game', bg='#FF4C4C', fg='white', command=reset_game)
reset_btn.grid(row=7, column=0, columnspan=3, pady=10)









root.mainloop()