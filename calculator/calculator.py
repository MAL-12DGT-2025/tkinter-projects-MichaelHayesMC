import tkinter as tk
from tkinter import ttk

def press(button):
    current = equation.get()
    
    symbols = ["+", "-", "*", "/"]

    if current[-1] in symbols:
        equation.set(current[:-1] + button)
        
    current += button
    equation.set(current)

def clear():
    equation.set("")

def calculate():
    try:
        result = eval(equation.get())
        equation.set(result)
    except:
        equation.set("ERROR")

root = tk.Tk()
root.title("Calculator")

equation = tk.StringVar()

display = ttk.Entry(root, textvariable=equation)
display.grid(row=0, column=0, columnspan=4)

num7 = ttk.Button(root, text="7", command=lambda:press("7"))
num7.grid(row=1, column=0)

num8 = ttk.Button(root, text="8", command=lambda:press("8"))
num8.grid(row=1, column=1)

num9 = ttk.Button(root, text="9", command=lambda:press("9"))
num9.grid(row=1, column=2)

num_div = ttk.Button(root, text="/", command=lambda:press("/"))
num_div.grid(row=1, column=3)

num4 = ttk.Button(root, text="4", command=lambda:press("4"))
num4.grid(row=2, column=0)

num5 = ttk.Button(root, text="5", command=lambda:press("5"))
num5.grid(row=2, column=1)

num6 = ttk.Button(root, text="6", command=lambda:press("6"))
num6.grid(row=2, column=2)

num_mult = ttk.Button(root, text="*", command=lambda:press("*"))
num_mult.grid(row=2, column=3)

num1 = ttk.Button(root, text="1", command=lambda:press("1"))
num1.grid(row=3, column=0)

num2 = ttk.Button(root, text="2", command=lambda:press("2"))
num2.grid(row=3, column=1)

num3 = ttk.Button(root, text="3", command=lambda:press("3"))
num3.grid(row=3, column=2)

num_sub = ttk.Button(root, text="-", command=lambda:press("-"))
num_sub.grid(row=3, column=3)

clr = ttk.Button(root, text="CLR", command=clear)
clr.grid(row=4, column=0)

num0 = ttk.Button(root, text="0", command=lambda:press("0"))
num0.grid(row=4, column=1)

num_equal = ttk.Button(root, text="=", command=calculate)
num_equal.grid(row=4, column=2)

num_add = ttk.Button(root, text="+", command=lambda:press("+"))
num_add.grid(row=4, column=3)

root.mainloop()