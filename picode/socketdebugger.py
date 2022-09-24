import socket
import json

from cmdhandler import HEADERSIZE

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 4576))
    s.listen()
    print(f"listening to: {s}")
    sock, addr = s.accept()
    print(f"Connection accepted by: {addr}")
    cmd = {"path": [[1,2,True],
                    [1,2,True],
                    [1,2,False],
                    [1,2,True]]}
    msg = json.dumps(cmd)
    msgHeader = f"{len(msg):<{HEADERSIZE}}".encode("UTF-8")
    sock.send(msgHeader + msg.encode("UTF-8"))