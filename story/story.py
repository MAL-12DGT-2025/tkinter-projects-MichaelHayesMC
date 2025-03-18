import tkinter as tk
from tkinter import ttk

def button_push():
    bible_verse = input_entry.get()
    with open("bible_verse.txt", "w") as file:
        file.write(bible_verse)
    with open("bible_verse.txt", "r") as file:
        bible_verse_label.config(text=file.read())

root = tk.Tk()
root.title("Bible Verse Text Reader")

title = ttk.Label(root, text="Bible Verse Text Reader")
title.grid(row=0, pady=10)

prompt_label = ttk.Label(root, text="Please input your Bible Verse:")
prompt_label.grid(row=1, padx=20)

input_entry = ttk.Entry(root)
input_entry.grid(row=2)

process = ttk.Button(root, text="Process", command=button_push)
process.grid(row=3)

bible_verse_label = ttk.Label(root, text="Bible Verse:")
bible_verse_label.grid(row=4,pady=20)

root.mainloop()