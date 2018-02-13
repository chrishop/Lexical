# !/usr/bin/python3

# is a message box for if the system is installed successfully
import tkinter
from tkinter import messagebox

def showpass():
    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    # message box display
    messagebox.showinfo("Lexical", "Installation complete")

def showfail():
    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    # message box display
    messagebox.showerror("Lexical", "Installation failed")