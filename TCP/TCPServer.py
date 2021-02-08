# import socket module
from socket import *

# set the server port
serverPort = 12000

# the 'Welcome Door'
# set the TCP socket type
serverSocket = socket(AF_INET, SOCK_STREAM)
# associate the server with port
serverSocket.bind(('', serverPort))

# This line has the server listen for TCP connection requests from the client.
# The parameter specifies the maximum number of queued connections (at least 1).
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    # When a client knocks on this door
    # the program invokes the accept() method for serverSocket
    # which creates a new socket in the server, called connectionSocket, dedicated to this particular client.
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

# close
connectionSocket.close()