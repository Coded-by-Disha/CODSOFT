import tkinter as tk

def calculate():
    try:
        number1 = float(input1.get())
        number2 = float(input2.get())
        operator = selected_operation.get()

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "/":
            if number2 != 0:
                result = number1 / number2
            else:
                result_display.configure(state="normal")
                result_display.delete(0, tk.END)
                result_display.insert(0, "Error (÷ by 0)")
                result_display.configure(state="readonly")
                return
        else:
            result = "Invalid Op"

        result_display.configure(state="normal")
        result_display.delete(0, tk.END)
        result_display.insert(0, round(result, 2))
        result_display.configure(state="readonly")

    except:
        result_display.configure(state="normal")
        result_display.delete(0, tk.END)
        result_display.insert(0, "Invalid Input")
        result_display.configure(state="readonly")

app = tk.Tk()
app.title("Calculator")
app.geometry("320x400")
app.configure(bg="#fff9e6")

tk.Label(app, text="Calculator", font=("Segoe UI", 16, "bold"), bg="#fff9e6", fg="#4d3300").pack(pady=(15, 10))

result_display = tk.Entry(app, font=("Segoe UI", 14), justify="center", bd=3, state="readonly", disabledbackground="#fff1cc", disabledforeground="#333")
result_display.pack(pady=10, ipadx=5, ipady=5)

tk.Label(app, text="Enter first number", font=("Segoe UI", 10, "bold"), bg="#fff9e6", fg="#333").pack(pady=(10, 5))
input1 = tk.Entry(app, font=("Segoe UI", 12), bd=2, relief="groove")
input1.pack(pady=5)

tk.Label(app, text="Enter second number", font=("Segoe UI", 10, "bold"), bg="#fff9e6", fg="#333").pack(pady=5)
input2 = tk.Entry(app, font=("Segoe UI", 12), bd=2, relief="groove")
input2.pack(pady=5)

tk.Label(app, text="Choose operation", font=("Segoe UI", 10, "bold"), bg="#fff9e6", fg="#333").pack(pady=10)

selected_operation = tk.StringVar()
selected_operation.set("+")

for symbol in ["+", "-", "*", "/"]:
    tk.Radiobutton(
        app,
        text=symbol,
        variable=selected_operation,
        value=symbol,
        font=("Segoe UI", 11),
        bg="#fff9e6",
        fg="#333",
        activebackground="#ffe0a3",
        selectcolor="#ffecc2"
    ).pack()

tk.Button(
    app,
    text="Calculate",
    font=("Segoe UI", 11, "bold"),
    bg="#ffb84d",
    fg="white",
    activebackground="#e69500",
    padx=10,
    pady=5,
    bd=0,
    command=calculate
).pack(pady=20)

app.mainloop()
