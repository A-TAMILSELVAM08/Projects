from tkinter import *
def click(num):
    ip = t.get()
    t.delete(0, END)
    t.insert(0, str(ip)+str(num))
    return
def add():
    x = t.get()
    global a
    global math
    math ="addition"
    a = int(x)
    t.delete(0,END)
    return
def sub():
    x = t.get()
    global a
    global math
    a = int(x)
    math = "subtraction"
    t.delete(0, END)
    return
def mul():
    x = t.get()
    global a
    global math
    a = int(x)
    math = "multiplication"
    t.delete(0, END)
    return
def divid():
    x = t.get()
    global a
    global math
    a = int(x)
    math = "division"
    t.delete(0, END)
    return
def clear():
    t.delete(0, END)
    return
def equal():
    y = t.get()
    b = int(y)
    t.delete(0, END)
    if math == "addition":
        t.insert(0, a + b)
    elif math == "subtraction":
        t.insert(0, a - b)
    elif math == "multiplication":
        t.insert(0, a * b)
    elif math == "division":
        t.insert(0, a / b)
    return


root = Tk()
root.title("calculator-TS")
t = Entry(root,width=50)
t.grid(row=0, column=0, columnspan=4, padx=5, pady=10)
button_1 = Button(root, text=1, bg="gray", padx=60, pady=30,command=lambda: click(1))
button_2 = Button(root, text=2, bg="gray", padx=60, pady=30,command=lambda: click(2))
button_3 = Button(root, text=3, bg="gray", padx=60, pady=30,command=lambda: click(3))
button_4 = Button(root, text=4, bg="gray", padx=60, pady=30,command=lambda: click(4))
button_5 = Button(root, text=5, bg="gray", padx=60, pady=30,command=lambda: click(5))
button_6 = Button(root, text=6, bg="gray", padx=60, pady=30,command=lambda: click(6))
button_7 = Button(root, text=7, bg="gray", padx=60, pady=30,command=lambda: click(7))
button_8 = Button(root, text=8, bg="gray", padx=60, pady=30,command=lambda: click(8))
button_9 = Button(root, text=9, bg="gray", padx=60, pady=30,command=lambda: click(9))
button_0 = Button(root, text=0, bg="gray", padx=60, pady=30,command=lambda: click(0))
buttonadd = Button(root, text="+", bg="gray", padx=60, pady=30,command=add)
buttonsub = Button(root, text="-", bg="gray", padx=60, pady=30,command=sub)
buttonmul = Button(root, text="*", bg="gray", padx=60, pady=30,command=mul)
buttondivid = Button(root, text="/", bg="gray", padx=60, pady=30,command=divid)
buttonclear = Button(root, text="AC", bg="gray", padx=55, pady=30,command=clear)
buttonequal = Button(root, text="=", bg="gray", padx=60, pady=30,command=equal)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
buttonclear.grid(row=1, column=4)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
buttonadd.grid(row=2, column=4)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
buttonsub.grid(row=3, column=4)
button_0.grid(row=4, column=0)
buttonmul.grid(row=4, column=1)
buttondivid.grid(row=4, column=2)
buttonequal.grid(row=4, column=4)




root.mainloop()






