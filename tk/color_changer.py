""" tkinter """
from tkinter import *
import tkinter.messagebox
# color changer, filedialog
from tkinter.colorchooser import *
from tkinter.filedialog import *
def main():
    """ color changer """
    def select_clr():
        color = askcolor()
        print(color[1])
        myLabel = Label(text="Hello Python", bg=color[1]).pack()
    def select_file():
        fileopen = askopenfile()
        fileContent = open(fileopen, encoding='UTF-8')
        myLabel = Label(text=fileopen).pack()

    root = Tk()
    root.title("Color Changer")
    root.geometry('500x500')
    btn1 = Button(root, text="Choose color", command=select_clr).pack()
    btn2 = Button(root, text="Choose file", command=select_file).pack()
    root.mainloop()
main()
