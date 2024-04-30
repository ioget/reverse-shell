import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
            
        try:
            while True:
                request = input("cli >>> ")
                await websocket.send(request)
                response = await websocket.recv()
                print(f"{response}")
        except websockets.ConnectionClosed:
            print('Connection closed. ' )    





asyncio.run(hello())