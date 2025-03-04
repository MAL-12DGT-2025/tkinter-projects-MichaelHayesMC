import tkinter as tk

root = tk.Tk()

title = tk.Label(root, text="Temperature\nConverter")
title.grid(row=0, column=0)

number = tk.Entry(root)
number.grid(row=1, column=0)

root.mainloop()