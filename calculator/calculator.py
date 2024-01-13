from tkinter import *

root = Tk()
root.title("Simple Calculator")

e=Entry(root, width=36, borderwidth=6)
e.grid(row=0, columnspan=4)
ws = 8
wb = ws*2 + 2
h = 3
bg1 = "#D3D3D3"
bg2 = "#fff"
bg3 = "#899499"

def buttonAdd(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_Clear():
    e.delete(0, END)
    
def button_Equal():
    second = int(e.get())
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + second)
    elif math == "substract":
        e.insert(0, f_num - second)
    elif math == "multiply":
        e.insert(0, f_num * second)
    elif math == "divide":
        e.insert(0, f_num / second)
    
def buttonAddOperation():
    first = e.get()
    global f_num 
    global math
    math = "add"
    f_num = float(first)
    e.delete(0, END)

def buttonSubstractOperation():
    first = e.get()
    global f_num 
    global math
    math = "substract"
    f_num = float(first)
    e.delete(0, END)

def buttonMultiplyOperation():
    first = e.get()
    global f_num 
    global math
    math = "multiply"
    f_num = float(first)
    e.delete(0, END)

def buttonDivideOperation():
    first = e.get()
    global f_num 
    global math
    math = "divide"
    f_num = float(first)
    e.delete(0, END)

#Define Buttons

button9 = Button(root, text="9", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(9))
button8 = Button(root, text="8", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(8))
button7 = Button(root, text="7", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(7))
button6 = Button(root, text="6", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(6))
button5 = Button(root, text="5", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(5))
button4 = Button(root, text="4", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(4))
button3 = Button(root, text="3", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(3))
button2 = Button(root, text="2", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(2))
button1 = Button(root, text="1", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(1))
button0 = Button(root, text="0", bg=bg1, width=ws, height=h, command=lambda: buttonAdd(0))
buttonClear = Button(root, text="Clear", bg=bg2, width=ws, height=h, command=button_Clear).grid(row=4, column=1)
buttonEqual = Button(root, text="=", bg=bg2, width=ws, height=h, command=button_Equal).grid(row=4, column=2)

buttonPlus= Button(root, text="+", bg=bg3, width=ws, height=h, command=buttonAddOperation)
buttonSubstract = Button(root, bg=bg3, text="-", width=ws, height=h, command=buttonSubstractOperation)
buttonMultiply = Button(root, bg=bg3, text="*", width=ws, height=h, command=buttonMultiplyOperation)
buttonDivide = Button(root, bg=bg3, text="/", width=ws, height=h, command=buttonDivideOperation)

#Shove Buttons

button9.grid(row=1, column=2)
button8.grid(row=1, column=1)
button7.grid(row=1, column=0)

button6.grid(row=2, column=2)
button5.grid(row=2, column=1)
button4.grid(row=2, column=0)

button3.grid(row=3, column=2)
button2.grid(row=3, column=1)
button1.grid(row=3, column=0)

button0.grid(row=4, column=0)

buttonPlus.grid(row=1, column=3)
buttonSubstract.grid(row=2, column=3)
buttonMultiply.grid(row=3, column=3)
buttonDivide.grid(row=4, column=3)

root.mainloop()