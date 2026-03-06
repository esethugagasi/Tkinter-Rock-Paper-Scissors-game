import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]

def play(player_choice):
    computer_choice = random.choice(choices)
    result_label.config(text=f"You chose {player_choice}, computer chose {computer_choice}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

info_label = tk.Label(root, text="Choose rock, paper, or scissors", font=("Arial", 12))
info_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10)
scissors_button.grid(row=0, column=2, padx=5)


root.mainloop()