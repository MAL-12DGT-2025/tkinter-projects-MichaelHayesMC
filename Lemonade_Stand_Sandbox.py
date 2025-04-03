import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

total_cart = 0

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
    total = size_lemonade+condiments+price
    # Initalise Popup Window
    global pop
    pop = tk.Toplevel(root)
    pop.title("Popup")
    pop.resizable(False, False)
    pop.grab_set()

    pop_frame = tk.Frame(pop, height=237, width=390)
    pop_frame.pack(padx=10, pady=10)

    # Size Values
    size_frame = tk.LabelFrame(pop_frame, height=110, width=190, text="Size")
    size_frame.grid(row=0, column=0, sticky="nsew")
    size_frame.grid_propagate(False)

    def radio():
        nonlocal size_lemonade
        nonlocal total
        portion = size.get()

        if portion == 1:
            size_lemonade = prices.ml250
        elif portion == 2:
            size_lemonade = prices.ml500
        elif portion == 3:
            size_lemonade = prices.L1
        price_change_popup()

    global size
    size = tk.IntVar(value=1)
    ml250 = ttk.Radiobutton(size_frame, text="250ml", value=1, variable=size, command=lambda: radio())
    ml250.grid(row=0, column=0, sticky="nsew")
    dash_250_label = ttk.Label(size_frame, text="")
    dash_250_label.grid(column=1, row=0, padx=42)
    price_250_label = ttk.Label(size_frame, text="+$0.00")
    price_250_label.grid(column=2, row=0, sticky="w")

    ml500 = ttk.Radiobutton(size_frame, text="500ml", value=2, variable=size, command=lambda: radio())
    ml500.grid(row=1, column=0, sticky="nsew")
    price_500_label = ttk.Label(size_frame, text="+$2.00")
    price_500_label.grid(column=2, row=1, sticky="w")

    L1 = ttk.Radiobutton(size_frame, text="1L", value=3, variable=size, command=lambda: radio())
    L1.grid(row=2, column=0, sticky="nsew")
    price_1_label = ttk.Label(size_frame, text="+$4.00")
    price_1_label.grid(column=2, row=2, sticky="w")
    
    # Condiments Values
    condiments_frame = tk.LabelFrame(pop_frame, height=110, width=190, text="Condiments")
    condiments_frame.grid(row=0, column=1, sticky="nsew")
    condiments_frame.grid_propagate(False)

    def box(item):
        nonlocal condiments
        nonlocal total
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
    
        price_change_popup()

    global icebool
    icebool = tk.BooleanVar(value=False)
    ice = ttk.Checkbutton(condiments_frame, text="Ice", variable=icebool, onvalue=True, offvalue=False, command=lambda:box("ice"))
    ice.grid(row=0, column=0, sticky="nsew")
    dash_ice_label = ttk.Label(condiments_frame, text="")
    dash_ice_label.grid(column=1, row=0, padx=28)
    price_ice_label = ttk.Label(condiments_frame, text="+$0.50")
    price_ice_label.grid(column=2, row=0, sticky="w")

    global sugarbool
    sugarbool = tk.BooleanVar(value=False)
    extra_sugar = ttk.Checkbutton(condiments_frame, text="Extra Sugar", variable=sugarbool, onvalue=True, offvalue=False, command=lambda:box("sugar"))
    extra_sugar.grid(row=1, column=0, sticky="nsew")
    price_ice_label = ttk.Label(condiments_frame, text="+$0.50")
    price_ice_label.grid(column=2, row=1, sticky="w")

    # Price Display Lemonade Customisation Popup
    def price_change_popup():
        total = size_lemonade+condiments+price
        pop_price_label.config(text=f"${total}0")

    pop_price_label = ttk.Label(pop_frame, text=f"${total}0")
    pop_price_label.grid(row=4, column=0, columnspan=2, sticky="s", pady=5)

    # Confirm Button
    pop_button = ttk.Button(pop_frame, text="Confirm", command = lambda: (amount(flavour, size_lemonade+condiments+price), pop.destroy()))
    pop_button.grid(row=5, column=0, columnspan=2)

