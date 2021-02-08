# similar to UDP Client
# import socket module
from socket import *

# set the port and
serverPort = 12000

# set the UDP socket type
serverSocket = socket(AF_INET, SOCK_DGRAM)

# binds (that is, assigns) the port number 12000 to the server’s socket.
serverSocket.bind(('', serverPort))

print("The server is ready to receive passed in sentence")

# the while loop will allow UDPServer to receive and process packets from clients indefinitely
while True:
    message, clientAddress = serverSocket.recvfrom(2048) # when packet arrives then store them
    modifiedMessage = message.decode().upper() # converting the received sentence
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) # send the modified sentence back to client