import select
import socket
import json

from cmdhandler import HEADERSIZE

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 4576))

server_socket.listen()

sockets_list = [server_socket]

clients = {}

print("Listening for connections....")

def receive_message(client_socket: socket.socket):
    try:

        # Receive our "header" containing message length, it's size is defined and constant
        msgheader = client_socket.recv(HEADERSIZE)

        # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(msgheader):
            return False

        # Convert header to int value
        msglength = int(msgheader.decode('utf-8').strip())

        # Return an object of message header and message data
        return {'header': msgheader, 'data': client_socket.recv(msglength)}

    except:
        return False

while True:
    readSockets, garbage, errSock = select.select(sockets_list, [], sockets_list)
    for notifiedSocket in readSockets:

        if notifiedSocket == server_socket:
            sock, addr = server_socket.accept()

            clientType = receive_message(sock)

            if clientType is False:
                continue
            
            sockets_list.append(sock)
            clients[sock] = clientType

            print(f"Accepted new connection from {addr} of type {clientType['data']}")
        else:
            msg = receive_message(notifiedSocket)
            if not msg:
                print("Connection closed")

                sockets_list.remove(notifiedSocket)
                del clients[notifiedSocket]
                continue
            else:
                msgdata = json.loads(msg['data'].decode("UTF-8"))
                clientType = clients[notifiedSocket]

                if clientType['data'].decode("UTF-8") == "client":
                    if "path" in msgdata:
                        print(f"path received {msgdata['path']}")
