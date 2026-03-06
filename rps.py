import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"

def play(player_choice):
    computer_choice = random.choice(choices)
    choices_label.config(text=f"You: {player_choice} | Computer: {computer_choice}")

    winner = get_winner(player_choice, computer_choice)

    if winner == "player":
        result_label.config(text="You win!")
    elif winner == "computer":
        result_label.config(text="Computer wins!")
    else:
        result_label.config(text="It's a tie!")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

info_label = tk.Label(root, text="Choose rock, paper, or scissors", font=("Arial", 12))
info_label.pack(pady=5)

choices_label = tk.Label(root, text="", font=("Arial", 12))
choices_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

root.mainloop()