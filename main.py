from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
import matplotlib
from tkinter import messagebox

from backend import *  # importing the ML model from the other file
from MySQL import *    # 

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

# Analysis
def Analysis():
    global prediction

    name = Name.get()
    D1 = Date.get()
    today = datetime.date.today()
    A = today.year-DOB.get()

    try:
        B = selection()
    except:
        messagebox.showerror("missing", "Please select gender !!")
        return
    
    try:
        F = selection2()
    except:
        messagebox.showerror("missing", "Please select fbs !!")
        return
    
    try:
        I = selection3()
    except:
        messagebox.showerror("missing", "Please select exang !!")
        return
    
    try:
        C = int(selection4())
    except:
        messagebox.showerror("missing", "Please select chol !!")
        return
    
    try:
        G = int(restecg_combobox.get())
    except:
        messagebox.showerror("missing", "Please select restecg !!")
        return
    
    try:
        K = int(selection5())
    except:
        messagebox.showerror("missing", "Please select slope !!")
        return
    
    try:
        L = int(ca_combobox.get())
    except:
        messagebox.showerror("missing", "Please select ca !!")
        return
    
    try:
        M = int(thal_combobox.get())
    except:
        messagebox.showerror("missing", "Please select thal !!")
        return
    
    try:
        D = int(trestbps.get())
        E = int(chol.get())
        H = int(thalach.get())
        J = int(oldpeak.get())
    except:
        messagebox.showerror("missing data", "Few missing data entry !!")
        return
    
    print("A is age:",A)
    print("B is gender:",B)
    print("C is cp:",C)
    print("D is trestbps:",D)
    print("E is chol:",E)
    print("F is fbs:",F)
    print("G is restecg:",G)
    print("H is thalach:",H)
    print("I is Exang:",I)
    print("J is oldpeak::",J)
    print("K is slope:",K)
    print("L is ca:",L)
    print("M is thal:",M)

    # First Graph
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.plot(["Sex","fbs","exang"],[B,F,I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas._tkcanvas.place(width=250, height=250, x=600, y=240)

    # Second Graph
    f2 = Figure(figsize=(5,5), dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age","trestbps","chol","thalach"],[A,D,E,H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas2._tkcanvas.place(width=250, height=250, x=860, y=240)

    # Third Graph
    f3 = Figure(figsize=(5,5), dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(["oldpeak","restecg","cp"],[J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas3._tkcanvas.place(width=250, height=250, x=600, y=470)

    # Fourth Graph
    f4 = Figure(figsize=(5,5), dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(["slope","ca","thal"],[K,L,M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas4._tkcanvas.place(width=250, height=250, x=860, y=470)

#########################################################################################################################

# Machine Learning Model

    # input data
    input_data = (A, B, C, D, E, F, G, H, I, J, K, L, M)

    input_data_as_numpy_array = np.asanyarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict (input_data_reshape)
    print(prediction[0])

    
    if(prediction[0]==0):
        print('The person does not have a Heart Disease.')
        report.config(text=f"Report:{0}", fg="#8dc63f")
        report1.config(text=f"{name}, you do not have a heart disease.")
    else:
        print('The person has a Heart Disease.')
        report.config(text=f"Report:{1}", fg="#ed1c24")
        report1.config(text=f"{name}, you have a heart disease.")
    
    
#########################################################################################################################

# info window (operated by info button)
def Info():
    Icon_window = Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+400+100")

    # icon image
    icon_image = PhotoImage(file="Images/info.png")
    Icon_window.iconphoto(False, icon_image)

    # Heading
    Label(Icon_window, text="Information related to the dataset", font="robot 17 bold").pack(padx=20, pady=20)

    # Info
    Label(Icon_window, text="age: age in years", font="arial 11").place(x=20, y=100)
    Label(Icon_window, text="sex: sex(1=male, 0=female)", font="arial 11").place(x=20, y=130)
    Label(Icon_window, text="cp: chest pain type(0=typical angina, 1=atypical angina, 2=non-anginal pain, 3=asymptomatic)", font="arial 11").place(x=20, y=160)
    Label(Icon_window, text="trestbps: resting blood pressure (in mm Hg on admission to the hospital)", font="arial 11").place(x=20, y=190)
    Label(Icon_window, text="chol: serum cholestrolin mg/dl (in mm Hg on admission to the hospital)", font="arial 11").place(x=20, y=220)
    Label(Icon_window, text="fbs: fasting blood sugar > 120mg/dl (1=true, 0=false)", font="arial 11").place(x=20, y=250)
    Label(Icon_window, text="restecg: resting electrocardiographic results (0=normal, 1=having ST-T, 2=hypertrophy)", font="arial 11").place(x=20, y=280)
    Label(Icon_window, text="thalach: maximum heart rate achieved", font="arial 11").place(x=20, y=310)
    Label(Icon_window, text="exang: exercise induced angina (1=yes, 0=no)", font="arial 11").place(x=20, y=340)
    Label(Icon_window, text="oldpeak: ST depression induced by exercise relative to rest", font="arial 11").place(x=20, y=370)
    Label(Icon_window, text="slope: the slope of the peak exercise ST segment (0=upsloping, 1=flat, 2=downsloping)", font="arial 11").place(x=20, y=400)
    Label(Icon_window, text="ca: number of major vessels (0-3) colored by flourosopy", font="arial 11").place(x=20, y=430)
    Label(Icon_window, text="thal: 0=normal, 1=fixed defect, 2=reversable defect", font="arial 11").place(x=20, y=460)

    Icon_window.mainloop()

# A function to exit the application
def logout():
    root.destroy()

# Clear (with the help of clear we can clear multiple fields at once)
def Clear():
    Name.get('')
    DOB.get('')
    trestbps.get('')
    chol.get('')
    thalach.set('')
    oldpeak.set('')

# Function to save the report.

def Save():
    B2 = Name.get()
    C2 = Date.get()
    D2 = DOB.get()

    today = datetime.date.today()
    E2 = today.year-DOB.get()

    try:
        F2 = selection()
    except:
        messagebox.showerror("Missing Data", " Plese select gender!")

    try:
        J2 = selection2()
    except:
        messagebox.showerror("Missing Data", " Plese select fbs!")

    try:
        M2 = selection3()
    except:
        messagebox.showerror("Missing Data", " Plese select Exang!")

    try:
        G2 = selection4()
    except:
        messagebox.showerror("Missing Data", " Plese select cp!")

    try:
        K2 = restecg_combobox.get()
    except:
        messagebox.showerror("Missing Data", " Plese select restecg!")

    try:
        O2 = selection5()
    except:
        messagebox.showerror("Missing Data", " Plese select slope!")

    try:
        P2 = ca_combobox.get()
    except:
        messagebox.showerror("Missing Data", " Plese select ca!")

    try:
        Q2 = thal_combobox.get()
    except:
        messagebox.showerror("Missing Data", " Plese select thal!")

    H2 = trestbps.get()
    I2 = chol.get()
    L2 = thalach.get()
    N2 = float(oldpeak.get())

    print(B2)
    print(C2)
    print(D2)
    print(E2)
    print(F2)
    print(G2)
    print(H2)
    print(I2)
    print(J2)
    print(K2)
    print(L2)
    print(M2)
    print(N2)
    print(O2)
    print(P2)
    print(Q2)

    Save_Data_MySql(B2, C2, int(D2), int(E2), int(F2), int(G2), int(H2), int(I2), int(J2), int(K2), int(L2), int(M2), int(N2), int(O2), int(P2), int(Q2), int(prediction[0]))

    Clear()

    root.destroy()
    os.system("main.py")

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

Name = StringVar()
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

def selection4():
    input = cp_combobox.get()
    if input=="0 = typical angina":
        return(0)
    elif input=="1 = atypical angina":
        return(1)
    elif input=="2 = non-anginal pain":
        return(2)
    elif input=="3 = asyptomatic":
        return(3)
    else:
        print(Exang)

def selection5():
    input = slope_combobox.get()
    if input=="0 = upsloping":
        return(0)
    elif input=="1 = flat":
        return(1)
    elif input=="2 = downsloping":
        return(2)
    else:
        print(Exang)

cp_combobox = Combobox(Detail_entry, values=['0 = typical angina','1 = atypical angina','2 = non-anginal pain','3 = asyptomatic'], font="arial 12", state="r", width=14)
restecg_combobox = Combobox(Detail_entry, values=['0','1','2'], font="arial 12", state="r", width=11)
slope_combobox = Combobox(Detail_entry, values=['0 = upsloping','1 = flat', '2 = downsloping'], font="arial 12", state="r", width=12)
ca_combobox = Combobox(Detail_entry, values=['0','1','2','3','4'], font="arial 12", state="r", width=14)
thal_combobox = Combobox(Detail_entry, values=['0','1','2','3'], font="arial 12", state="r", width=14)

cp_combobox.place(x=50, y=50)
restecg_combobox.place(x=80, y=90)
slope_combobox.place(x=70, y=130)
ca_combobox.place(x=50, y=170)
thal_combobox.place(x=50, y=210)

#########################################################################################################################

# Data Entry Box (7)
Label(Detail_entry, text="Smoking:", font="arial 13", width=7, bg="#dbe0e3", fg="black").place(x=240, y=50)
Label(Detail_entry, text="trestbps:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=90)
Label(Detail_entry, text="chol:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=130)
Label(Detail_entry, text="thalach:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=170)
Label(Detail_entry, text="oldpeak:", font="arial 13", width=7, bg=framebg, fg=framefg).place(x=240, y=210)

trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

trestbps_entry = Entry(Detail_entry, textvariable=trestbps, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
chol_entry = Entry(Detail_entry, textvariable=chol, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
thalach_entry = Entry(Detail_entry, textvariable=thalach, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
oldpeak_entry = Entry(Detail_entry, textvariable=oldpeak, width=10, font="arial 15", bg="#ededed", fg="#222222", bd=0)
trestbps_entry.place(x=320, y=90)
chol_entry.place(x=320, y=130)
thalach_entry.place(x=320, y=170)
oldpeak_entry.place(x=320, y=210)

#########################################################################################################################

# Report (8)
square_report_image = PhotoImage(file="Images/Report.png")
report_background = Label(image=square_report_image, bg=background)
report_background.place(x=1120, y=340)

report = Label(root, font="arial 25 bold", bg="white", fg="#8dc63f")
report.place(x=1170, y=550)

report1 = Label(root, font="arial 10 bold", bg="white")
report1.place(x=1130, y=610)

#########################################################################################################################

# Graphs (9)
graph_image = PhotoImage(file="Images/graph.png")
Label(image=graph_image).place(x=600, y=270)
Label(image=graph_image).place(x=860, y=270)
Label(image=graph_image).place(x=600, y=500)
Label(image=graph_image).place(x=860, y=500)

#########################################################################################################################

# Analysis Button (10)
analysis_button = PhotoImage(file="Images/Analysis.png")
Button(root, image=analysis_button, bg=background, cursor='hand2', bd=0, command=Analysis).place(x=1130, y=240)

# info button
info_button = PhotoImage(file="Images/info.png")
Button(root, image=info_button, bg=background, cursor='hand2', bd=0, command=Info).place(x=10, y=240)

# save button
save_button = PhotoImage(file="Images/save.png")
Button(root, image=save_button, bg=background, cursor='hand2', bd=0, command=Save).place(x=1370, y=250)

#########################################################################################################################

# Smoking and Non smoking button (11)
button_mode = True
choice = "smoking"

def changemode():
    global button_mode
    global choice
    
    if button_mode:
        choice = "non_smoking"
        mode.config(image=non_smoking_icon, activebackground="white")
        button_mode = False

    else:
        choice = "smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode = True
    
    print(choice)

smoking_icon = PhotoImage(file="Images/smoker.png")
non_smoking_icon = PhotoImage(file="Images/non-smoker.png")

mode = Button(root, image=smoking_icon, bg="#dbe0e3", bd=0, cursor="hand2", command=changemode)
mode.place(x=350, y=495)

#########################################################################################################################

# Logout Button (12)
logout_icon = PhotoImage(file="Images/logout.png")
logout_button = Button(root, image=logout_icon, bg="#df2d4b", cursor="hand2", bd=0, command=logout)
logout_button.place(x=1405, y=10)

#########################################################################################################################

root.mainloop()