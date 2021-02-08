# The socket module forms the basis of all network communications in Python.
# By including this line, we will be able to create sockets within our program.
from socket import *

# Set the hostname and port number
serverName = '127.0.0.1'
serverPort = 12000

# This line creates the client’s socket, called clientSocket.
# The first parameter indicates the address family; in particular, AF_INET indicates that the underlying network is using IPv4.
# The second parameter indicates that the socket is of type SOCK_DGRAM, which means it is a UDP socket
# Note that we are not specifying the port number of the client socket when we create it; we are instead letting the operating system do this for us.
# Now that the client process’s door has been created, we will want to create a message to send through the door.
clientSocket = socket(AF_INET, SOCK_DGRAM)

# raw_input() is a built-in function in Python.
# When this command is executed, the user at the client is prompted with the sentence below
# Now that we have a socket and a message, we will want to send the message through the socket to the destination host.
message = input('Please enter a sentence in lowercase below:')

# we first convert the message from string type to byte type, as we need to send bytes into a socket
# The method sendto() attaches the destination address (serverName, serverPort) to the message
# And sends the resulting packet into the process’s socket, clientSocket.
clientSocket.sendto(message.encode(), (serverName, serverPort))

# when a packet arrives from the Internet at the client’s socket, the packet’s data is put into the variable modifiedMessage
# the packet’s source address is put into the variable serverAddress
# The method recvfrom also takes the buffer size 2048 as input. (work for most common case)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# This line prints out modifiedMessage on the user’s display, after converting the message from bytes to string.
print(modifiedMessage.decode())

# close the socket
clientSocket.close()
