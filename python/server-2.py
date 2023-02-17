# import socket

# server = socket.socket()  # initialize a socket object

# server.bind(('localhost', 6969))  # bind the ip

# server.listen(5)  # listen, queue length 5


# print("Waiting for clients----")

# while True:
#     conn, addr = server.accept()  # accept connection
#     print(conn, addr)
#     print("The data is coming")
#     while True:
#         data = conn.recv(1024)  # connect
#         print("Received data from client：", data)
#         if not data:
#             print("client has lost")
#             break
#         conn.send(data.upper())     # return data

#         if (data == 'bye'):
#             break

# server.close()  # close socket


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

    # Receive first message from client
    sentence = connectionSocket.recv(1024)
    print('Message received from client: ', bytes.decode(sentence))

    # Prepare response to send back to client
    response = 'Hello CIS Student'

    # Send response to client
    connectionSocket.send(str.encode(response))
    print('Sent response: ', response)

    # Receive second message from client
    sentence = connectionSocket.recv(1024)
    print('Message received from client: ', bytes.decode(sentence))

    # Prepare response to send back to client
    response = 'Bye'

    # Send response to client
    connectionSocket.send(str.encode(response))
    print('Sent response: ', response)

    # Close connection with client
    connectionSocket.close()
