# Initalising Tkinter GUI for Lemonade Stand Menu
import tkinter as tk
from tkinter import ttk

# Calculate 50g lemon prices per amount
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

# Calculate ice cube prices per amount
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

# Calculate lemonade prices per amount
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

# Calculate mango lemonade prices per amount
def mango_lemonade(i):
    amount = (count4.get())
    if len(amount) == 0:
        count4.set(1)
        result = eval(f"1*{mango_lemonade_price}0")
        price4.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{mango_lemonade_price}0")
        price4.config(text=f"${result}0")
    fpurchase()

# Calculate strawberry lemonade prices per amount
def strawberry_lemonade(i):
    amount = (count5.get())
    if len(amount) == 0:
        count5.set(1)
        result = eval(f"1*{strawberry_lemonade_price}0")
        price5.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{strawberry_lemonade_price}0")
        price5.config(text=f"${result}0")
    fpurchase()

# Calculate blueberry lemonade prices per amount
def blueberry_lemonade(i):
    amount = (count3.get())
    if len(amount) == 0:
        count3.set(1)
        result = eval(f"1*{blueberry_lemonade_price}0")
        price3.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{blueberry_lemonade_price}0")
        price3.config(text=f"${result}0")
    fpurchase()

# Calculate raspberry lemonade prices per amount
def raspberry_lemonade(i):
    amount = (count3.get())
    if len(amount) == 0:
        count3.set(1)
        result = eval(f"1*{raspberry_lemonade_price}0")
        price3.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{raspberry_lemonade_price}0")
        price3.config(text=f"${result}0")
    fpurchase()

# Calculate the sum of all costs(Lemons, Ice Cubes, Lemonade)
def fpurchase():
    amount1 = (count.get())
    amount2 = (count2.get())
    amount3 = (count3.get())
    amount4 = (count4.get())
    amount5 = (count5.get())
    amount6 = (count6.get())
    amount7 = (count7.get())
    result = eval(f"{amount1}*{lemon_price}+{amount2}*{icecube_price}+{amount3}*{lemonade_price}+{amount4}*{mango_lemonade_price}+{amount5}*{strawberry_lemonade_price}+{amount6}*{blueberry_lemonade_price}+{amount7}*{raspberry_lemonade_price}0")
    if check1.get() <= 0:
        result += eval(f"-{amount1}*{lemon_price}")
    if check2.get() <= 0:
        result += eval(f"-{amount2}*{icecube_price}")
    if check3.get() <= 0:
        result += eval(f"-{amount3}*{lemonade_price}")
    if check4.get() <= 0:
        result += eval(f"-{amount4}*{mango_lemonade_price}")
    if check5.get() <= 0:
        result += eval(f"-{amount5}*{strawberry_lemonade_price}")
    if check6.get() <= 0:
        result += eval(f"-{amount6}*{blueberry_lemonade_price}")
    if check7.get() <= 0:
        result += eval(f"-{amount7}*{raspberry_lemonade_price}")
    purchase_L.config(text=f"${result}0")

# Initialisng Item Prices
lemon_price = "1.50"
icecube_price = "0.50"
lemonade_price = "2.00"
mango_lemonade_price = "2.50"
strawberry_lemonade_price = "2.50"
blueberry_lemonade_price = "2.50"
raspberry_lemonade_price = "2.50"

# Initialise Lemonade Stand Window Menu
root = tk.Tk()
root.title("Lemonade Stand Menu")

# Intialise amount of the item as a string
count = tk.StringVar(value=1)
count2 = tk.StringVar(value=1)
count3 = tk.StringVar(value=1)
count4 = tk.StringVar(value=1)
count5 = tk.StringVar(value=1)
count6 = tk.StringVar(value=1)
count7 = tk.StringVar(value=1)

# Intialise if item is selected(True/False,1/0)
check1 = tk.IntVar()
check2 = tk.IntVar()
check3 = tk.IntVar()
check4 = tk.IntVar()
check5 = tk.IntVar()
check6 = tk.IntVar()
check7 = tk.IntVar()

# Test
idk = tk.StringVar()

# Intialise title
title = ttk.Label(root, text="Lemonade Stand Menu")
title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialise subheadings
price_L = ttk.Label(root, text="Price")
price_L.grid(row=1, column=3, pady=5)
item_L = ttk.Label(root, text="Item")
item_L.grid(row=1, column=2, pady=5)
amount_L = ttk.Label(root, text="Amount")
amount_L.grid(row=1, column=0, pady=5, columnspan=2)

