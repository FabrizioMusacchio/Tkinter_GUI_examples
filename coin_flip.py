"""
Random coin flip GUI application using Tkinter.
Code taken from https://www.askpython.com/python-modules/tkinter/coin-flip-gui
"""
# %% IMPORTS
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
# %% FUNCTIONS
def coinFlip():
    result = np.random.binomial(1, 0.5)
    tfield.delete("1.0", "end")

    if (result == 1):
        tfield.insert(INSERT, " It's ————> HEADS")
        i.config(image=heads)

    else:
        tfield.insert(INSERT, " It's ————> TAILS")
        i.config(image=tails)
# %% MAIN
root = Tk()
root.title("Python Coin Flip")

# load heads image
load = Image.open("images/head.png")
heads = ImageTk.PhotoImage(load)

# load tails image
load = Image.open("images/tail.png")
tails = ImageTk.PhotoImage(load)

i = Label(root, image=heads)
i.pack()

root.geometry("500x500")
b1 = Button(root, text="Toss the Coin", font=("Arial", 10), command=coinFlip, bg='teal', fg='white',
            activebackground="lightblue", padx=10, pady=10)
b1.pack()

# Text Field for Result
tfield = Text(root, width=52, height=5)
tfield.pack()
tfield.insert(INSERT, "Click on the Button.. To Flip the Coin and get the result")

root.mainloop()