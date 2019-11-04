from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('290x360')
root.configure(background='#17181a')


def num_on_click(number):
    fnumber = num_entry.get()
    num_entry.delete(0, END)
    num_entry.insert(0, fnumber + str(number))


def onclick_clear():
        num_entry.delete(0, END)


def onclick_add():
    fnumber = num_entry.get()
    global fnum
    global operation
    operation = "addition"
    fnum = int(fnumber)
    num_entry.delete(0, END)


def onclick_sub():
    fnumber = num_entry.get()
    global fnum
    global operation
    operation = "subtraction"
    fnum = int(fnumber)
    num_entry.delete(0, END)


def onclick_mult():
    fnumber = num_entry.get()
    global fnum
    global operation
    operation = "multiplication"
    fnum = int(fnumber)
    num_entry.delete(0, END)


def onclick_div():
    fnumber = num_entry.get()
    global fnum
    global operation
    operation = "division"
    fnum = int(fnumber)
    num_entry.delete(0, END)


def onclick_equal():
    snumber = num_entry.get()
    snum = int(snumber)
    num_entry.delete(0, END)
    if operation == "addition":
        num_entry.insert(0, fnum + snum)
    if operation == "subtraction":
        num_entry.insert(0, fnum - snum)
    if operation == "multiplication":
        num_entry.insert(0, fnum * snum)
    if operation == "division":
        num_entry.insert(0, fnum / snum)


num_entry = Entry(root, bg='#17181a', fg='#ff9e4f', font=("Alrial", 12, 'bold'))
num_entry.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

btn_1 = Button(root, text="1", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(1))

btn_2 = Button(root, text="2", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(2))

btn_3 = Button(root, text="3", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(3))

btn_4 = Button(root, text="4", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(4))

btn_5 = Button(root, text="5", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(5))

btn_6 = Button(root, text="6", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(6))

btn_7 = Button(root, text="7", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(7))

btn_8 = Button(root, text="8", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(8))

btn_9 = Button(root, text="9", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(9))

btn_0 = Button(root, text="0", padx=40, pady=20, borderwidth=0, font=("Alrial", 12, 'bold'),
               bg='#17181a', fg='#bdffcd', command=lambda: num_on_click(0))

btn_add = Button(root, text="+", padx=20, pady=10, borderwidth=0, font=("Alrial", 12, 'bold'),
                 bg='#17181a', fg='#bdffcd', command=onclick_add)

btn_equal = Button(root, text="=", padx=20, pady=10, borderwidth=0, font=("Alrial", 15, 'bold'),
                   bg='#17181a', fg='#ff9e4f', command=onclick_equal)

btn_clear = Button(root, text="clear", padx=11, pady=10, borderwidth=0, font=("Alrial", 10, 'bold'),
                   bg='#17181a', fg='#ffff80', command=onclick_clear)

btn_sub = Button(root, text="-", padx=20, pady=10, borderwidth=0, font=("Alrial", 15, 'bold'),
                 bg='#17181a', fg='#ff5e5e', command=onclick_sub)

btn_mult = Button(root, text="X", padx=20, pady=10, borderwidth=0, font=("Alrial", 15, 'bold'),
                  bg='#17181a', fg='#c4c2ff', command=onclick_mult)

btn_div = Button(root, text="/", padx=20, pady=10, borderwidth=0, font=("Alrial", 12, 'bold'),
                 bg='#17181a', fg='#ff6ee2', command=onclick_div)

btn_1.grid(row=3, column=1)
btn_2.grid(row=3, column=2)
btn_3.grid(row=3, column=3)
btn_4.grid(row=2, column=1)
btn_5.grid(row=2, column=2)
btn_6.grid(row=2, column=3)
btn_7.grid(row=1, column=1)
btn_8.grid(row=1, column=2)
btn_9.grid(row=1, column=3)
btn_0.grid(row=4, column=1)
btn_add.grid(row=4, column=1)
btn_equal.grid(row=4, column=3)
btn_clear.grid(row=5, column=3, columnspan=2)
btn_sub.grid(row=4, column=2)
btn_mult.grid(row=5, column=2)
btn_div.grid(row=5, column=1)

root.mainloop()
