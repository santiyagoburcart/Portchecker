import socket
from clrprint import *

# Get Ip  or Domin  and Port 
ip=(input("please Enter your IP for server or Domin:"))
port=int(input("please Enter your PORT for server or Domin:"))
# Create Function for checking open ports
def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, (port)))
      s.shutdown(2)
      return 'Open'
   except:
      return 'Closed'

# Use function to show results from user
if isOpen(ip,port)=='Open':
    print("checking for open port ..." )
    clrprint('Port',f'{port}', 'is' ,str(isOpen(ip,port)), 'on', f'{ip}', clr=['d','b','d','g','d','b'])
else:
    print("checking for open port ..." )
    clrprint('Port',f'{port}', 'is' ,str(isOpen(ip,port)), 'on', f'{ip}', clr=['d','b','d','r','d','b'])