import socket
import sys

HOST, PORT = "localhost", 9999
data = " hello udp server"

#udp sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(data+"\n",(HOST,PORT))
received = sock.recv(1024)

print "Send : {}".format(data)
print "Received:{}".format(received)
