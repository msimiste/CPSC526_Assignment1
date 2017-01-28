#!/usr/bin/python           # This is server.py file

#Name: Mike Simister
#StudentID: 10095107
#Tutorial Section: T02

import socket               
import subprocess
import shlex
import os
import sys

def helpList(l):
    build = ""
    for line in l:
        build += line
    return build
    
BUFFER_SIZE = 4096
PASS_MSG = "Password:"
PW = '\103\120\123\103\65\62\66' 
hList = ["\tCommands\n","cat <file> \t display a file\n", "cd \t\t change current working directory\n", "help \t\t shows a list of commands\n", "ls [agrs] \t list current directory contents\n","off \t\t shuts down the program\n", "who \t\t lists the users who are currently logged in\n",  "ps \t\t shows the current running processes\n", "pwd \t\t returns the current working directory\n", "who \t\t lists the users currently logged in\n", "***NOTE*** \tThis program will execute all linux commands\n"]
CONNECT = False

    
while True:
   
   if(not(CONNECT)):
       s = socket.socket()         # Create a socket object
       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       host = sys.argv[1]       # Get local machine name
       port = int(sys.argv[2])         # Reserve a port for your service.
       s.bind((host, port))        # Bind to the port
       
       s.listen(5)                 # Now wait for client connection.         
       c, addr = s.accept()     # Establish connection with client.
       print ('Got connection from', addr)
       c.send(bytearray(PASS_MSG,"ascii"))
       data = c.recv(BUFFER_SIZE, 0)
       pInfo = data.decode("ascii")
       
            
       while(pInfo.strip() != PW):
           c.send(bytearray(PASS_MSG,"ascii"))
           data = c.recv(BUFFER_SIZE, 0)
           pInfo = data.decode("ascii")           
       CONNECT = True
       c.send(bytearray('Welcome Back\n', "ascii"))    
   while CONNECT:
       try:
           #print("line17") for debug purposes
           data = c.recv(BUFFER_SIZE, 0)
           while (len(data) == BUFFER_SIZE):
                data += c.recv(BUFFER_SIZE, 0)
           data = data.decode("ascii")           
       except:
           break
       data1 = shlex.split(data)
       if(len(data1) == 0):
            CONNECT = False
       elif(data1[0].strip() == "off"):
            c.send(bytearray('GoodBye\n',"ascii"))
            sys.exit()            
       elif(data1[0] == "cd"):
            data1 = ''.join(str(x) for x in data1[1:])
            data1 = data1.replace(" ","")
            data1 = data1.replace("\n","")            
            try:
                os.chdir(data1)
            except Exception, e:
                c.send(bytearray(str(e)+'\n',"ascii"))      
       elif(data1[0] == "help"):          
           #c.send(bytearray(str(helpList(hList))+'\n',"ascii"))
           c.send(bytearray(''.join(str(x) for x in hList)))
       
       else:
           #print("line 58: ") for dubug purposes
           #print(data1) for debug purposes
           try:
                res = subprocess.check_output(data1,stderr=subprocess.STDOUT)
                c.send(res)
           except Exception, e:
               c.send(bytearray(str(e)+'\n', "ascii"))                             
   CONNECT = False
c.close()                # Close the connection


