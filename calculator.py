import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def divide():
    try:
        if float(num2.get()) == 0:
            messagebox.showerror("Error", "Division by zero")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Basic Calculator")

tk.Label(root, text="First number:").grid(row=0, column=0)
num1 = tk.Entry(root)
num1.grid(row=0, column=1)

tk.Label(root, text="Second number:").grid(row=1, column=0)
num2 = tk.Entry(root)
num2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=4, column=1)

root.mainloop()