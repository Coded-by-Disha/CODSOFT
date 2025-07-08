import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except:
        return
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    app.clipboard_clear()
    app.clipboard_append(password_entry.get())
    app.update()

def create_stars():
    stars.clear()
    canvas.delete("all")
    for _ in range(120):
        x = random.randint(0, 300)
        y = random.randint(0, 250)
        size = random.choice([1, 2])
        star = canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
        stars.append(star)
    twinkle()

def twinkle():
    for star in stars:
        state = random.choice(["normal", "hidden"])
        canvas.itemconfigure(star, state=state)
    app.after(300, twinkle)

app = tk.Tk()
app.title("Starry Password Generator ✨")
app.geometry("300x250")
app.resizable(False, False)

canvas = tk.Canvas(app, width=300, height=250, highlightthickness=0, bg="#0d0d0d")
canvas.place(x=0, y=0)

stars = []
create_stars()

frame = tk.Frame(app, bg="#0d0d0d")
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Password Length:", fg="white", bg="#0d0d0d", font=("Arial", 10)).pack(pady=5)
length_entry = tk.Entry(frame, bg="#1a1a1a", fg="white", insertbackground="white")
length_entry.pack()

tk.Button(frame, text="Generate", command=generate_password, bg="#333333", fg="white").pack(pady=10)
password_entry = tk.Entry(frame, width=25, bg="#1a1a1a", fg="white", insertbackground="white")
password_entry.pack()
tk.Button(frame, text="Copy", command=copy_password, bg="#333333", fg="white").pack(pady=5)

app.mainloop()
