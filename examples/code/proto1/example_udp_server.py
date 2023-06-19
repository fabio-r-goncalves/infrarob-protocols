import socket
import json
import threading
import time


serverIP = "0.0.0.0"
serverPort = 8888
bufferSize = 1024

FILE_ROOT = "examples/messages/proto1/"
DATA_FILE = "data_message.json"

sendSocket = None
clientIP = None
clientPort = None
message = None
period = 1


def handleRecvdMessage(message):
    global clientIP, clientPort, period
    data = json.loads(message)
    if('config' in data and data['config'] is not ""):
        newIp = data["config"]["datasinkIP"]
        newPort = int(data["config"]["datasinkPort"])
        newPeriod = int(data["config"]["sendingMethod"]["period"])
        print("Datasink: %s:%d Period:%d" %(newIp, newPort, newPeriod))
        clientIP = newIp
        clientPort = newPort
        period = newPeriod


def recfFunction():
    global clientIP, clientPort, period
    recvSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    recvSocket.bind((serverIP, serverPort))

    print("Starting UDP server IP: %s PORT: %d" % (serverIP, serverPort))

    while True:
        data, addr = recvSocket.recvfrom(bufferSize)
        print("Message: %s From: %s" % (data, addr))
        print(clientIP)
        handleRecvdMessage(data)

def sendFunction():
    global clientIP, clientPort, period
    
    while True:
        if( sendFunction is not None and clientIP is not None and clientPort is not None):
            print("sending data to client: %s:%d" % (clientIP, clientPort))
            sendSocket.sendto(message.encode(), (clientIP, clientPort))
        time.sleep(period)
    

sendSocket  = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

file_path = FILE_ROOT + DATA_FILE
file = open(file_path)
message = json.dumps(json.load(file))


sendThread = threading.Thread(target=recfFunction)
recvThread = threading.Thread(target=sendFunction)

recvThread.start()
sendThread.start()