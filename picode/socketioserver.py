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

CLIENTS = set()

# async def handler(websocket, path):
#     while True:
#         data = await websocket.recv()
#         header = f"{len(data):<{HEADERSIZE}}".encode('UTF-8')
#         s.send(header + data.encode("UTF-8"))
#         await websocket.send(data)

async def send(websocket, message):
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        pass

def broadcast(message):
    for websocket in CLIENTS:
        asyncio.create_task(send(websocket, message))

async def handler(websocket):
    CLIENTS.add(websocket)
    try:
        async for _ in websocket:
            data = await websocket.recv()
            header = f"{len(data):<{HEADERSIZE}}".encode('UTF-8')
            s.send(header + data.encode("UTF-8"))
            # await websocket.send(data)
            broadcast(data)
    finally:
        CLIENTS.remove(websocket)

start_server = websockets.serve(handler, "www.veleriumproject.com", 8000)


asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()