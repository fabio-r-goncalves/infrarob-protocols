import socket
import json
import threading
import time

from messages.proto1_message import Proto1Message
from messages.proto1_config_message import Config
from messages.proto1_object_messages import Proto1Objects



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


def getMessageHeader():
    return Proto1Message(112,1,"ok")

def getObjectMessage():
    message = getMessageHeader()
    objects = [
        Proto1Objects(123,20,1,4,1,230,1,999999999,111111111,2,100,1,1,0).ObjectsToJson(),
        Proto1Objects(124,10,2,5,2,240,1,999999888,222111111,3,120,1,1,0).ObjectsToJson()
    ]
    message.setObjects(objects)
    return message.messageToJson()

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