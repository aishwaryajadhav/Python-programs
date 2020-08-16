#This program is a part of an IOT project which takes in data 
#from a remote sensor 

import http.client
import time

val1 = 0
val2 = 0
while True:
	conn = http.client.HTTPConnection("192.168.43.210")
	conn.request("HEAD", "Get_Data")
	res = conn.getresponse()
	temp = str(res.msg)
	
	val1 = int(temp[18:20])
	print (str(val1))
	if val1<5:
		print("Overflow")
	else:
		print("Fine")
	