# Initialise checkboxes for each item
selected_1 = ttk.Checkbutton(root, variable=check1, onvalue=1, offvalue=0, command=lambda:lemons(1))
selected_1.grid(row=2, column=0, sticky="e")
selected_2 = ttk.Checkbutton(root, variable=check2, onvalue=1, offvalue=0, command=lambda:ice(1))
selected_2.grid(row=3, column=0, sticky="e")
selected_3 = ttk.Checkbutton(root, variable=check3, onvalue=1, offvalue=0, command=lambda:lemonade(1))
selected_3.grid(row=4, column=0, sticky="e")
selected_4 = ttk.Checkbutton(root, variable=check4, onvalue=1, offvalue=0, command=lambda:mango_lemonade(1))
selected_4.grid(row=5, column=0, sticky="e")
selected_5 = ttk.Checkbutton(root, variable=check5, onvalue=1, offvalue=0, command=lambda:strawberry_lemonade(1))
selected_5.grid(row=6, column=0, sticky="e")
selected_6 = ttk.Checkbutton(root, variable=check6, onvalue=1, offvalue=0, command=lambda:blueberry_lemonade(1))
selected_6.grid(row=7, column=0, sticky="e")
selected_7 = ttk.Checkbutton(root, variable=check7, onvalue=1, offvalue=0, command=lambda:raspberry_lemonade(1))
selected_7.grid(row=8, column=0, sticky="e", padx=10)

# Initialise prices for each item
price1 = ttk.Label(root, text=f"${lemon_price}")
price1.grid(row=2, column=3, padx=10)
price2 = ttk.Label(root, text=f"${icecube_price}")
price2.grid(row=3, column=3, padx=10)
price3 = ttk.Label(root, text=f"${lemonade_price}")
price3.grid(row=4, column=3, padx=10)
price4 = ttk.Label(root, text=f"${mango_lemonade_price}")
price4.grid(row=5, column=3, padx=10)
price5 = ttk.Label(root, text=f"${strawberry_lemonade_price}")
price5.grid(row=6, column=3, padx=10)
price6 = ttk.Label(root, text=f"${blueberry_lemonade_price}")
price6.grid(row=7, column=3, padx=10)
price7 = ttk.Label(root, text=f"${raspberry_lemonade_price}")
price7.grid(row=8, column=3, padx=10)

# Initialise items
millilitres = ["250ml", 
               "500ml", 
               "1L"]

item1 = ttk.Label(root, text="50g Lemons")
item1.grid(row=2, column=2, padx=5, sticky="w")
item2 = ttk.Label(root, text="Ice Cubes")
item2.grid(row=3, column=2, padx=5, sticky="w")
item3 = ttk.Label(root, text="250ml Lemonade")
item3.grid(row=4, column=2, padx=5, sticky="w")
item4 = ttk.Label(root, text="250ml Mango Lemonade")
item4.grid(row=5, column=2, padx=5, sticky="w")
item5 = ttk.Label(root, text="250ml Strawberry Lemonade")
item5.grid(row=6, column=2, padx=5, sticky="w")
item6 = ttk.Label(root, text="250ml Blueberry Lemonade")
item6.grid(row=7, column=2, padx=5, sticky="w")
item7 = ttk.Label(root, text="250ml Raspberry Lemonade")
item7.grid(row=8, column=2, padx=5, sticky="w")

millilitre = ttk.Combobox(root, values=millilitres, state="readonly")
millilitre.grid(row=4, column=2, sticky="w")

# Initialise entries(amount) for each item
quantity1 = ttk.Entry(root, width=5, textvariable=count)
quantity1.grid(row=2, column=1, padx=5)
quantity2 = ttk.Entry(root, width=5, textvariable=count2)
quantity2.grid(row=3, column=1, padx=5)
quantity3 = ttk.Entry(root, width=5, textvariable=count3)
quantity3.grid(row=4, column=1, padx=5)
quantity4 = ttk.Entry(root, width=5, textvariable=count4)
quantity4.grid(row=5, column=1, padx=5)
quantity5 = ttk.Entry(root, width=5, textvariable=count5)
quantity5.grid(row=6, column=1, padx=5)
quantity6 = ttk.Entry(root, width=5, textvariable=count6)
quantity6.grid(row=7, column=1, padx=5)
quantity7 = ttk.Entry(root, width=5, textvariable=count7)
quantity7.grid(row=8, column=1, padx=5)

# Purchase button
purchase_L = ttk.Button(root, text="$0.00")
purchase_L.grid(row=9, column=0, columnspan=4, padx=10, pady=10)

# Entry Binding
quantity1.bind("<KeyRelease>", lemons)
quantity2.bind("<KeyRelease>", ice)
quantity3.bind("<KeyRelease>", lemonade)
quantity4.bind("<KeyRelease>", mango_lemonade)
quantity5.bind("<KeyRelease>", strawberry_lemonade)
quantity6.bind("<KeyRelease>", blueberry_lemonade)
quantity7.bind("<KeyRelease>", raspberry_lemonade)

# Forward intialised widgets to window
root.mainloop()