""" tkinter test """
from tkinter import *

def greet(text="Hello World", times=4):
    print((text+" ")* times)
    # ทำf(x)แพ็คได้
def main():
    message = txt.get()
    Label1 = Label(root, text=message).grid(row=3, column=3)

root = Tk()
# App name
root.title("GUI Project")
# display in "root"
# .pack()

# .place(x=0, y=0) คล้าย absolute

# .grid() คล้าย css grid
myLabel1 = Label(root, text="Hello World", fg="red", font=30, bg="yellow").grid(row=0, column=0)
myLabel2 = Label(root, text="Tendou26", fg="blue", font=20, bg="green").grid(row=1, column=1)

# button
btn1 = Button(root, text="Execute", fg="green", font=35, bg="brown", command=main).grid(row=1, column=0)

# message box StringVar() คือตัวเก็บ String
txt = StringVar()
myText = Entry(root, textvariable=txt).grid(row=2, column=0)

root.geometry("500x500+1000+200")
root.mainloop()
