import tkinter as tk
from tkinter import ttk

def convert():
    result_1.config(text=str(number.get()))

root = tk.Tk()
con_var = tk.IntVar()

window_name = root.title("Temperature Converter")

title = ttk.Label(root, text="Temperature Converter")
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

number = ttk.Entry(root)
number.grid(row=1, column=0, columnspan=2)

c_f_rad = ttk.Radiobutton(root, text="°C to °F", variable=con_var, value=1)
c_f_rad.grid(row=2, column=0)

f_c_rad = ttk.Radiobutton(root, text="°F to °C", variable=con_var, value=2)
f_c_rad.grid(row=2, column=1)

convert_butt = ttk.Button(root, text="Convert", command=convert)
convert_butt.grid(row=3, column=0, columnspan=2)

result_1 = ttk.Label(root, text="")
result_1.grid(row=4, column=0, columnspan=2)

root.mainloop()