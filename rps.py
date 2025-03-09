import random
import tkinter as tk
from tkinter import ttk

score = 0

def button_click(event):
    global score 
    prompt.configure(text=f"You clicked {event}")
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    if computer_choice == event:
        prompt.configure(text="It's a tie!")
    elif computer_choice == "Paper" and event == "Rock":
        prompt.configure(text="Computer wins!")
    elif computer_choice == "Scissors" and event == "Rock":
        prompt.configure(text="You win!")
        score = score + 1
    elif computer_choice == "Rock" and event == "Scissors":
        prompt.configure(text="Computer wins!")
    elif computer_choice == "Paper" and event == "Scissors":
        prompt.configure(text="You win!")
        score = score + 1
    elif computer_choice == "Scissors" and event == "Paper":
        prompt.configure(text="Computer wins!")
    elif computer_choice == "Rock" and event == "Paper":
        prompt.configure(text="You win!")
        score = score + 1
    score_l.configure(text=f"Score: {score}")

root = tk.Tk()
root.title("Rock Paper Scissors")
title = tk.Label(root, text="Rock, Paper, \nScissors Game")
title.grid(row=0, column=1)

prompt = ttk.Label(root, text="Make a choice")
prompt.grid(row=1, column=1)

choice = tk.StringVar()

rock = ttk.Button(root, text="Rock", command=lambda:button_click("Rock"))
rock.grid(row=2,column=0)

paper = ttk.Button(root, text="Paper", command=lambda:button_click("Paper"))
paper.grid(row=2,column=1)

scissors = ttk.Button(root, text="Scissors", command=lambda:button_click("Scissors"))
scissors.grid(row=2,column=2)

score_l = ttk.Label(root, text=f"Score: {score}")
score_l.grid(row=3, column=1)

root.mainloop()