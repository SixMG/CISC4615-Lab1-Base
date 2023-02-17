# import socket

# client = socket.socket()

# client.connect(('localhost',6969))  #connection

# while True:
#     msg = input(">>:").strip()
#     if len(msg) == 0 :continue
#     client.send(msg.encode())   # send data

#     data = client.recv(1024)    # receive data

#     print("Return:",data.decode())


# client.close()


from socket import *

# Define the server name and port to connect to
serverName = 'localhost'  # localhost = 127.0.0.1 = 0.0.0.0
serverPort = 12000

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the specified server and port
clientSocket.connect((serverName, serverPort))

# Create a list to store messages
messages = []

# Get user input for first message to send to server
sentence = input('Input first message:')

# Send the message to the server
clientSocket.send(str.encode(sentence))

# Receive response from server
response = bytes.decode(clientSocket.recv(1024))
print('Response from server: ', response)
messages.append(('Client', sentence))
messages.append(('Server', response))

# Get user input for second message to send to server
sentence = input('Input second message:')

# Send the message to the server
clientSocket.send(str.encode(sentence))

# Receive response from server
response = bytes.decode(clientSocket.recv(1024))
print('Response from server: ', response)
messages.append(('Client', sentence))
messages.append(('Server', response))

# Close connection with server
clientSocket.close()

# Print all messages
print('All messages:')
for message in messages:
    print(message[0] + ': ', message[1])
