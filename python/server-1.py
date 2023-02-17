# from socket import *

# serverPort = 12000
# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind(('localhost',serverPort))
# serverSocket.listen(1)
# print ('The server is ready to receive')
# while 1:
#      connectionSocket, addr = serverSocket.accept()
#      sentence = connectionSocket.recv(1024)
#      capitalizedSentence = sentence.upper()
#      connectionSocket.send(capitalizedSentence)
#      connectionSocket.close()

from socket import *

# Define the port to listen on
serverPort = 12000

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to localhost and the specified port
serverSocket.bind(('localhost', serverPort))

# Listen for incoming connections, with a maximum queue of 1
serverSocket.listen(1)
print('The server is ready to receive')

# Loop to continuously accept connections
while True:
    # Accept incoming connections
    connectionSocket, addr = serverSocket.accept()

    # Receive message from client
    sentence = connectionSocket.recv(1024)
    print('Message received from client: ', bytes.decode(sentence))

    # Prepare response to send back to client
    response = 'Bye'

    # Send response to client
    connectionSocket.send(str.encode(response))
    print('Sent response: ', response)

    # Close connection with client
    connectionSocket.close()