def amount(item, price):
    global amount_main_frame
    amount_main_frame = tk.Toplevel(root)
    amount_main_frame.title("Popup")
    amount_main_frame.resizable(False, False)
    amount_main_frame.grab_set()

    amount_frame = tk.LabelFrame(amount_main_frame, height=200, width=300, padx=10, pady=10)
    amount_frame.pack(padx=10, pady=10)

    desired_amount = ttk.Label(amount_frame, text="Choose desired amount")
    desired_amount.grid(row=0, column=0, sticky="nsew")

    def price_change():
        spinbox = amount_input.get()
        amount_price_label.config(text=f"${price*float(spinbox)}0")

    global amount_input_num
    amount_input_num = tk.IntVar(value=1)
    amount_input = ttk.Spinbox(amount_frame, width=10, from_=1, to=100, increment=1, textvariable=amount_input_num, command=price_change, state="readonly")
    amount_input.grid(row=1, column=0, pady=10)

    amount_price_label = ttk.Label(amount_frame, text=f"${price}0")
    amount_price_label.grid(row=2, column=0)

    def confirm(item, price, amount):
        global total_cart
        label = ttk.Label(cart_canvas_frame, text=(f"{amount}x {item} ${price}0"))
        label.pack(pady=2, anchor="nw")
        total_cart += price
        purchase_cart_button.config(text=f"Purchase ${total_cart}0")
        amount_main_frame.destroy()

    confirm_amount = ttk.Button(amount_frame, text="Confirm", command=lambda: (confirm(item, price*amount_input_num.get(), amount_input_num.get())))
    confirm_amount.grid(row=3, column=0, pady=10)

# Main Frame of Tkinter Window
main_frame = tk.Frame(root, height=500, width=800)
main_frame.pack(padx=10, pady=10)

# Menu Frame of items to purchase
item_select_frame = tk.LabelFrame(main_frame, text="Select Item", height=400, width=395, padx=10)
item_select_frame.grid(row=0, column=0, columnspan=3, rowspan=8, sticky="n")
item_select_frame.grid_propagate(False)

# Cart Frame for purchasing items
cart_frame = tk.LabelFrame(main_frame, text="Cart", height=300, width=180)
cart_frame.grid(row=0, column=3, rowspan=6, sticky="n")
cart_frame.pack_propagate(False)

cart_canvas = tk.Canvas(cart_frame)
cart_canvas.pack(expand=True, fill="both")

cart_canvas_frame = tk.Frame(cart_canvas)
cart_canvas.create_window(0, 0, window=cart_canvas_frame, anchor="nw")

# Clear Cart
def clear():
    global total_cart
    for widget in cart_canvas_frame.winfo_children():
        widget.destroy()
    total_cart = 0
    purchase_cart_button.config(text=f"Purchase $0.00")

clear_cart_button = ttk.Button(main_frame, text="Clear Cart", command=clear)
clear_cart_button.grid(row=6, column=3, sticky="nsew")  

# Purchase items
def purchase():
    if total_cart != 0:
        messagebox.showinfo("Purchase", "Thank you for your purchase")
        clear()
    else:
        messagebox.showerror("ERROR", "Please select an item to purchase")

purchase_cart_button = ttk.Button(main_frame, text="Purchase $0.00", padding=10, width=26, command=purchase)
purchase_cart_button.grid(row=7, column=3, sticky="nsew")

# Item Buttons
lemons_button = ttk.Button(item_select_frame, text="Lemon \n$1.00", padding=40, width=6, command=lambda: amount("Lemon", prices.lemon))
lemons_button.grid(row=0, column=0, sticky="nsew")

classic_lemonade_button = ttk.Button(item_select_frame, text="Lemonade \n$2.00", width=20, padding=(0, 50), command=lambda: lemonade_customisation("Classic Lemonade", prices.classic_lemonade))
classic_lemonade_button.grid(row=0, column=1, sticky="nsew")

mango_lemonade_button = ttk.Button(item_select_frame, text="Mango Lemonade \n$2.50", command=lambda: lemonade_customisation("Mango Lemonade", prices.mango_lemonade))
mango_lemonade_button.grid(row=0, column=2, sticky="nsew")

strawberry_lemonade_button = ttk.Button(item_select_frame, text="Strawberry \nLemonade \n$2.50", width=6, command=lambda: lemonade_customisation("Strawberry Lemonade", prices.strawberry_lemonade))
strawberry_lemonade_button.grid(row=1, column=0, sticky="nsew")

blueberry_lemonade_button = ttk.Button(item_select_frame, text="Blueberry \nLemonade \n$2.50", width=20, command=lambda: lemonade_customisation("Blueberry Lemonade", prices.blueberry_lemonade))
blueberry_lemonade_button.grid(row=1, column=1, sticky="nsew")

raspberry_lemonade_button = ttk.Button(item_select_frame, text="Raspberry \nLemonade \n$2.50", width=19, padding=(0, 40), command=lambda: lemonade_customisation("Raspberry Lemonade", prices.raspberry_lemonade))
raspberry_lemonade_button.grid(row=1, column=2, sticky="nsew")

# Initalise Widgets
root.mainloop()