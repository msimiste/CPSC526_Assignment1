#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import subprocess

BUFFER_SIZE = 8
s = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 9998           # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   
   while 1:
       try:
           print("line17")
           data = c.recv(BUFFER_SIZE, 0)
           while (len(data) == BUFFER_SIZE):
                data += c.recv(BUFFER_SIZE, 0)
           #data = data.decode("utf-8")
           ##print("Testing: " + data.decode("utf-8"))
       except:
           break
       #c.send(bytearray(data, "utf-8"))
       data1 = data.split()
       res = subprocess.check_output(data1)
       #res = subprocess.check_output(["/bin/ls", "-al", "/home"])
       # convert result from bytes to string
       res = res.decode( 'utf-8')
       # split the string at newlines
       res = res.split( "\n")
       # report results
       print("Output:")
       for line in res:
           print( "  ", line)
c.close()                # Close the connection
