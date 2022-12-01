import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Fueng & Fon")
root.geometry("300x500")
""" 2 inputs """
# Num1 input
num1 = tk.ttk.Entry(root, width=5, justify="center")
num1.pack()
# Num2 input
num2 = tk.ttk.Entry(root, width=5, justify="center")
num2.pack()

""" create operation """
# +
btn_plus = tk.ttk.Button(root, text="+", width=2)
btn_plus.pack()
# -
btn_minus = tk.ttk.Button(root, text="-", width=2)
btn_minus.pack()
# x
btn_multi = tk.ttk.Button(root, text="x", width=2)
btn_multi.pack()
# /
btn_div = tk.ttk.Button(root, text="/", width=2)
btn_div.pack()

# calculate function

root.mainloop()
