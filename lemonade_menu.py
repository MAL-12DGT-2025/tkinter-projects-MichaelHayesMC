import tkinter as tk
from tkinter import ttk

lemon_price = 1.50
icecube_price = 0.50
lemonade_price = 2.00

def price_calc(i):
    amount = float(count.get())
    print(float(amount))
    price1.config(text=f"${amount*lemon_price: .2f}")

root = tk.Tk()
root.title("Lemonade Stand Menu")

count = tk.IntVar()

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

selected_1 = ttk.Checkbutton(root, onvalue=1, offvalue=0)
selected_1.grid(row=2, column=0)

selected_2 = ttk.Checkbutton(root, onvalue=1, offvalue=0)
selected_2.grid(row=3, column=0)

selected_3 = ttk.Checkbutton(root, onvalue=1, offvalue=0)
selected_3.grid(row=4, column=0)

price1 = ttk.Label(root, text="$0.00")
price1.grid(row=2, column=3, padx=10)

price2 = ttk.Label(root, text="$0.00")
price2.grid(row=3, column=3, padx=10)

price3 = ttk.Label(root, text="$0.00")
price3.grid(row=4, column=3, padx=10)

item1 = ttk.Label(root, text="50g Lemons")
item1.grid(row=2, column=2, padx=5)

item2 = ttk.Label(root, text="Ice Cubes")
item2.grid(row=3, column=2, padx=5)

item3 = ttk.Label(root, text="250ml Lemonade")
item3.grid(row=4, column=2, padx=5)

quantity1 = ttk.Entry(root, width=5, textvariable=count)
quantity1.grid(row=2, column=1, padx=5)
quantity1.bind("<Return>", price_calc)

quantity2 = ttk.Entry(root, width=5)
quantity2.grid(row=3, column=1, padx=5)

quantity3 = ttk.Entry(root, width=5)
quantity3.grid(row=4, column=1, padx=5)

purchase_L = ttk.Button(root, text="(Cost)")
purchase_L.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()