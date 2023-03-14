# DarkHallway
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
Mess=False

# Set global application background color
background = '#333538'

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
splashs.place(relx = 0.5, rely = 0.3, anchor='center')

# This is where messages should be printed into
user = customtkinter.CTkTextbox(master=root, width=800, height=200, corner_radius=10, text_color="white")
user.place(relx = 0.5, rely = 0.5, anchor = 'center')
user.configure(border_width=1, border_color="grey")

# This is where new messages should be typed and sent from
EntryVar = customtkinter.StringVar()
entry = customtkinter.CTkEntry(master=root, textvariable=EntryVar, placeholder_text="Type Message", width=800, height=100, corner_radius=10, )
entry.place(relx = 0.5, rely = 0.8, anchor = 'center')


#####################################################
#Output Modules
#####################################################
ts = calendar.timegm(time.gmtime())
ts = time.gmtime()
HeaderLength = 10
IP = ""
Port = 0
My_Username1 = ""

def Grab1():
    myfile = open("Data/data.txt", "r")
    filedata = myfile.read().split(":")    
    global IP
    global Port
    global My_Username1
    while filedata[0]=="":
            print ("Please complete the signup")
            time.sleep(5)
            os.system('python signup.py')
    My_Username = filedata[0]
    IP = filedata[2]
    Port = int(filedata[3])
    myfile.close()
    My_Username1=My_Username1+"OutputBox"
    SocketStuff1()



def SocketStuff1():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, Port))
    client_socket.setblocking(False)
    
    username = My_Username1.encode("utf-8")
    username_header = f"{len(username):<{HeaderLength}}".encode('utf-8')
    client_socket.send(username_header + username)
    try:
        while True:
            try:
                while True:
                    username_header = client_socket.recv(HeaderLength)
                    if not len(username_header):
                        exit()
                    username_length = int(username_header.decode("utf-8"))
                    username = client_socket.recv(username_length).decode('utf-8')

                    msg_header = client_socket.recv(HeaderLength)
                    msg_length = int(msg_header.decode('utf-8'))
                    msg = client_socket.recv(msg_length).decode('utf-8')
                    ts = calendar.timegm(time.gmtime())
                    ts = time.gmtime()
                    
                    MESSAGE=((time.strftime("%Y-%m-%d %H:%M:%S", ts)),f"{username}:: {msg}")
                    user.insert(END, MESSAGE)
                    user.insert(END, '\n')
                    user.insert(END, "#####################################################\n")
                    


            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("reading error", str(e))
                    exit()
                continue

            except Exception as e:
                print("general error: ", str(e))
                exit()
    except KeyboardInterrupt:
        exit()
#Grab1()

#####################################################
#Input Modules
#####################################################
IP = ""
password = ""
My_Username = ""
Port = 0
ts = calendar.timegm(time.gmtime())
ts = time.gmtime()

def Login():
#    print("Hello", My_Username, "please input password:")
#    passwordInput = getpass.getpass()
#    if passwordInput ==  password:
#    print ("Welcome")
    socketStuff()
#    else:
#        print ("Incorrect, try again")
#        Login()

def Dump(Usr, Psswd, IP, Port):
    Port=str(Port)
    myfile = open("Data/data.txt", 'w')
    myfile.write(f"{Usr}:")
    myfile.write(f"{Psswd}:")
    myfile.write(f"{IP}:")
    myfile.write(f"{Port}:")
    myfile.close()
    Grab()

def passwd():
    print("Please input a password?")
    passwod = getpass.getpass(">")
    print("please input again")
    passwd1 = getpass.getpass(">")
    if passwod == passwd1:
        print("passwords accepted")
        return(passwod)
    else:
        print("passwords did not match")
        passwd()
    
def firstInput():
    print("whats your username?")
    Uname = str(input(">"))
    pwd = passwd()
    print("please input IP")
    IP = str(input(">"))
    while True:
        print("please input Port number")
        try:
            Port = int(input(">"))
            break
        except:
            print("must be a number")
            continue
    Dump(Uname, pwd, IP, Port)
    
def Grab():      
    myfile = open("Data/data.txt", "r")
    filedata = myfile.read().split(":")    
    global My_Username
    global password
    global IP
    global Port
    try:
        My_Username = filedata[0]
        password = filedata[1]
        IP = filedata[2]
        Port = int(filedata[3])
        myfile.close()
    except:
        myfile.close()
        firstInput()
    
    Login()
HeaderLength = 10

def socketStuff():
    global EntryVar
    global Mess
    global client_socket
    global username
    global username_header
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, Port))
    client_socket.setblocking(False)

    username = My_Username.encode("utf-8")
    username_header = f"{len(username):<{HeaderLength}}".encode('utf-8')
    client_socket.send(username_header + username)

def socketStuff1(*args):
    global EntryVar
    global Mess
    global client_socket
    global username
    global username_header
    try:
            msg = EntryVar.get()
            if msg:
                msg = msg.encode('utf-8')
                msg_header = f"{len(msg):<{HeaderLength}}".encode("utf-8")
                client_socket.send(msg_header + msg)
                user.see(tk.END)
                entry.delete(0, END)

    except KeyboardInterrupt:
        exit()

#Grab()

#####################################################
def Death(*args):
    root.destroy()


root.bind('<Return>', socketStuff1)
root.bind('<Escape>', Death)

if __name__ == "__main__":
    
    Thread1 = threading.Thread(target=Grab)
    Thread2 = threading.Thread(target=Grab1)
    
    
    Thread1.start()
    Thread2.start()
    


root.mainloop()