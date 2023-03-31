# create a client that sends messages to the server, it should be able to send multiple messages
# if the message is "exit" the client should exit

import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            name = input("Enter your name: ")
            if name == "exit":
                break
            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
