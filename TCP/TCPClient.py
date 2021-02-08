# import socket module
from socket import *

# set the server name and port
serverName = '127.0.0.1'
serverPort = 12000

# create socket client
# SOCK_STREAM indicates TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initiates the TCP connection between the client and server
# Before we can send and receive data
clientSocket.connect((serverName, serverPort))

# three-way handshake performed

# Ask user to enter sentence
sentence = input('Input lowercase sentence:')

# sends the sentence through the client’s socket and into the TCP connection.
# Note it just drops bytes into sentence rather than a specified destination address
clientSocket.send(sentence.encode())

# When characters arrive from the server, they get placed into the string modifiedSentence.
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())

# close socket
clientSocket.close()