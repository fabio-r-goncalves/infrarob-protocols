import socket

ServerIP = "127.0.0.1"
ServerPort = 8888
Message = b"hellow world"


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSocket.sendto(Message, (ServerIP, ServerPort))