import tkinter as tk
from tkinter import messagebox
import math


def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror('Input error', 'Please enter valid numbers')


def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror('Input error', 'Please enter valid numbers')


def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror('Input error', 'Please enter valid numbers')


def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            raise ZeroDivisionError
        result.set(float(entry1.get()) / denominator)
    except ValueError:
        messagebox.showerror('Input error', 'Please enter valid numbers')
    except ZeroDivisionError:
        messagebox.showerror('Math error', 'Division by zero')


def square_root():
    try:
        value = float(entry1.get())
        if value < 0:
            raise ValueError('Negative input')
        result.set(math.sqrt(value))
    except ValueError:
        messagebox.showerror('Input error', 'Please enter a non-negative number in the first field')


root = tk.Tk()
root.title('Calculator')

entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, width=20)
result_label.grid(row=2, column=0, columnspan=4, pady=5)

btn_add = tk.Button(root, text='+', width=5, command=add)
btn_add.grid(row=3, column=0, padx=5, pady=5)
btn_sub = tk.Button(root, text='-', width=5, command=subtract)
btn_sub.grid(row=3, column=1, padx=5, pady=5)
btn_mul = tk.Button(root, text='*', width=5, command=multiply)
btn_mul.grid(row=3, column=2, padx=5, pady=5)
btn_div = tk.Button(root, text='/', width=5, command=divide)
btn_div.grid(row=3, column=3, padx=5, pady=5)
btn_sqrt = tk.Button(root, text='√', width=5, command=square_root)
btn_sqrt.grid(row=4, column=0, columnspan=4, pady=5)

root.mainloop()

