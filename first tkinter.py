import tkinter as tk

window = tk.Tk()
window.title("Mera pahla code")
window.geometry('400x300')

mytext = tk.Label(window, text = "Shri Radhavallabh Lal ki",fg="blue",font=('Arial',12,'bold'))
mytext.pack(pady=20)

ipbox = tk.Entry()
ipbox.pack()


result_label = tk.Label(window, text="", fg="red", font=("Arial", 12, "bold"))
result_label.pack(pady=20)


def alpha():
    jaikara = ipbox.get()
    result_label.config(text=f'Shri Radhavallabh lal ki {jaikara}')

button = tk.Button(window, text="Click here",command=alpha)
button.pack()

window.mainloop()