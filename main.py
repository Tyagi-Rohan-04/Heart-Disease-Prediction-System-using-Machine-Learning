from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

root = Tk()
root.title("Heart Attack Prediction")
root.geometry("1450x730+60+80")
root.resizable(False, False)
root.config(bg=background)

#########################################################################################################################

# icon (1)
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

# header section (2)
logo = PhotoImage(file="Images/header.png")
myimage = Label(image=logo, bg=background)
myimage.place(x=0, y=0)

# frame (3)
Heading_entry = Frame(root, width=800, height=190, bg="#df2d4b")
Heading_entry.place(x=600, y=20)

Label(Heading_entry, text="Registration No.", font="arial 13", bg="#df2d4b", fg=framefg).place(x=30, y=0)
Label(Heading_entry, text="Date", font="arial 13", bg="#df2d4b", fg=framefg).place(x=430, y=0)
Label(Heading_entry, text="Patient Name", font="arial 13", bg="#df2d4b", fg=framefg).place(x=30, y=90)
Label(Heading_entry, text="Birth Year", font="arial 13", bg="#df2d4b", fg=framefg).place(x=430, y=90)

Entry_image = PhotoImage(file="Images/Rounded Rectangle 1.png")
Entry_image2 = PhotoImage(file="Images/Rounded Rectangle 2.png")

Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=20, y=30)
Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=430, y=30)

Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=20, y=120)
Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=430, y=120)

Registration = IntVar()
reg_entry = Entry(Heading_entry, textvariable=Registration, width=30, font="arial 15", bg="#0e5363", fg="white", bd=0)
reg_entry.place(x=30, y=45)

Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(Heading_entry, textvariable=Date, width=15, font="arial 15", bg="#0e5363", fg="white", bd=0)
date_entry.place(x=440, y=45)
Date.set(d1)

Name = IntVar()
name_entry = Entry(Heading_entry, textvariable=Name, width=20, font="arial 20", bg="#ededed", fg="#222222", bd=0)
name_entry.place(x=30, y=130)

DOB = IntVar()
dob_entry = Entry(Heading_entry, textvariable=DOB, width=20, font="arial 20", bg="#ededed", fg="#222222", bd=0)
dob_entry.place(x=440, y=130)

#########################################################################################################################

# Body (4)
Detail_entry = Frame(root, width=490, height=260, bg="#dbe0e3")
Detail_entry.place(x=30, y=450)

# Radio Button (5)
Label(Detail_entry, text="sex:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=10)
Label(Detail_entry, text="fbs:", font="arial 13", bg=framebg, fg=framefg).place(x=180, y=10)
Label(Detail_entry, text="exang:", font="arial 13", bg=framebg, fg=framefg).place(x=335, y=10)

# Radio Button Function
def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.Get()==2:
        Gender=0
        return(Gender)
        print(Gender)
    else:
        print(Gender)

def selection2():
    if fbs.get()==1:
        Fbs=1
        return(Fbs)
        print(Fbs)
    elif fbs.Get()==2:
        Fbs=0
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)

def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.Get()==2:
        Exang=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)

gen = IntVar()
R1 = Radiobutton(Detail_entry, text="Male", variable=gen, value=1, command=selection)
R2 = Radiobutton(Detail_entry, text="Female", variable=gen, value=2, command=selection)
R1.place(x=43, y=10)
R2.place(x=93, y=10)

fbs = IntVar()
R3 = Radiobutton(Detail_entry, text="True", variable=fbs, value=1, command=selection2)
R4 = Radiobutton(Detail_entry, text="False", variable=fbs, value=2, command=selection2)
R3.place(x=213, y=10)
R4.place(x=263, y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry, text="Yes", variable=exang, value=1, command=selection3)
R6 = Radiobutton(Detail_entry, text="No", variable=exang, value=2, command=selection3)
R5.place(x=387, y=10)
R6.place(x=430, y=10)

#########################################################################################################################

# Combobox (6)
Label(Detail_entry, text="cp:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=50)
Label(Detail_entry, text="restecg:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=90)
Label(Detail_entry, text="slope:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=130)
Label(Detail_entry, text="ca:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=170)
Label(Detail_entry, text="thal:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=210)

#########################################################################################################################

root.mainloop()