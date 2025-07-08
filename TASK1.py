import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def add_task():
    task = task_input.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("😅 Oops!", "Please type something to add.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("⚠️ No Selection", "Please select a task to delete.")

def mark_task_done():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        task_listbox.insert(index, f"✓ {task}")
        save_tasks()
    except:
        messagebox.showwarning("⚠️ No Selection", "Please select a task.")

def clear_all_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)
        save_tasks()

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for i in range(task_listbox.size()):
            file.write(task_listbox.get(i) + "\n")

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    if dark_mode:
        bg_color = "#2c2c2c"
        fg_color = "#f2f2f2"
        box_bg = "#3c3c3c"
        btn_bg = "#444"
        sel_bg = "#555"
    else:
        bg_color = "#f9f9fb"
        fg_color = "#333"
        box_bg = "#ffffff"
        btn_bg = "#6c63ff"
        sel_bg = "#a3c9f7"

    window.configure(bg=bg_color)
    title_label.configure(bg=bg_color, fg=fg_color)
    task_input.configure(bg=box_bg, fg=fg_color, insertbackground=fg_color)
    task_listbox.configure(bg=box_bg, fg=fg_color, selectbackground=sel_bg, selectforeground=fg_color)
    button_frame.configure(bg=bg_color)
    theme_button.configure(bg=btn_bg, fg="white", activebackground=btn_bg)
    clear_button.configure(bg=btn_bg, fg="white", activebackground=btn_bg)

    for btn in action_buttons:
        btn.configure(bg=btn_bg, fg="white", activebackground=btn_bg)

window = tk.Tk()
window.title("🌸 Disha’s To-Do List")
window.geometry("420x530")

dark_mode = False

title_label = tk.Label(window, text="📋 My To-Do List", font=("Segoe UI", 18, "bold"))
title_label.pack(pady=20)

task_input = tk.Entry(window, font=("Segoe UI", 12), width=30, bd=2, relief="groove")
task_input.pack(pady=10)

task_listbox = tk.Listbox(window, width=35, height=10, font=("Segoe UI", 11))
task_listbox.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=15)

button_style = {
    "font": ("Segoe UI", 10, "bold"),
    "bd": 0,
    "padx": 12,
    "pady": 6
}

add_btn = tk.Button(button_frame, text="➕ Add", command=add_task, **button_style)
delete_btn = tk.Button(button_frame, text="🗑️ Delete", command=delete_task, **button_style)
done_btn = tk.Button(button_frame, text="✅ Done", command=mark_task_done, **button_style)

add_btn.pack(side=tk.LEFT, padx=6)
delete_btn.pack(side=tk.LEFT, padx=6)
done_btn.pack(side=tk.LEFT, padx=6)

action_buttons = [add_btn, delete_btn, done_btn]

theme_button = tk.Button(window, text="🌙 Toggle Theme", font=("Segoe UI", 10, "bold"), bd=0, command=toggle_theme)
theme_button.pack(pady=5)

clear_button = tk.Button(window, text="🧹 Clear All", font=("Segoe UI", 10, "bold"), bd=0, command=clear_all_tasks)
clear_button.pack(pady=5)

load_tasks()
apply_theme()
window.mainloop()