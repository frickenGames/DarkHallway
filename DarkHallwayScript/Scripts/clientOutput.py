import sys
import os
import socket
import select
import random
import errno
import calendar;
import time;
os.system("clear")
ts = calendar.timegm(time.gmtime())
ts = time.gmtime()
HeaderLength = 10
IP = ""
Port = 0
My_Username = ""

def Grab():
    print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
      
    myfile = open("../Data/data.txt", "r")
    filedata = myfile.read().split(":")    
    global IP
    global Port
    global My_Username
    while filedata[0]=="":
            print ("Please complete the setup below")
            time.sleep(5)
            os.system("clear")
            Grab()
    My_Username = filedata[0]
    IP = filedata[2]
    Port = int(filedata[3])
    myfile.close()
    My_Username = My_Username + "_Output"
    SocketStuff()



def SocketStuff():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, Port))
    client_socket.setblocking(False)
    
    username = My_Username.encode("utf-8")
    username_header = f"{len(username):<{HeaderLength}}".encode('utf-8')
    client_socket.send(username_header + username)
    try:
        while True:
            try:
                while True:
                    username_header = client_socket.recv(HeaderLength)
                    if not len(username_header):
                        print("connection closed by the server")
                        exit()
                    username_length = int(username_header.decode("utf-8"))
                    username = client_socket.recv(username_length).decode('utf-8')

                    msg_header = client_socket.recv(HeaderLength)
                    msg_length = int(msg_header.decode('utf-8'))
                    msg = client_socket.recv(msg_length).decode('utf-8')
                    ts = calendar.timegm(time.gmtime())
                    ts = time.gmtime()
                    print ("______________________________________")
                    print ((time.strftime("%Y-%m-%d %H:%M:%S", ts)),f"{username}:: {msg}")
                    print ("--------------------------------------")

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("reading error", str(e))
                    exit()
                continue

            except Exception as e:
                print("general error: ", str(e))
                exit()
    except KeyboardInterrupt:
        print("goodbye")
        exit()
Grab()
