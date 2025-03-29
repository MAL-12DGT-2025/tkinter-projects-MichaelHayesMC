# Initalising Tkinter GUI for Lemonade Stand Menu
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

result = ""

# Calculate 50g lemon prices per amount
def lemons(i):
    amount = (lemons_entryvalue.get())
    if len(amount) == 0:
        lemons_entryvalue.set(1)
        result = eval(f"1*{lemon_price}0")
        lemon_price_label.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{lemon_price}0")
        lemon_price_label.config(text=f"${result}0")
    fpurchase()

# Calculate ice cube prices per amount
def ice(i):
    amount = (ice_entryvalue.get())
    if len(amount) == 0:
        ice_entryvalue.set(1)
        result = eval(f"1*{icecube_price}0")
        ice_price_label.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{icecube_price}0")
        ice_price_label.config(text=f"${result}0")
    fpurchase()

# Calculate lemonade prices per amount
def lemonade(i):
    amount = (lemonade_entryvalue.get())
    if len(amount) == 0:
        lemonade_entryvalue.set(1)
        result = eval(f"1*{lemonade_price}0")
        lemonade_price_label.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{lemonade_price}0")
        lemonade_price_label.config(text=f"${result}0")
    fpurchase()

# Calculate mango lemonade prices per amount
def mango_lemonade(i):
    amount = (mango_entryvalue.get())
    if len(amount) == 0:
        mango_entryvalue.set(1)
        result = eval(f"1*{mango_lemonade_price}0")
        mango_price_label.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{mango_lemonade_price}0")
        mango_price_label.config(text=f"${result}0")
    fpurchase()

# Calculate strawberry lemonade prices per amount
def strawberry_lemonade(i):
    amount = (strawberry_entryvalue.get())
    if len(amount) == 0:
        strawberry_entryvalue.set(1)
        result = eval(f"1*{strawberry_lemonade_price}0")
        strawberry_price_label.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{strawberry_lemonade_price}0")
        strawberry_price_label.config(text=f"${result}0")
    fpurchase()

# Calculate blueberry lemonade prices per amount
def blueberry_lemonade(i):
    amount = (lemonade_entryvalue.get())
    if len(amount) == 0:
        lemonade_entryvalue.set(1)
        result = eval(f"1*{blueberry_lemonade_price}0")
        lemonade_price_label.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{blueberry_lemonade_price}0")
        lemonade_price_label.config(text=f"${result}0")
    fpurchase()

# Calculate raspberry lemonade prices per amount
def raspberry_lemonade(i):
    amount = (lemonade_entryvalue.get())
    if len(amount) == 0:
        lemonade_entryvalue.set(1)
        result = eval(f"1*{raspberry_lemonade_price}0")
        lemonade_price_label.config(text=f"${result}0")
    else:
        result = eval(f"{amount}*{raspberry_lemonade_price}0")
        lemonade_price_label.config(text=f"${result}0")
    fpurchase()

# Calculate the sum of all costs(Lemons, Ice Cubes, Lemonade)
def fpurchase():
    amount1 = (lemons_entryvalue.get())
    amount2 = (ice_entryvalue.get())
    amount3 = (lemonade_entryvalue.get())
    amount4 = (mango_entryvalue.get())
    amount5 = (strawberry_entryvalue.get())
    amount6 = (blueberry_entryvalue.get())
    amount7 = (raspberry_entryvalue.get())
    global result
    result = eval(f"{amount1}*{lemon_price}+{amount2}*{icecube_price}+{amount3}*{lemonade_price}+{amount4}*{mango_lemonade_price}+{amount5}*{strawberry_lemonade_price}+{amount6}*{blueberry_lemonade_price}+{amount7}*{raspberry_lemonade_price}0")
    if lemon_boolean.get() <= 0:
        result += eval(f"-{amount1}*{lemon_price}")
    if ice_boolean.get() <= 0:
        result += eval(f"-{amount2}*{icecube_price}")
    if lemonade_boolean.get() <= 0:
        result += eval(f"-{amount3}*{lemonade_price}")
    if mango_boolean.get() <= 0:
        result += eval(f"-{amount4}*{mango_lemonade_price}")
    if strawberry_boolean.get() <= 0:
        result += eval(f"-{amount5}*{strawberry_lemonade_price}")
    if blueberry_boolean.get() <= 0:
        result += eval(f"-{amount6}*{blueberry_lemonade_price}")
    if raspberry_boolean.get() <= 0:
        result += eval(f"-{amount7}*{raspberry_lemonade_price}")
    purchase_L.config(text=f"${result}0")

def purchase_items():
    if result == 0 or result == "":
        messagebox.showwarning("Purchase", "Please select an item to purchase.")
    else:
        messagebox.showinfo("Purchase", f"Thank you for your purchase of ${result}0!")

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
lemons_entryvalue = tk.StringVar(value=1)
ice_entryvalue = tk.StringVar(value=1)
lemonade_entryvalue = tk.StringVar(value=1)
mango_entryvalue = tk.StringVar(value=1)
strawberry_entryvalue = tk.StringVar(value=1)
blueberry_entryvalue = tk.StringVar(value=1)
raspberry_entryvalue = tk.StringVar(value=1)

# Intialise if item is selected(True/False,1/0)
lemon_boolean = tk.IntVar()
ice_boolean = tk.IntVar()
lemonade_boolean = tk.IntVar()
mango_boolean = tk.IntVar()
strawberry_boolean = tk.IntVar()
blueberry_boolean = tk.IntVar()
raspberry_boolean = tk.IntVar()

