# from socket import *

# serverName = 'localhost'  # localhost = 127.0.0.1 = 0.0.0.0
# serverPort = 12000
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName, serverPort))
# sentence = input('Input lowercase sentence:')
# clientSocket.send(str.encode(sentence))
# modifiedSentence = clientSocket.recv(1024)
# print('From Server: ', bytes.decode(modifiedSentence))
# clientSocket.close()

from socket import *

# Define the server name and port to connect to
serverName = 'localhost'  # localhost = 127.0.0.1 = 0.0.0.0
serverPort = 12000

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the specified server and port
clientSocket.connect((serverName, serverPort))

# Get user input for message to send to server
sentence = input('Input message:')

# Send the message to the server
clientSocket.send(str.encode(sentence))

# Receive response from server
response = clientSocket.recv(1024)
print('Response from server: ', bytes.decode(response))

# Print 'Bye'
print('Bye')

# Close connection with server
clientSocket.close()
