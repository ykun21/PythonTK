from tkinter import*
root=Tk()
root.geometry('400x450')
root.title('Expense Manager')
root.configure(bg='#17181a')

def Enter_budge():
    global x,y,z
    x=Enter_Budget.get()
    y=Enter_Amount.get()
    z=Enter_exp.get()
    clear()
    display()

def clear():
    Enter_Budget.delete(0, END)
    Enter_exp.delete(0, END)
    Enter_Amount.delete(0,END)

def total():
    totalexp=0



def display() :

     txt_txtbox.insert("end"," "+z+" | "+y+"."+"\n")




lbl_title=Label(root,text='Expense Manager',font=('Arial',15,'bold'),bg='#17181a',fg='#ff6e63')
lbl_title.place(x=115,y=5)

lbl_budget=Label(root,text='Enter Budget',font=('Arial',10,'bold'),fg='#bdffcd',bg='#17181a')
lbl_budget.place(x=60,y=50)

Enter_Budget=Entry(root,width='28',fg='#bdffcd',bg='#17181a')
Enter_Budget.place(x=150,y=50)

lbl_exp=Label(root,text='Expenses',font=('Arial',9,'bold'),fg='#bdffcd',bg='#17181a')
lbl_exp.place(x=60,y=95)

Enter_exp=Entry(root,width='28',fg='#bdffcd',bg='#17181a')
Enter_exp.place(x=150,y=95)

lbl_Amount=Label(root,text='Amount',font=('Arial',9,'bold'),fg='#bdffcd',bg='#17181a')
lbl_Amount.place(x=60,y=140)

Enter_Amount=Entry(root,width='28',fg='#bdffcd',bg='#17181a')
Enter_Amount.place(x=150,y=140)

btn_Enter=Button(root,text='Enter',width='10',command=Enter_budge,fg='#bdffcd',bg='#17181a')
btn_Enter.place(x=150,y=180)

txt_txtbox=Text(root,width='28',height='6',font=('Arial',10,'bold'),fg='#bdffcd',bg='#17181a')
txt_txtbox.place(x=150,y=220)

lbl_txtbox=Label(root,text='Your \n Expenses',font=('Arial',9,'bold'),fg='#bdffcd',bg='#17181a')
lbl_txtbox.place(x=60,y=220)

txt_Total=Text(root,width='28',height='2',font=('Arial',10,'bold'),fg='#bdffcd',bg='#17181a')
txt_Total.place(x=150,y=340)

lbl_txttotal=Label(root,text='Total \n Expenses',font=('Arial',9,'bold'),fg='#bdffcd',bg='#17181a')
lbl_txttotal.place(x=60,y=340)

root.mainloop()