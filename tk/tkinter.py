""" tkinter test """
from tkinter import *

root = Tk()
# App's Title name
root.title("GUI TEST")

# text
myLabel1 = Label(text="Hello World").pack()
myLabel2 = Label(text="KongRukSiam").pack()

# height & width
root.geometry("500x500")
root.mainloop()
