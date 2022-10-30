"""
Digital clock GUI application using Tkinter.
Code cloned from https://github.com/Aditya-Bhate/Digital-Clock-using-Python-Tkinter
"""
# %% IMPORTS
from tkinter import *
from tkinter.ttk import *
from time import strftime
# %% MAIN
# creating tkinter window
root = Tk()
root.title('Clock')


# This function is used to  display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='pink')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()