import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

root = tk.Tk()
root.title("Lemonade Stand Menu")
root.geometry("600x420")
root.resizable(False, False)

class prices:
    lemon = 1.00
    classic_lemonade = 2.00
    mango_lemonade = 2.50
    strawberry_lemonade = 2.50
    blueberry_lemonade = 2.50
    raspberry_lemonade = 2.50
    ice = 0.50
    sugar = 0.50
    ml250 = 0.00
    ml500 = 2.00
    L1 = 4.00

def lemonade_customisation(flavour, price):
    size_lemonade = 0
    condiments = 0
    # Initalise Popup Window
    global pop
    pop = tk.Toplevel(root)
    pop.title("Popup")
    pop.resizable(False, False)
    pop.grab_set()

    pop_frame = tk.Frame(pop, height=200, width=300)
    pop_frame.pack(padx=10, pady=10)

    # Size Values
    size_frame = tk.LabelFrame(pop_frame, height=100, width=100, text="Size")
    size_frame.grid(row=0, column=0, sticky="nsew")
    size_frame.grid_propagate(False)

    def radio():
        nonlocal size_lemonade
        portion = size.get()

        if portion == 1:
            size_lemonade = prices.ml250
        elif portion == 2:
            size_lemonade = prices.ml500
        elif portion == 3:
            size_lemonade = prices.L1

    global size
    size = tk.IntVar(value=1)
    ml250 = ttk.Radiobutton(size_frame, text="250ml", value=1, variable=size, command=lambda: radio())
    ml250.grid(row=0, column=0, sticky="nsew")

    ml500 = ttk.Radiobutton(size_frame, text="500ml", value=2, variable=size, command=lambda: radio())
    ml500.grid(row=1, column=0, sticky="nsew")

    L1 = ttk.Radiobutton(size_frame, text="1L", value=3, variable=size, command=lambda: radio())
    L1.grid(row=2, column=0, sticky="nsew")
    
    # Condiments Values
    condiments_frame = tk.LabelFrame(pop_frame, height=100, width=100, text="Condiments")
    condiments_frame.grid(row=0, column=1, sticky="nsew")
    condiments_frame.grid_propagate(False)

    def box(item):
        nonlocal condiments
        if item == "ice":
            if icebool.get():
                condiments += prices.ice
            elif icebool.get() == False:
                condiments -= prices.ice

        if item == "sugar":
            if sugarbool.get():
                condiments += prices.ice
            elif sugarbool.get() == False:
                condiments -= prices.ice

    global icebool
    icebool = tk.BooleanVar(value=False)
    ice = ttk.Checkbutton(condiments_frame, text="Ice", variable=icebool, onvalue=True, offvalue=False, command=lambda:box("ice"))
    ice.grid(row=0, column=0, sticky="nsew")

    global sugarbool
    sugarbool = tk.BooleanVar(value=False)
    extra_sugar = ttk.Checkbutton(condiments_frame, text="Extra Sugar", variable=sugarbool, onvalue=True, offvalue=False, command=lambda:box("sugar"))
    extra_sugar.grid(row=1, column=0, sticky="nsew")

    # Confirm Button
    pop_button = ttk.Button(pop_frame, text="Confirm", command = lambda: (amount(flavour, size_lemonade+condiments+price)))
    pop_button.grid(row=4, column=0, columnspan=2, pady=10)

def amount(item, price):
    print(item , price)
    pop.destroy()
    global amount_main_frame
    amount_main_frame = tk.Toplevel(root)
    amount_main_frame.title("Popup")
    amount_main_frame.resizable(False, False)
    amount_main_frame.grab_set()

    amount_frame = tk.LabelFrame(amount_main_frame, height=200, width=300, padx=10, pady=10)
    amount_frame.pack(padx=10, pady=10)

    desired_amount = ttk.Label(amount_frame, text="Choose desired amount")
    desired_amount.grid(row=0, column=0, sticky="nsew")

    global amount_input_num
    amount_input_num = tk.IntVar(value=1)
    amount_input = ttk.Spinbox(amount_frame, width=10, from_=1, to=100, increment=1, textvariable=amount_input_num)
    amount_input.grid(row=1, column=0, pady=10)

    def confirm(item, price, amount):
        print(item, price*amount, amount)

        amount_main_frame.destroy()

    confirm_amount = ttk.Button(amount_frame, text="Confirm", command=lambda: (confirm(item, price, amount_input_num.get())))
    confirm_amount.grid(row=2, column=0, pady=10)



main_frame = tk.Frame(root, height=500, width=800)
main_frame.pack(padx=10, pady=10)


item_select_frame = tk.LabelFrame(main_frame, text="Select Item", height=400, width=395, padx=10)
item_select_frame.grid(row=0, column=0, columnspan=3, rowspan=8, sticky="n")
item_select_frame.grid_propagate(False)


cart_frame = tk.LabelFrame(main_frame, text="Cart", height=300, width=180)
cart_frame.grid(row=0, column=3, rowspan=6, sticky="n")
cart_frame.pack_propagate(False)

clear_cart_button = ttk.Button(main_frame, text="Clear Cart")
clear_cart_button.grid(row=6, column=3, sticky="nsew")  

purchase_cart_button = ttk.Button(main_frame, text="Purchase $0.00", padding=10, width=26)
purchase_cart_button.grid(row=7, column=3, sticky="nsew")


# Item Buttons
lemons_button = ttk.Button(item_select_frame, text="Lemon \n$1.00", padding=40, width=6)
lemons_button.grid(row=0, column=0, sticky="nsew")

classic_lemonade_button = ttk.Button(item_select_frame, text="Lemonade \n$2.00", width=20, padding=(0, 50), command=lambda: lemonade_customisation("Classic Lemonade", prices.classic_lemonade))
classic_lemonade_button.grid(row=0, column=1, sticky="nsew")

mango_lemonade_button = ttk.Button(item_select_frame, text="Mango Lemonade \n$2.50", padding=0)
mango_lemonade_button.grid(row=0, column=2, sticky="nsew")

strawberry_lemonade_button = ttk.Button(item_select_frame, text="Strawberry \nLemonade \n$2.50", width=6)
strawberry_lemonade_button.grid(row=1, column=0, sticky="nsew")

blueberry_lemonade_button = ttk.Button(item_select_frame, text="Blueberry \nLemonade \n$2.50", width=20)
blueberry_lemonade_button.grid(row=1, column=1, sticky="nsew")

raspberry_lemonade_button = ttk.Button(item_select_frame, text="Raspberry \nLemonade \n$2.50", width=19, padding=(0, 40))
raspberry_lemonade_button.grid(row=1, column=2, sticky="nsew")

# Initalise Widgets
root.mainloop()