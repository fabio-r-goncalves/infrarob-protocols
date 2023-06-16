import socket
import json
import sys

FILE_ROOT =  "examples/messages/proto1/"
CONFIG_FILE = "config_message.json"
DATA_FILE = "data_message.json"
REQUEST_FILE = "request_message.json"

def messageFromJson(option):
    file_path = FILE_ROOT
    match option:
        case "CONFIG":
            file_path = file_path + CONFIG_FILE
        case "DATA":
            file_path = file_path + DATA_FILE
        case "REQUEST":
            file_path = file_path + REQUEST_FILE
        case _:
            print("Invalid Input... Exiting")
            return 

    print(file_path)
    file = open(file_path)
    print(file)
    return json.dumps(json.load(file))


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


