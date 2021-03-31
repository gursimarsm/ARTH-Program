import socket
import os
import time
from pyfiglet import Figlet

os.system("clear")
pyf = Figlet(font='puffy')
a = pyf.renderText("UDP Chat App without Multi-Threading")
os.system("tput setaf 3")
print(a)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      
ip=input("Enter your IP: ")
port=int(input("Enter your port number: "))
sendip=input("Enter sender IP: ")
sendport=int(input("Enter sender port number: "))
s.bind((ip,port))
while True:
  i=input("Enter your message:")
  s.sendto(i.encode(), (sendip,sendport))
  x=s.recvfrom(20)
  clientip=x[1][0]

  data=x[0].decode()

  print(clientip + " : " + data)