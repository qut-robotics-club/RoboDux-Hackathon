import asyncio
import websockets
import socket

from cmdhandler import HEADERSIZE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = "client"
header = f"{len(message):<{HEADERSIZE}}".encode('UTF-8')
try:
    s.connect(("127.0.0.1", 4576))
    s.send(header + message.encode("UTF-8"))
except IOError as e:
    pass
except Exception as e:
    print(e)


async def handler(websocket, path):

    data = await websocket.recv()

    reply = f"Data recieved as:  {data}!"

    await websocket.send(reply)

start_server = websockets.serve(handler, "localhost", 8000)


asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()