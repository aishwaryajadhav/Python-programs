# server implementing sliding window protocol
from array import *
import socket              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              

host = socket.gethostname() 
port = 12341
s.bind((host, port))  
      
s.listen(5)              
c, addr = s.accept() 
s.settimeout(0)
print("Received connection: " , addr)
i=1
while(True):
	g=0
	try:
		data=c.recv(100)
	except socket.error:
		g=1
	if g==0:
		if data=="exit":
			c.send("exit")
			break
		print("\n")	
		print(data)
		f = "\nPacket received"
		i=i+1
		c.send(f)
print("\nAll packets received")

