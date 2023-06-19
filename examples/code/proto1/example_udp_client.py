import socket
import json
import sys


from messages.proto1_message import Proto1Message
from messages.proto1_config_message import Config
from messages.proto1_object_messages import Proto1Objects

FILE_ROOT =  "examples/messages/proto1/"
CONFIG_FILE = "config_message.json"
DATA_FILE = "data_message.json"
REQUEST_FILE = "request_message.json"

def getMessageHeader():
    return Proto1Message(112,1,"ok")


def getConfigMessage(dataSinkIP, dataSinkPort, method, period):
    message = getMessageHeader()
    config = Config(dataSinkIP, dataSinkPort, method, period)
    message.setConfig(config.configToJson())
    return message.messageToJson()

def getRequestMessage(request):
    message = getMessageHeader()
    message.setRequest(request)
    return message.messageToJson()

def getObjectMessage():
    message = getMessageHeader()
    objects = [
        Proto1Objects(123,20,1,4,1,230,1,999999999,111111111,2,100,1,1,0).ObjectsToJson(),
        Proto1Objects(124,10,2,5,2,240,1,999999888,222111111,3,120,1,1,0).ObjectsToJson()
    ]
    message.setObjects(objects)
    return message.messageToJson()

def messageFromJson(option):
    messageJson = None
    match option:
        case "CONFIG":
            messageJson = getConfigMessage("localhost", 8123, "periodically", 1)
        case "DATA":
            messageJson = getObjectMessage()
        case "REQUEST":
            messageJson = getRequestMessage("ping")
        case _:
            print("Invalid Input... Exiting")
            return 

    print(messageJson)
    return json.dumps(messageJson)


args_n = len(sys.argv)
print(args_n)

if(args_n < 4):
    print("usage: python3 example_udp_client.py IP PORT OPTION")

serverIp = sys.argv[1]
serverPort = int(sys.argv[2])

message = messageFromJson(sys.argv[3])
if(message != None):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.sendto(message.encode(), (serverIp, serverPort))


