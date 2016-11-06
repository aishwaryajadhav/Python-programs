#Server for remote procedure call 

from SimpleXMLRPCServer import SimpleXMLRPCServer

import os


#Enter apt ip and port no. for server

server = SimpleXMLRPCServer(('172.18.39.132', 9000), logRequests=True)

def add(a,b):

	a=int(a)
	b=int(b)
	f=a+b
	return f

server.register_function(add)


try:
    
	print 'Use Control-C to exit'
    
	server.serve_forever()

except KeyboardInterrupt:
   
	print 'Exiting'


