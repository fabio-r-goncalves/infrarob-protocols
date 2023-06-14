import socket

serverIP = "0.0.0.0"
serverPort = 8888
bufferSize = 1024



serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

serverSocket.bind((serverIP, serverPort))

print("Starting UDP server IP: %s PORT: %d" % (serverIP, serverPort))

while True:
    data, addr = serverSocket.recvfrom(bufferSize)
    print("Message: %s From: %s" % (data, addr))

