# DarkHallway
# By frickengames
# Version 0.1
# 10/03/23

import customtkinter
import tkinter as tk
from tkinter import *
import time
import random
from PIL import Image, ImageTk
from splashtext import splash

# Set global application background color
background = '#333538'



#####################################################

# Setup the main tkinter window
root = customtkinter.CTk()
root.geometry('1200x700')
root.resizable(True, True)
root.configure(fg_color=background)
root.title("Welcome to DH")

# Load the application icon
ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Set themes for CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "Dark" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")

# Random Splash Text
splashno = random.randrange(1, 4)

splashs = Label(text=splash[splashno], bg='#333538', fg='#ffffff')
splashs.place(relx = 0.5, rely = 0.36, anchor='center')

# Define the username entry field
user = customtkinter.CTkEntry(master=root, placeholder_text="Username", width=200)
user.place(relx = 0.5, rely = 0.5, anchor = 'center')

# Define the password entry field
password = customtkinter.CTkEntry(master=root, placeholder_text="Type Message", width=800, height=100)
password.place(relx = 0.5, rely = 0.8, anchor = 'center')


#####################################################






root.mainloop()
