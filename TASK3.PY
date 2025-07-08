import tkinter as tk
import random

options = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(options)

    user_label.config(text="You chose: " + user_choice)
    computer_label.config(text="Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!", fg="#ff66cc")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result_label.config(text="You win!", fg="#33ff99")
        user_score += 1
    else:
        result_label.config(text="You lose!", fg="#ff5050")
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def reset_game():
    user_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")
    result_label.config(text="")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def new_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    reset_game()

win = tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("360x420")

tie_dye_colors = ["#ffccff", "#ccffff", "#ffffcc", "#ffcccc", "#ccffcc"]
current_color = 0

def change_bg():
    global current_color
    current_color = (current_color + 1) % len(tie_dye_colors)
    new_color = tie_dye_colors[current_color]
    win.config(bg=new_color)
    title_label.config(bg=new_color)
    user_label.config(bg=new_color)
    computer_label.config(bg=new_color)
    result_label.config(bg=new_color)
    score_label.config(bg=new_color)
    btn_frame.config(bg=new_color)
    play_again_btn.config(bg=new_color)
    new_game_btn.config(bg=new_color)
    win.after(1000, change_bg)

title_label = tk.Label(win, text="Choose Rock, Paper, or Scissors", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

btn_frame = tk.Frame(win)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", width=10, bg="#ff9999", fg="white", command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, bg="#99ccff", fg="white", command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, bg="#ccff99", fg="black", command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

user_label = tk.Label(win, text="You chose: ")
user_label.pack(pady=5)

computer_label = tk.Label(win, text="Computer chose: ")
computer_label.pack(pady=5)

result_label = tk.Label(win, text="", font=("Arial", 10, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(win, text="Score - You: 0  Computer: 0")
score_label.pack()

play_again_btn = tk.Button(win, text="Play Again", bg="#e6e6fa", command=reset_game)
play_again_btn.pack(pady=5)

new_game_btn = tk.Button(win, text="New Game", bg="#ffe6e6", command=new_game)
new_game_btn.pack(pady=5)

change_bg()
win.mainloop()
