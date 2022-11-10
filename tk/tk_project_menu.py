""" Menu in Tkinter """
from tkinter import *
import tkinter.messagebox
def main():
    """ main function """
    window = Tk()
    window.title("Test Menu")
    window. geometry("500x500")

    # create menu
    myMenu = Menu()
    window.config(menu=myMenu)

    # show about me
    def about_me():
        tkinter.messagebox.showinfo("info", "Developed by Jay")
    # create new window
    def showWindow():
        newTab = Tk()
        newTab.title("New Window")
        newTab.mainloop()
    # exitProgram
    def exitProgram():
        
        window.destroy()

    # add sub-menu
    sub_menu = Menu()
    sub_menu.add_command(label="New Window", command=showWindow)
    sub_menu.add_command(label="Open File")
    sub_menu.add_command(label="Save")
    sub_menu.add_command(label="About", command=about_me)
    sub_menu.add_command(label="Exit", command=exitProgram)

    # add menu
    myMenu.add_cascade(label="File", menu=sub_menu)
    myMenu.add_cascade(label="Edit")
    myMenu.add_cascade(label="View")

    window.mainloop()
main()
