import socket
import sys

HOST, PORT = "localhost" , 9999
data = "hello this is client"

#Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #connect to server and send data
    sock.connect((HOST,PORT))
    sock.sendall(data+"\n")

    #receive data from server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent :   {}".format(data)
print "Received: {}".format(received)