# Intialise title
title = ttk.Label(root, text="Lemonade Stand Menu")
title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialise subheadings
price_L = ttk.Label(root, text="Price")
price_L.grid(row=1, column=3, pady=5)
item_L = ttk.Label(root, text="Item")
item_L.grid(row=1, column=2, pady=5)
amount_L = ttk.Label(root, text="Amount")
amount_L.grid(row=1, column=0, pady=5, columnspan=2, padx=20)

# Initialise checkboxes for each item
lemon_selected = ttk.Checkbutton(root, variable=lemon_boolean, onvalue=1, offvalue=0, command=lambda:lemons(1))
lemon_selected.grid(row=2, column=0)
ice_selected = ttk.Checkbutton(root, variable=ice_boolean, onvalue=1, offvalue=0, command=lambda:ice(1))
ice_selected.grid(row=3, column=0)
lemonade_selected = ttk.Checkbutton(root, variable=lemonade_boolean, onvalue=1, offvalue=0, command=lambda:lemonade(1))
lemonade_selected.grid(row=4, column=0)
mango_selected = ttk.Checkbutton(root, variable=mango_boolean, onvalue=1, offvalue=0, command=lambda:mango_lemonade(1))
mango_selected.grid(row=5, column=0)
strawberry_selected = ttk.Checkbutton(root, variable=strawberry_boolean, onvalue=1, offvalue=0, command=lambda:strawberry_lemonade(1))
strawberry_selected.grid(row=6, column=0)
blueberry_selected = ttk.Checkbutton(root, variable=blueberry_boolean, onvalue=1, offvalue=0, command=lambda:blueberry_lemonade(1))
blueberry_selected.grid(row=7, column=0)
raspberry_selected = ttk.Checkbutton(root, variable=raspberry_boolean, onvalue=1, offvalue=0, command=lambda:raspberry_lemonade(1))
raspberry_selected.grid(row=8, column=0)

# Initialise prices for each item
lemon_price_label = ttk.Label(root, text=f"${lemon_price}")
lemon_price_label.grid(row=2, column=3, padx=10)
ice_price_label = ttk.Label(root, text=f"${icecube_price}")
ice_price_label.grid(row=3, column=3, padx=10)
lemonade_price_label = ttk.Label(root, text=f"${lemonade_price}")
lemonade_price_label.grid(row=4, column=3, padx=10)
mango_price_label = ttk.Label(root, text=f"${mango_lemonade_price}")
mango_price_label.grid(row=5, column=3, padx=10)
strawberry_price_label = ttk.Label(root, text=f"${strawberry_lemonade_price}")
strawberry_price_label.grid(row=6, column=3, padx=10)
blueberry_price_label = ttk.Label(root, text=f"${blueberry_lemonade_price}")
blueberry_price_label.grid(row=7, column=3, padx=10)
raspberry_price_label = ttk.Label(root, text=f"${raspberry_lemonade_price}")
raspberry_price_label.grid(row=8, column=3, padx=10)

# Initialise items
lemon_label = ttk.Label(root, text="50g Lemons")
lemon_label.grid(row=2, column=2, padx=5, sticky="w")
ice_label = ttk.Label(root, text="Ice Cubes")
ice_label.grid(row=3, column=2, padx=5, sticky="w")
lemonade_label = ttk.Label(root, text="250ml Lemonade")
lemonade_label.grid(row=4, column=2, padx=5, sticky="w")
mango_label = ttk.Label(root, text="250ml Mango Lemonade")
mango_label.grid(row=5, column=2, padx=5, sticky="w")
strawberry_label = ttk.Label(root, text="250ml Strawberry Lemonade")
strawberry_label.grid(row=6, column=2, padx=5, sticky="w")
blueberry_label = ttk.Label(root, text="250ml Blueberry Lemonade")
blueberry_label.grid(row=7, column=2, padx=5, sticky="w")
raspberry_label = ttk.Label(root, text="250ml Raspberry Lemonade")
raspberry_label.grid(row=8, column=2, padx=5, sticky="w")

# Initialise entries(amount) for each item
num_lemons = ttk.Entry(root, width=5, textvariable=lemons_entryvalue)
num_lemons.grid(row=2, column=1, padx=5)
num_ice = ttk.Entry(root, width=5, textvariable=ice_entryvalue)
num_ice.grid(row=3, column=1, padx=5)
num_lemonade = ttk.Entry(root, width=5, textvariable=lemonade_entryvalue)
num_lemonade.grid(row=4, column=1, padx=5)
num_mango = ttk.Entry(root, width=5, textvariable=mango_entryvalue)
num_mango.grid(row=5, column=1, padx=5)
num_strawberry = ttk.Entry(root, width=5, textvariable=strawberry_entryvalue)
num_strawberry.grid(row=6, column=1, padx=5)
num_blueberry = ttk.Entry(root, width=5, textvariable=blueberry_entryvalue)
num_blueberry.grid(row=7, column=1, padx=5)
num_raspberry = ttk.Entry(root, width=5, textvariable=raspberry_entryvalue)
num_raspberry.grid(row=8, column=1, padx=5)

# Purchase button
purchase_L = ttk.Button(root, text="$0.00", command=purchase_items)
purchase_L.grid(row=9, column=0, columnspan=4, padx=10, pady=10)

# Entry Binding
num_lemons.bind("<KeyRelease>", lemons)
num_ice.bind("<KeyRelease>", ice)
num_lemonade.bind("<KeyRelease>", lemonade)
num_mango.bind("<KeyRelease>", mango_lemonade)
num_strawberry.bind("<KeyRelease>", strawberry_lemonade)
num_blueberry.bind("<KeyRelease>", blueberry_lemonade)
num_raspberry.bind("<KeyRelease>", raspberry_lemonade)

# Forward intialised widgets to window
root.mainloop()