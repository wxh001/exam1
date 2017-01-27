import sys
from socket import *
serverHost = '192.168.1.213'
serverPort = 50007
message = ''
if len(sys.argv) > 1:
   serverHost = sys.argv[1]
   if len(sys.argv) > 2:
      message = (x.encode() for x in sys.argv[2:])
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))
for line in message:   # print('line is :',line,end=' ')
   sockobj.send(line)
   data = sockobj.recv(1024)
   print('Client recieved:',data)
sockobj.close()
