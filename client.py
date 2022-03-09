import socket
from threading import Thread

# Main client functionality

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
clientHost = input("Enter an unused hostname: ")
clientPort = int(input("Enter an unused port number: "))

# The IP address and port number for the server
serverHost = input("Enter the hostname for the Index Server: ")
serverPort = 7734

# Message sent to join the system
request = "JOIN P2P\nHost: " + clientHost + '\n' + "Port: " + str(clientPort)
sendRequest(request, serverHost, serverPort)

# Handle input from the client
while (True):
    print("What do you want to do? Enter number corresponding to an option you choose:")
    print("1. Quit")
    # Functionality of centralized server
    option = int(input())
    if (option == 1):
        quitConnection(serverHost, serverPort)
        break
    else:
        print('please enter a valid choice')
