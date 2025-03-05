import tkinter as tk
from tkinter import ttk

def convert(event):
    num=int(number.get())

    if int(con_var.get()) == 1: # Celsius to Farenheit
        result = (num * 9/5) + 32
        result_l.config(text=f"{num}°C is equal to {result:.0f}°F")

    elif int(con_var.get()) == 2: # Farenheit to Celsius:
        result = (num - 32) * 5/9
        result_l.config(text=f"{num}°F is equal to {result:.0f}°C")


root = tk.Tk()
con_var = tk.IntVar(value = 1)

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

result_l = ttk.Label(root, text="")
result_l.grid(row=4, column=0, columnspan=2)

root.bind("<Return>", convert)

root.mainloop()