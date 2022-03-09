import socket
from threading import Thread


# Client joining the network
def clientJoin(dataList, clientSocket, peerID):

    # Get IP and port from client
    host = dataList[1].split(':')[1]
    port = dataList[2].split(':')[1]

    # List for client information
    clientInfo = [host, port, "Absent"]
    P2P.activePeers[peerID] = clientInfo
    print("Index server: ")
    print(P2P.activePeers)
    clientSocket.send('You have successfully joined the P2P network'.encode())


# Handle new requests from clients
def newConnection(clientSocket,peerID):
    message = clientSocket.recv(1024).decode()
    print("New request from client")
    messageList = message.split('\n')
    # print(messageList)
    for line in messageList:
        print(line)
    if messageList[0].split(' ')[0] == 'JOIN':
        clientJoin(messageList, clientSocket,peerID)


class P2P:
    # Dictionary to retain active peers
    activePeers = {}


peerID = 0
# Functionality of centralized server

# Create a new socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port for the central server
serverHost = input("Enter the IP address of the central server: ")
serverPort = 7734

# Bind to the port
serverSocket.bind((serverHost, serverPort))

# Wait for connection
serverSocket.listen(5)
print("Index Server is running...")
while (True):
    # Establish connection with client
    clientSocket, clientAddress = serverSocket.accept()
    peerID += 1
    print('Got connection from', clientAddress)
    newThread = Thread(target=newConnection, args=(clientSocket,peerID))
    newThread.start()
print('shutting down central server')
serverSocket.close()
