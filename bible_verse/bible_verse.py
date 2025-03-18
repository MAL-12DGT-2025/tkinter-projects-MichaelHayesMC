# Initalising Tkinter GUI for Bible Verse text reader
import tkinter as tk
from tkinter import ttk

# Call txt file and write input to txt file
def button_push():
    bible_verse = input_entry.get()
    with open(textfile, "w") as file:
        file.write(bible_verse)
    with open(textfile, "r") as file:
        bible_verse_label.config(text=file.read())

# Refer txt file as textfile variable
textfile = "bible_verse/bible_verse.txt"

# Initialise Bible Verse text reader Window Menu
root = tk.Tk()
root.title("Bible Verse Text Reader")

# Initalise Widgets
title = ttk.Label(root, text="Bible Verse Text Reader")
prompt_label = ttk.Label(root, text="Please input your Bible Verse:")
input_entry = ttk.Entry(root)
process = ttk.Button(root, text="Process", command=button_push)
bible_verse_label = ttk.Label(root, text="Bible Verse:")

# Place Widgets
title.grid(row=0, pady=10)
prompt_label.grid(row=1, padx=20)
input_entry.grid(row=2)
process.grid(row=3)
bible_verse_label.grid(row=4,pady=20)

root.mainloop()