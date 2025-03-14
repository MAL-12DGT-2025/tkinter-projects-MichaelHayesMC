import tkinter as tk
from tkinter import ttk

lemon_price = "1.50"
icecube_price = "0.50"
lemonade_price = "2.00"

def lemons(i):
    amount = (count.get())
    if len(amount) == 0:
        count.set(1)
        result = eval(f"1*{lemon_price}0")
        price1.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{lemon_price}0")
        price1.config(text=f"${result}0")
    fpurchase()

def ice(i):
    amount = (count2.get())
    if len(amount) == 0:
        count2.set(1)
        result = eval(f"1*{icecube_price}0")
        price2.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{icecube_price}0")
        price2.config(text=f"${result}0")
    fpurchase()

def lemonade(i):
    amount = (count3.get())
    if len(amount) == 0:
        count3.set(1)
        result = eval(f"1*{lemonade_price}0")
        price3.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{lemonade_price}0")
        price3.config(text=f"${result}0")
    fpurchase()

def fpurchase():
    amount1 = (count.get())
    amount2 = (count2.get())
    amount3 = (count3.get())
    result = eval(f"{amount1}*{lemon_price}+{amount2}*{icecube_price}+{amount3}*{lemonade_price}0")
    if check1.get() <= 0:
        result += eval(f"-{amount1}*{lemon_price}")
    if check2.get() <= 0:
        result += eval(f"-{amount2}*{icecube_price}")
    if check3.get() <= 0:
        result += eval(f"-{amount3}*{lemonade_price}")
    purchase_L.config(text=f"${result}0")

root = tk.Tk()
root.title("Lemonade Stand Menu")

count = tk.StringVar(value=1)
count2 = tk.StringVar(value=1)
count3 = tk.StringVar(value=1)

check1 = tk.IntVar()
check2 = tk.IntVar()
check3 = tk.IntVar()

title = ttk.Label(root, text="Lemonade Stand Menu")
title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

selected_L = ttk.Label(root, text="Selected")
selected_L.grid(row=1, column=0, padx=5)

price_L = ttk.Label(root, text="Price")
price_L.grid(row=1, column=3, pady=5)

item_L = ttk.Label(root, text="Item")
item_L.grid(row=1, column=2, pady=5)

amount_L = ttk.Label(root, text="Amount")
amount_L.grid(row=1, column=1, pady=5)

selected_1 = ttk.Checkbutton(root, variable=check1, onvalue=1, offvalue=0, command=lambda:lemons(1))
selected_1.grid(row=2, column=0)

selected_2 = ttk.Checkbutton(root, variable=check2, onvalue=1, offvalue=0, command=lambda:ice(1))
selected_2.grid(row=3, column=0)

selected_3 = ttk.Checkbutton(root, variable=check3, onvalue=1, offvalue=0, command=lambda:lemonade(1))
selected_3.grid(row=4, column=0)

price1 = ttk.Label(root, text=f"${lemon_price}")
price1.grid(row=2, column=3, padx=10)

price2 = ttk.Label(root, text=f"${icecube_price}")
price2.grid(row=3, column=3, padx=10)

price3 = ttk.Label(root, text=f"${lemonade_price}")
price3.grid(row=4, column=3, padx=10)

item1 = ttk.Label(root, text="50g Lemons")
item1.grid(row=2, column=2, padx=5)

item2 = ttk.Label(root, text="Ice Cubes")
item2.grid(row=3, column=2, padx=5)

item3 = ttk.Label(root, text="250ml Lemonade")
item3.grid(row=4, column=2, padx=5)

quantity1 = ttk.Entry(root, width=5, textvariable=count)
quantity1.grid(row=2, column=1, padx=5)
quantity1.bind("<KeyRelease>", lemons)

quantity2 = ttk.Entry(root, width=5, textvariable=count2)
quantity2.grid(row=3, column=1, padx=5)
quantity2.bind("<KeyRelease>", ice)

quantity3 = ttk.Entry(root, width=5, textvariable=count3)
quantity3.grid(row=4, column=1, padx=5)
quantity3.bind("<KeyRelease>", lemonade)

purchase_L = ttk.Button(root, text="$0.00")
purchase_L.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()