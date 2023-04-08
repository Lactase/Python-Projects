# Import QR Libraries
import qrcode
from tkinter import *
import tkinter as ttk
from PIL import ImageTk, Image


# Function to create QR Code
def generate_qr_code(event=None):
  # Gets text from text box
  text = link_var.get()
  filename = "QR_CODE.png"
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  #Creates QR CODE
  qr.add_data(text)
  #Makes QR CODE size fit
  qr.make(fit=True)

  # Change color of QR CODE
  img = qr.make_image(back_color=("Black"), fill_color=("White"))
  # Saves img of QR CODE
  img.save(filename)
  # Opens image in TK
  img = ImageTk.PhotoImage(Image.open("QR_CODE.png"))
  ImageBox.configure(image=img)
  ImageBox.image = img


# Tkinter
root = Tk()
# Creates Frame
frm = ttk.Frame(root)
# Turns frame into grid
frm.grid()
# Window Title
root.title("QR CODE GENERATOR")
# Variables
link_var = ttk.StringVar()
Filename_var = ttk.StringVar()
# Creates Labels
Text = ttk.Label(frm, text="Enter links or text").grid(column=0, row=0)
ImageBox = ttk.Label(frm)
# Creates Entry Box
Link = ttk.Entry(frm, textvariable=link_var).grid(column=0, row=2)
# Creates Button
Generate = ttk.Button(frm, text="Generate",
                      command=generate_qr_code).grid(column=1, row=2)
# Grid
ImageBox.grid(column=0, row=3)
# Key binds
root.bind("<Return>", generate_qr_code)

root.mainloop()
