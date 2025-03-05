import tkinter as tk
from tkinter import ttk

def calculations():
    print(numbers.get())

root = tk.Tk()
root.title("Calculator")

numbers = tk.IntVar()

display = ttk.Entry(root)
display.grid(row=0, column=0, columnspan=4)

num7 = ttk.Button(root, text="7", command=calculations)
num7.grid(row=1, column=0)

num8 = ttk.Button(root, text="8")
num8.grid(row=1, column=1)

num9 = ttk.Button(root, text="9")
num9.grid(row=1, column=2)

num_div = ttk.Button(root, text="/")
num_div.grid(row=1, column=3)

num4 = ttk.Button(root, text="4")
num4.grid(row=2, column=0)

num5 = ttk.Button(root, text="5")
num5.grid(row=2, column=1)

num6 = ttk.Button(root, text="6")
num6.grid(row=2, column=2)

num_mult = ttk.Button(root, text="*")
num_mult.grid(row=2, column=3)

num1 = ttk.Button(root, text="1")
num1.grid(row=3, column=0)

num2 = ttk.Button(root, text="2")
num2.grid(row=3, column=1)

num3 = ttk.Button(root, text="3")
num3.grid(row=3, column=2)

num_sub = ttk.Button(root, text="-")
num_sub.grid(row=3, column=3)

clr = ttk.Button(root, text="CLR")
clr.grid(row=4, column=0)

num0 = ttk.Button(root, text="0")
num0.grid(row=4, column=1)

num_equal = ttk.Button(root, text="=")
num_equal.grid(row=4, column=2)

num_add = ttk.Button(root, text="+")
num_add.grid(row=4, column=3)

root.mainloop()