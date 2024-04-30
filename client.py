#!/usr/bin/env python

import asyncio
import signal
import websockets
import os

async def echo(websocket):
    async for request in websocket:
        
     
        try:
            # Execute la commande shell et récupère la sortie
            result = os.popen(request).read()
        except Exception as e:
            # En cas d'erreur, envoie le message d'erreur au client
            await websocket.send(str(e))
        else:
            # Si aucune erreur, envoie la sortie normale au client
            await websocket.send(result)

async def server():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(echo, "localhost", 8765):
        await stop

asyncio.run(server())