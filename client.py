import socket
from threading import Thread


# Main client functionality

def peerServer(clientPort):
    peerServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peerServer.bind((socket.gethostbyname(socket.gethostname()), clientPort))
    peerServer.listen(2)
    while (True):
        (clientSocket, clientAddress) = peerServer.accept()
        print('Got connection from', clientAddress)
        newThread = Thread(target=peerConnection, args=(clientSocket,))
        newThread.start()
        newThread.join()
        print("What do you want to do? Enter number corresponding to an option you choose")
        print("1. Send image")
    upload_socket.close()


# peer connection
def peerConnection(clientSocket):
    data = clientSocket.recv(1034).decode()
    print(data)
    print('new request from peer')
    clientSocket.close()


# send to peer
def sendToPeer(message):
    peerHost = input("Enter the hostname of the peer:")
    peerPort = int(input("Enter port number of the peer:"))

    peerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peerSocket.connect((peerHost, peerPort))
    peerSocket.send(message.encode())
    peerSocket.close()


# Send requests to the central server
def sendRequest(request, serverHost, serverPort):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    print('Response from the central server:')
    print(response)
    clientSocket.close()


# handle quitting
def quitConnection(serverHost, serverPort):
    note = "EXIT P2P\nHost: " + serverHost + '\n' + "Port: " + str(serverPort)
    sendRequest(note, serverHost, serverPort)


# The IP address and port number for the client
clientHost = input("Enter an unused hostname:")
clientPort = int(input("Enter an unused port:"))

# The IP address and port number for the server
serverHost = input("Enter the hostname for the Index Server:")
serverPort = 7734

# Message sent to join the system
request = "JOIN P2P\nHost: " + clientHost + '\n' + "Port: " + str(clientPort)
sendRequest(request, serverHost, serverPort)

uploadThread = Thread(target=peerServer, args=(clientPort,))
# destroy this upload thread on quitting
uploadThread.daemon = True
uploadThread.start()

# Handle input from the client
while (True):
    print("What do you want to do? Enter number corresponding to an option you choose:")
    print("1. Send image")
    # Functionality of centralized server
    option = int(input())
    if (option == 1):
        message = input()
        sendToPeer(message)
    else:
        print('please enter a valid choice')
