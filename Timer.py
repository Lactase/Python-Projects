import time
from tkinter import *
import tkinter as ttk
import datetime
from datetime import timedelta


def current_time():
    curr_time = time.strftime("%H:%M:%S", get_current_time())
    time_label.configure(text = curr_time)
    frm1.after(100, current_time)

def get_current_time():
    return time.localtime()

def elapsed_time():
    global start_time
    start_time = datetime.datetime.now()
    elapse()

def elapse():
    global id
    curr_time = datetime.datetime.now()
    elapsed_label.configure(text = curr_time - start_time)
    id = frm1.after(100,elapse)

def stop_time():
    frm1.after_cancel(id)
    

        


    

root = Tk()
# Creates Frame
frm1 = ttk.Frame(root)
frm2 = ttk.Frame(root)

frm1 = LabelFrame(root, text="Current Time!", bg="white", padx=75, pady=10)
frm2 = LabelFrame(root, text="Stop Watch!", bg="white", padx=50, pady=16)

# Turns frame into grid
root.geometry("230x200")

frm1.grid()
frm2.grid()
# Window Title
root.title("Timer")

# Variables

# Creates number counter label title
get_time = ttk.Button(frm1, text = "Current time", command = current_time, pady = 5).grid(column= 1 , row = 2)
elapsed_time_button = ttk.Button(frm2, text = "Start Time", command = elapsed_time, pady = 5).grid(column= 0 , row = 1)
elapsed_stop_button = ttk.Button(frm2, text = "Stop Time", command = stop_time, pady = 5).grid(column= 2 , row = 1, )



elapsed_label= ttk.Label(frm2, bg= "white")
elapsed_label.grid(column = 0, row = 3, columnspan= 3)

time_label = ttk.Label(frm1, bg = "white")
time_label.grid(column = 1, row = 3)



root.mainloop()