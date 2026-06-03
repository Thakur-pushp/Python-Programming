from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg='black')



mainscreen = Entry(root,width=40,bg='lightblue',relief=RAISED,bd=5)
mainscreen.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def button_click(number):
    current = mainscreen.get()
    mainscreen.delete(0, END)
    mainscreen.insert(0, str(current) + str(number))
def clear_screen():
    mainscreen.delete(0, END)

def calculate():
    try:
        result = eval(mainscreen.get()) 
        mainscreen.delete(0, END)
        mainscreen.insert(0, result)
    except:
        mainscreen.delete(0, END)
        mainscreen.insert(0, "Error")

def backspace():
    length = len(mainscreen.get())
    mainscreen.delete(length-1,END)

def squareroot():
    try:
        current = mainscreen.get()
        num = float(current)
        sqrt = num ** 0.5
        mainscreen.delete(0,END)
        mainscreen.insert(0,sqrt)
    except:
        mainscreen.delete(0,END)
        mainscreen.insert(0,"ERROR")


def square():
    try:
        current = mainscreen.get()
        num = float(current)
        sqrt = num ** 2
        mainscreen.delete(0,END)
        mainscreen.insert(0,sqrt)
    except:
        mainscreen.delete(0,END)
        mainscreen.insert(0,"ERROR")

btn1 = Button(root,text='1',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(1))
btn1.grid(row=1,column=0,pady=5)
btn2 = Button(root,text='2',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(2))
btn2.grid(row=1,column=1,pady=5)
btn3 = Button(root,text='3',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(3))
btn3.grid(row=1,column=2,padx= 5,pady=5)
btnplus = Button(root,text='+',height=2,width=5,bg='orange',relief=RAISED,bd=3,command=lambda: button_click('+'))
btnplus.grid(row=1,column=3,padx= 5,pady=5)

btn4 = Button(root,text='4',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(4))
btn4.grid(row=2,column=0,pady=5)
btn5 = Button(root,text='5',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(5))
btn5.grid(row=2,column=1,pady=5)
btn6 = Button(root,text='6',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(6))
btn6.grid(row=2,column=2,padx= 5,pady=5)
btnminus = Button(root,text='-',height=2,width=5,bg='orange',relief=RAISED,bd=3,command=lambda: button_click('-'))
btnminus.grid(row=2,column=3,padx= 5,pady=5)

btn7 = Button(root,text='7',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(7))
btn7.grid(row=3,column=0,pady=5)
btn8 = Button(root,text='8',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(8))
btn8.grid(row=3,column=1,pady=5)
btn9 = Button(root,text='9',height=2,width=5,bg="grey",fg='white',relief=RAISED,bd=3,command=lambda: button_click(9))
btn9.grid(row=3,column=2,padx= 5,pady=5)
btnmul = Button(root,text='*',height=2,width=5,bg='orange',command=lambda: button_click('*'))
btnmul.grid(row=3,column=3,padx= 5,pady=5)

btnc = Button(root,text='AC',height=2,width=5,bg= 'red',relief=RAISED,bd=3,command=clear_screen)
btnc.grid(row=4,column=0,pady=5)
btn0 = Button(root,text='0',height=2,width=5,bg="grey",relief=RAISED,bd=3,fg='white',command=lambda: button_click(0))
btn0.grid(row=4,column=1,pady=5)
btneq = Button(root,text='=',height=2,width=5,bg= 'lightgreen',relief=RAISED,bd=3,command=calculate)
btneq.grid(row=4,column=2,padx= 5,pady=5)
btndiv = Button(root,text='/',height=2,width=5,bg='orange',relief=RAISED,bd=3,command=lambda: button_click('/'))
btndiv.grid(row=4,column=3,padx= 5,pady=5)

btndel = Button(root,text='C',height=2,width=10,bg= 'red',relief=RAISED,bd=3,command=backspace)
btndel.grid(row= 5,column=0,columnspan=2,padx=5,pady=5)

btnroot = Button(root,text='√',height=2,width=5,bg='orange',relief=RAISED,bd=3,command= squareroot)
btnroot.grid(row= 5,column=3,padx=5,pady=5)

btnsquare = Button(root,text="x²",height=2,width=5,bg='orange',relief=RAISED,bd=3,command= square)
btnsquare.grid(row=5,column= 2,columnspan=1,padx=5,pady=5)

# watermark = Label(root,text="Pushp ka Calculator",bg='black',fg='white',font=('Arial',18,"bold"))
# watermark.grid(row=,column=0,columnspan=4,pady=10)

root.mainloop()