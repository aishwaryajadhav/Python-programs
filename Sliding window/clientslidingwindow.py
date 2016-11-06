# client implementing sliding window protocol
from array import *
import socket   
import os            
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
host = socket.gethostname()
port = 12341
s.connect((host, port))
s.settimeout(0)
win= raw_input('Enter window size')
winstart=1
winend=int(win)
sendstart=1
data=[]
print('Enter the message(Press ctrl-C to terminate message): ')
while True:
    try:
        d = raw_input()
    except KeyboardInterrupt:
	data.append('exit')
        break
    data.append(d)
j=0
k=0
while(j < len(data)):
	while( j < winend ):
		if(j == len(data)):
			k=1
			break
		#f= str(j)+"."+data[j]
		s.send(data[j])
		g=0
		try:
			a = s.recv(1024)
		except socket.error:
			g=1
		if g==0:
			print("\n")
			print(a)	
			winend=winend+1
			winstart=winstart+1
		j=j+1
	if k==1:
		o=winstart	
		while (o<=winend):	
			g=0
			try:
				a = s.recv(1024)
			except socket.error:
				g=1
			if g==0:
				print("\n")
				print(a)
				o=o+1
		break
	else:
		g=0
		try:
			a = s.recv(1024)
		except socket.error:
			g=1
		if g==0:
			print("\n")
			print(a)	
			winend=winend+1
			winstart=winstart+1
print('Sent all data')
	
