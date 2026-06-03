import tkinter as tk

root = tk.Tk()
root.title('CGPA Calculator')
root.geometry('300x400')
root.configure(bg= "#1E293B")
root.grid_columnconfigure((0,1,2,3), weight=1,uniform='equal')
root.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1,uniform='equal')

head = tk.Label(text='CGPA Calculator',font=("Segoe UI",20,'bold'),relief='ridge',bg= "#1E293B",fg= "#ffffff")
head.grid(row= 0, column= 0,columnspan=4,pady=2)

first_Sem = tk.Label(text='1st Sem:',font=('Segoe UI',10,'bold'),bg="#1E293B",fg="#F8FAFC")
first_Sem.grid(row=2,column=0,padx=5)

sem1 = tk.Entry(root,relief='sunken',bd=3,bg = "#334155",fg="#F8FAFC")
sem1.grid(row=2,column=1,columnspan=2)


Second_Sem = tk.Label(text='2nd Sem:',font=('Segoe UI',10,'bold'),bg="#1E293B",fg="#F8FAFC")
Second_Sem.grid(row=3,column=0,padx=5)

sem2 = tk.Entry(root,relief='sunken',bd=3,bg = "#334155",fg="#F8FAFC")
sem2.grid(row=3,column=1,columnspan=2)


cgpa = tk.Label(text='CGPA',font=('Segoe UI',18,'bold'),bg="#1E293B",fg="#F8FAFC")
cgpa.grid(row= 4, column= 1,columnspan=2,pady=2)

cgpares = tk.Entry(root,relief='sunken',bd=3,readonlybackground= "#334155",fg="#F8FAFC")
cgpares.grid(row=5,column=1,columnspan=2)
cgpares.config(state='readonly')


def calculate():
    try:
        fsem,ssem = sem1.get(),sem2.get()
        sem1.delete(0,tk.END)
        sem2.delete(0,tk.END)
        answer = (float(fsem) + float(ssem))/2
        cgpares.config(state='normal')
        cgpares.delete(0,tk.END)
        cgpares.insert(0,f'{answer:.2f}')
        cgpares.config(state='readonly')
    except:
        cgpares.config(state='normal')
        cgpares.delete(0,tk.END)
        cgpares.insert(0,'ERROR')
        cgpares.config(state='readonly')






btn = tk.Button(text= 'Calculate',bg="#3B82F6",fg="#F8FAFC",cursor='hand2',relief='groove',bd=3,command=calculate)
btn.grid(row=6, column=1,columnspan=2)



root.mainloop()