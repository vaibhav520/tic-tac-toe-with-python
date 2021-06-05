from tkinter import  *
from tkinter import messagebox
base=Tk()
base.title("tic tac toe")
base.minsize(550,700)
base.maxsize(550,700)
count=0
turn="0"
winner=False

def disableAllbuttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
def winnerCheck():
    global winner
    # check for 0 wins
    if b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0":
        winner=True
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif count==9:
        messagebox.showinfo(("shit","its a tie"))

# check for x wins
    if b1["text"]=="x" and b2["text"]=="x" and b3["text"]=="x":
        winner=True
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b4["text"]=="x" and b5["text"]=="x" and b6["text"]=="x":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b7["text"]=="x" and b8["text"]=="x" and b9["text"]=="x":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b1["text"]=="x" and b4["text"]=="x" and b7["text"]=="x":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b2["text"] == "x" and b5["text"] == "x" and b8["text"] == "x":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b3["text"]=="x" and b6["text"]=="x" and b9["text"]=="x":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b1["text"]=="x" and b5["text"]=="x" and b9["text"]=="x":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
    elif b3["text"]=="x" and b5["text"]=="x" and b7["text"]=="x":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        disableAllbuttons()
        messagebox.showinfo("congratulations", "0 wins")
def click(b):
    global turn,count
    if b["text"]==" " and turn=="0":
        b["text"]="0"
        turn="x"
        count+=1
    elif b["text"]==" " and turn=="x":
        b["text"]="x"
        turn="0"
        count+=1
    winnerCheck()

def reset():
    global winner,turn,count
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    winner=False
    turn="0"
    count=0
    b1 = Button(base, text=" ", height="15", width="25", command=lambda: click(b1))
    b1.grid(row=1, column=1)

    b2 = Button(base, text=" ", height="15", width="25", command=lambda: click(b2))
    b2.grid(row=1, column=2)

    b3 = Button(base, text=" ", height="15", width="25", command=lambda: click(b3))
    b3.grid(row=1, column=3)

    b4 = Button(base, text=" ", height="15", width="25", command=lambda: click(b4))
    b4.grid(row=2, column=1)

    b5 = Button(base, text=" ", height="15", width="25", command=lambda: click(b5))
    b5.grid(row=2, column=2)

    b6 = Button(base, text=" ", height="15", width="25", command=lambda: click(b6))
    b6.grid(row=2, column=3)

    b7 = Button(base, text=" ", height="15", width="25", command=lambda: click(b7))
    b7.grid(row=3, column=1)

    b8 = Button(base, text=" ", height="15", width="25", command=lambda: click(b8))
    b8.grid(row=3, column=2)

    b9 = Button(base, text=" ", height="15", width="25", command=lambda: click(b9))
    b9.grid(row=3, column=3)


b1 = Button(base,text=" ",height="15",width="25",command=lambda :click(b1))
b1.grid(row=1,column=1)

b2 = Button(base,text=" ",height="15",width="25",command=lambda :click(b2))
b2.grid(row=1,column=2)

b3=Button(base,text=" ",height="15",width="25",command=lambda :click(b3))
b3.grid(row=1,column=3)

b4=Button(base,text=" ",height="15",width="25",command=lambda :click(b4))
b4.grid(row=2,column=1)

b5=Button(base,text=" ",height="15",width="25",command=lambda :click(b5))
b5.grid(row=2,column=2)

b6=Button(base,text=" ",height="15",width="25",command=lambda :click(b6))
b6.grid(row=2,column=3)

b7=Button(base,text=" ",height="15",width="25",command=lambda :click(b7))
b7.grid(row=3,column=1)

b8=Button(base,text=" ",height="15",width="25",command=lambda :click(b8))
b8.grid(row=3,column=2)

b9=Button(base,text=" ",height="15",width="25",command=lambda :click(b9))
b9.grid(row=3,column=3)

#menu
menu=Menu(base)
menu.add_command(label="reset game",command=reset)
base.config(menu=menu)

base.mainloop()