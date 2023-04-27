from tkinter import *
import tkinter as ttk


counter = 0

def label_config():
    label.configure(text = f"Counter: {counter}")

def add():
    global counter
    counter += 1
    label_config()

def minus():
    global counter
    counter -= 1
    label_config()

def half():
    global counter
    counter = counter // 2
    label_config()

def double():
    global counter
    counter = counter * 2
    label_config()

# Tkinter
root = Tk()
# Creates Frame
frm = ttk.Frame(root)
# Turns frame into grid
root.geometry("250x200")

frm.grid()
# Window Title
root.title("Counter")

# Variables
counter_var = ttk.IntVar()

# Creates number counter label title
num_counter_label = ttk.Label(frm, text= "Number Counter!", font= ("Arial", 14), pady = 20).grid(column = 0, row = 0, columnspan= 4)

# Creates buttons
addition = ttk.Button(frm, text= "+", command = add, height = 2, width = 4, font= ("Arial", 10)).grid(column= 0, row = 2, padx=10)
subtract = ttk.Button(frm, text= "-", command = minus, height = 2, width = 4, font= ("Arial", 10)).grid(column=1, row = 2, padx=10)
halved = ttk.Button(frm, text= "½", command = half, height = 2, width = 4, font= ("Arial", 10)).grid(column=2, row = 2, padx=10)
halved = ttk.Button(frm, text= "x2", command = double, height = 2, width = 4, font= ("Arial", 10)).grid(column= 3, row = 2, padx=10)

# Creates label for counter
label = ttk.Label(frm, text = f"Counter: {counter}", font=("Arial", 14), pady= 20)
# Assigns counter label to the grid
label.grid(column= 0, row= 3, columnspan= 4)

root.mainloop()
