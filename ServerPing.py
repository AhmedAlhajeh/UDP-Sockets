import random
import socket

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #create UDP socket
sock.bind(('127.0.0.1', 34567)) #put local ip to receive ping message between client and server with port 34567

# infinity loop
while True:
    rand = random.randint(0, 10) #generating a random integer from 0-10
    data,addr=sock.recvfrom(4096) #specifiying the size of the packet
#if the random integer is bigger or equal than 3
    if rand >= 3:
       data = data.upper() # capitalizes the encapsulated data
       print(str(data.decode())) #print data

       
       sock.sendto(data,addr) #send the data to the client via ip address 127.0.0.1
    else:
     continue



