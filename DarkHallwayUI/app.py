# DarkHallway Login Screen
# By frickengames
# Version 0.1
# 13/03/23

import random
import os
import sys
import socket
import select
import errno
import getpass
import calendar
import time
import threading
import customtkinter
import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
from splashtext import splash
import os

# Set global application background color
background = '#333538'



# Setup the main tkinter window
root = customtkinter.CTk()
root.geometry('700x480')
root.resizable(False, False)
root.configure(fg_color=background)
root.title("Login into DH")

# Load the application icon
ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Set themes for CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "Dark" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")

# Load the login background image
image = Image.open("login.png")
img = ImageTk.PhotoImage(image)

label1 = Label(image=img, bg='#333538')
label1.image = img
label1.place(relx = -0.003, rely = 0.5, anchor='w')

# Load the game logo
image2 = Image.open("logo.png")
img2 = ImageTk.PhotoImage(image2)

label1 = Label(image=img2, bg='#333538')
label1.image2 = img2
label1.place(relx = 0.75, rely = 0.23, anchor='center')

# Random Splash Text
splashno = random.randrange(1, 4)

splashs = Label(text=splash[splashno], bg='#333538', fg='#ffffff')
splashs.place(relx = 0.75, rely = 0.36, anchor='center')

# Define the username entry field
UsrVar = customtkinter.StringVar()
user = customtkinter.CTkEntry(master=root, placeholder_text="Username", textvariable=UsrVar, width=200)
user.place(relx = 0.75, rely = 0.5, anchor = 'center')

# Define the password entry field
PassVar = customtkinter.StringVar()
password = customtkinter.CTkEntry(master=root, placeholder_text="Password", textvariable=PassVar, width=200)
password.place(relx = 0.75, rely = 0.6, anchor = 'center')

#def checkbox_event():
    #create pop up to enter new IP and Port

BoxVar = customtkinter.IntVar()
checkbox = customtkinter.CTkCheckBox(master=root, text="Enter new IP and Port?", variable=BoxVar, onvalue=1, offvalue=0)
checkbox.place(relx = 0.722, rely = 0.67, anchor = 'center')





def popupmsg():
    popup = customtkinter.CTk()
    popup.geometry('300x100')
    popup.resizable(False, False)
    popup.wm_title("!")
    label12 = customtkinter.CTkLabel(popup, text="Incorrect Username or Password")
    label12.pack(side="top", fill="x", pady=10)
    B1 = customtkinter.CTkButton(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def RootIPDef():
    RootIP = customtkinter.CTk()
    RootIP.geometry('300x100')
    RootIP.resizable(True, True)
    RootIP.wm_title("Submit New Details")
    label12 = customtkinter.CTkLabel(RootIP, text="Enter New Port and IP")
    label12.pack(side="top", fill="x", pady=10)

    # Define the IP entry field
    IPVar = customtkinter.StringVar()
    user1 = customtkinter.CTkEntry(master=RootIP, placeholder_text="IP", textvariable=IPVar, width=200)
    user1.place(relx = 0.75, rely = 0.5, anchor = 'center')
    user1.pack()

    # Define the Port entry field
    
    PortVar = customtkinter.IntVar()
    Port = customtkinter.CTkEntry(master=RootIP, placeholder_text="Port", textvariable=PortVar, width=200)
    Port.place(relx = 0.75, rely = 0.6, anchor = 'center')
    Port.pack()

    B1 = customtkinter.CTkButton(RootIP, text="Submit", command=lambda:[NewPort(IPVar, PortVar),RootIP.destroy()])
    B1.pack()

    IP = IPVar.get()
    Port1 = PortVar.get()
    print(IP)
    print(Port1)

    RootIP.mainloop()

def NewPort(IPVar, PortVar):
    IP = IPVar.get()
    Port1 = PortVar.get()
    myfile = open("Data/data.txt", "r")
    filedata = myfile.read().split(":")
    My_Username = filedata[0]
    Password = filedata[1]
    myfile.close()

    print(My_Username)
    print(Password)
    print(IP)
    print(PortVar)

    myfile = open("Data/data.txt", 'w')
    myfile.write(f"{My_Username}:")
    myfile.write(f"{Password}:")
    myfile.write(f"{IP}:")
    myfile.write(f"{PortVar}:")
    myfile.close()

def login_event():
    global UsrVar
    global PassVar
    myfile = open("Data/data.txt", "r")
    filedata = myfile.read().split(":")    
    while filedata[0]=="":
            print ("Please complete the signup")
            time.sleep(5)
            os.system('python signup.py')
    My_Username = filedata[0]
    Password = filedata[1]
    myfile.close()
    Usr = UsrVar.get()
    Pass = PassVar.get()
    Box = BoxVar.get()
    if Box == 1:
        if Usr == My_Username:
            if Pass==Password:
                RootIPDef()
                os.system('python dh.py')
            else:
                #wrong password
                popupmsg()          
        else:
            #wrong username
            popupmsg()

    elif Box == 0:
        if Usr == My_Username:
            if Pass==Password:
                os.system('python dh.py')
            else:
                #wrong password
                popupmsg()          
        else:
            #wrong username
            popupmsg()

# Define the login button
button = customtkinter.CTkButton(master=root, text="Login", command=login_event)
button.place(relx = 0.75, rely = 0.75, anchor = 'center')

def signup_event():
    os.system('python signup.py')
    SystemExit()

# Define the signup button
button = customtkinter.CTkButton(master=root, text="Signup", command=signup_event)
button.place(relx = 0.75, rely = 0.85, anchor = 'center')

#####################################################


root.mainloop()
