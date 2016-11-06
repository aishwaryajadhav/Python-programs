#Remote procedure call client

import xmlrpclib


a=int(input('Enter 1st number'))

b=int(input('Enter 2nd number'))

proxy=xmlrpclib.ServerProxy('http://172.18.39.132:9000')
    #Enter server ip and port number
print proxy.add(a,b)
