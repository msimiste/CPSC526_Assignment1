disimport socketserver
import subprocess
import os
import socket, threading
class MyTCPHandler(socketserver.BaseRequestHandler):
   BUFFER_SIZE = 4096
   def handle(self):
       while 1:
           data = self.request.recv(self.BUFFER_SIZE)
           if len(data) == self.BUFFER_SIZE:
               while 1:
                   try:  # error means no more data
                       data += self.request.recv(self.BUFFER_SIZE, socket.MSG_DONTWAIT)
                   except:
                       break
           if len(data) == 0:
               break
           data = data.decode( "utf-8")
           off = str(data)           
           print(data)
           if data.lower() == off:
               print("Reached line 20")
               self.request.sendall( bytearray( "I hate you", "utf-8"))
               os._exit(1)
               pring("Reached line 24")           
           self.request.sendall( bytearray( "You said: " + data, "utf-8"))
           print("%s (%s) wrote: %s" % (self.client_address[0], 
		   threading.currentThread().getName(), data.strip()))
		   # run ls on /home with -al as options
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

if __name__ == "__main__":
   HOST, PORT = "localhost", 9999
   server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
   server.serve_forever()
