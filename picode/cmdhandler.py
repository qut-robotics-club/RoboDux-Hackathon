import socket
import os
import string
import json

HEADERSIZE = 10

class cmdlink():
    def __init__(self) -> None:
        self.insocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.insocket.setblocking(False)
        self.ip = ("127.0.0.1", 4576)
        self.isConnected = True

    def connect(self) -> bool:
        try:
            self.insocket.connect(self.ip)
            self.isConnected = True
        except IOError as e:
            pass
        except Exception as e:
            print(e)

    def setIP(self, ip, port = 4576):
        if not self.isConnected:
            self.ip = (ip, port)
        else:
            print(f"Socket connection already established, IP remains at: {self.ip}")

    def msgSend(self, message: string):
        header = f"{len(message):<{HEADERSIZE}}".encode('UTF-8')
        if self.isConnected:
            self.insocket.send(header + message.encode('UTF-8'))
        else:
            print("Socket not connected yet. :(")
    
    def msgRecv(self) -> string:
        header = self.insocket.recv(HEADERSIZE)
        msgLen = int(header.decode("UTF-8").strip())
        msg = self.insocket.recv(msgLen).decode("UTF-8")
        return msg        

    def Ready(self, isReady: bool=True):
        state = json.dumps(["ready", isReady])
        self.msgSend(state)

    def pubPos(self, x, y, theta=0):
        pose = json.dumps(["pose", [x, y, theta]])
        self.msgSend(pose)

    def handleMsg(self):
        msg = self.msgRecv()
        output = json.loads(msg)
        return output
