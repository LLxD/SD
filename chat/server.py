# create a websocket server that receives messages from the client
# if the message is "exit" the server should exit
# else the server should be able to receive multiple messages

import asyncio
import websockets


async def hello(websocket, path):
    while True:
        name = await websocket.recv()
        print(f"< {name}")

        greeting = f"Hello {name}!"

        await websocket.send(greeting)
        print(f"> {greeting}")

        if name == "exit":
            break


start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
