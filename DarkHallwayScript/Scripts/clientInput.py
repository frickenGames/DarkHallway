
import os
import sys
import socket
import select
import errno
import getpass
import calendar
import time
IP = ""
password = ""
My_Username = ""
Port = 0
os.system("clear")
ts = calendar.timegm(time.gmtime())
ts = time.gmtime()

def Login():
    print("Hello", My_Username, "please input password:")
    passwordInput = getpass.getpass()
    if passwordInput ==  password:
        print ("Welcome")
        socketStuff()
    else:
        print ("Incorrect, try again")
        Login()

def Dump(Usr, Psswd, IP, Port):
    Port=str(Port)
    myfile = open("../Data/data.txt", 'w')
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
    myfile = open("../Data/data.txt", "r")
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
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, Port))
    client_socket.setblocking(False)

    username = My_Username.encode("utf-8")
    username_header = f"{len(username):<{HeaderLength}}".encode('utf-8')
    client_socket.send(username_header + username)
    try:
        while True:
            msg = input(f"{My_Username}>")

            if msg:
                msg = msg.encode('utf-8')
                msg_header = f"{len(msg):<{HeaderLength}}".encode("utf-8")
                client_socket.send(msg_header + msg)
                os.system("clear")
    except KeyboardInterrupt:
        print("goodbye")
        exit()

Grab()

