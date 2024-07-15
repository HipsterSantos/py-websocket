import asyncio
import random
import datetime
import websockets

CONNECTIONS  = set()
async def register(websocket):
    CONNECTIONS.add(websocket)
    try: 
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)


async def hello(websocket):
    name = await websocket.recv()
    print(f'<<< {name}')
    #prepping message to send back to the sender 
    greeting= f"hellow {name}"
    await websocket.send(greeting)
    print(f'>>>{greeting}')

async def  main():
    async with websockets.serve(hello,'localhost',8765) as server:
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())