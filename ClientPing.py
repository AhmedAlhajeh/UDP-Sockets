import socket
import time
import numpy
import datetime
from datetime import datetime


counter = 1
rrtArray = []
rttsum = 0

# sending 10 pings to the server by creating a while loop
while counter < 11:
    TimeNow = datetime.now()
    msg = ' ping from client ' + str(counter) + ', sent at ' + str(TimeNow) + " , " #message format
    TimeNow = (time.time() * 1000)
    counter = counter + 1 #incrementing
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creating UDP socket
    try:
        client_socket.settimeout(2.0) #The client waits 2 seconds for a reply

        tstart= (time.time() * 1000) #changing the starting time to milliseconds
        client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',34567))
        data, addr = client_socket.recvfrom(4096)

        tend = (time.time() * 1000) #changing the ending time to milliseconds
        rtt = (tend - tstart) #finding the round trip time
        rrtArray.append(rtt) #creating an array with rtt in it so we can find maximum and minimum rtt
        rttsum += rtt #finding the sum of rtt so we can find the average
        time.sleep(1)
        print(str(data.decode()) + str(rtt) + "ms") #printing the data (ping) with rtt for each ping
    except:
        print ('request timed out')




print("minimum RRT " + str(min(rrtArray)) +"ms") #finding the minimum rrt
print("maximum RRT " + str(max(rrtArray)) + "ms") #finding maximum rrt
print("average RRT " + str((rttsum/len(rrtArray))) + "ms") #finding the average
print("Standard deviation RRT " + str(numpy.std(rrtArray)) + "ms") #finding standard deviation
print("packet loss rate " + str((1-(len(rrtArray) / 10)) * 100) + "%") #fidning loss rate


client_socket.close()