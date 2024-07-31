import mysql.connector
from tkinter import messagebox


def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', password="iltpbaf@007")
        mycursor = mydb.cursor()
        messagebox.showinfo("Information", "Connection Established!!!")
    except:
        messagebox.showerror("Connection", "Database connection not established !!")

    try:
        command = "create database heart_data"
        mycursor.execute(command)

        command = "use heart_data"
        mycursor.execute(command)

        command = "create table data(user int auto_increment key not null, Name varchar(50), Date varchar(100), DOB varchar(50), age varchar(100), sex varchar(100), Cp varchar(100), trestbps varchar(100), chol varchar(100), fbs varchar(100), restecg varchar(100), thalach varchar(100), exang varchar(100), oldpeak varchar(100), slope varchar(100), ca varchar(100), thal varchar(100), result varchar(100))"
        mycursor.execute(command)

        command = "insert into data(Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command, (B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register", "New user added successfully !!!!")

    except:
        mycursor.execute("use heart_data")
        mydb = mysql.connector.connect(host="localhost", user="root", password = "iltpbaf@007", database="Heart_Data")
        mycursor = mydb.cursor()

        command = "insert into data(Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command, (B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register", "New user added successfully !!!!")

# Save_Data_MySql("Rohan","08/08/2023","1979","44","1","1","233","233","1","1","233","1","233.0","0","2","1","0")