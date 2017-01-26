#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import subprocess
import shlex
import os
import sys

BUFFER_SIZE = 4096
PASS_MSG = "Password:"
PW = "CPSC526"
CONNECT = False
s = socket.socket()         # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "localhost" # Get local machine name
port = 9999           # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.


c, addr = s.accept()     # Establish connection with client.
c.send(bytearray(PASS_MSG,"utf-8"))
data = c.recv(BUFFER_SIZE, 0)
pInfo = "".join(map(chr,data))     
while(pInfo.upper().strip() != PW.upper()):
    c.send(bytearray(PASS_MSG,"utf-8"))
    data = c.recv(BUFFER_SIZE, 0)
    pInfo = "".join(map(chr,data))
    print(pInfo.upper() == PW.upper())
    
while True:
   #c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)   
   while 1:
       try:
           #print("line17") for debug purposes
           data = c.recv(BUFFER_SIZE, 0)
           while (len(data) == BUFFER_SIZE):
                data += c.recv(BUFFER_SIZE, 0)
           data = data.decode("utf-8")           
       except:
           break
       data1 = shlex.split(data)
       if(data1[0].strip() == "off"):
            c.send(bytearray('GoodBye',"ascii"))
            #sys.exit()
            c.close()
       elif(data1[0] == "cd"):
            data1 = ''.join(str(x) for x in data1[1:])
            data1 = data1.replace(" ","")
            data1 = data1.replace("\n","")
            os.chdir(data1)       
       elif(data1[0] == "help"):
           res = subprocess.check_output(data1,stderr=subprocess.STDOUT, shell=True)
           #print("".join(map(chr,res)))
           c.send(res)
       else:
           #print("line 58: ") for dubug purposes
           #print(data1) for debug purposes
           try:
                res = subprocess.check_output(data1,stderr=subprocess.STDOUT)
                c.send(res)
           except:
               #err = (bytearray("Command: " + "".join(map(chr,res)) + "Not Supported"),"utf-8")
               c.send(bytearray("\nCommand: \"" + data.strip() + "\" not supported\n","utf-8"))              
c.close()                # Close the connection
