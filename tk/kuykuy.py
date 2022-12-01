import tkinter as tk

fon = tk.Tk()
fon.title("Edok Fueng")
fon.geometry("500x500+500+200")
fon.resizable(False, False)

def new_win():
    # lee = tk.Tk()
    # lee.mainloop()
    label = tk.Label(fon, text="Hey!").pack()

def get_var():
    num = int(value1.get())
    print(num)

# widget
label1 = tk.Label(fon, text="Fon1")
label1.pack()

value1 = tk.StringVar()
entry1 = tk.Entry(fon, width=5, textvariable=value1).pack()
button = tk.Button(fon, text="Press me", command=get_var)
button.pack()
fon.mainloop()
