from tkinter import *

timer = 5

def print_char(i):
    global timer
    print(i.char)
    window.after_cancel(timer)
    counter_down(5)

def counter_down(count):
    global timer
    if count > 0:
        global timer
        timer = window.after(1000,counter_down,count - 1)
        num.set(count)
    else:
        num.set("TIME OVER")
        text_1.delete("1.0","end")

#Window
window = Tk()
window.title("Writing text")
window.minsize(width=800,height=600)
window.config(padx=100, pady=50, bg='white')

num = StringVar()


text_1 = Text(window, height=20, width=60, font=("Arial",18,"normal"))
text_1.grid(column=1, row=2)

num_label = Label(window, textvariable=num, font=("Arial",24,"normal"))
num.set("5")
num_label.grid(column=1, row=4)

text_1.bind("<KeyPress>", lambda i : print_char(i))

counter_down(5)

window.mainloop()