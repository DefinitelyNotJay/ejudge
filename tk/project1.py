""" tkinter """
from tkinter import *

def text():
    print('Hey')
def noway():
    message = txt.get()
    print(message)
root = Tk()
root.title('Project')
root.geometry('500x500')

myLabel = Label(root, bg="#ffa8a8", text="Start", font=30)
myLabel.grid(row=0, column=0)
myBtn = Button(root, bg="#f03e3e", text="Submit", font=40, fg="#212529", command=noway)
myBtn.grid(row=1, column=2)
txt = StringVar()
myText = Entry(root, textvariable=txt).grid(row=3, column=3)

root.mainloop()
