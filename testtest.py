import asyncio
import websockets

async def send_message(websocket):
    while True:
        message = input("Enter your message: ")
        await asyncio.sleep(5)  
        await websocket.send(message)

async def receive_messages(websocket):
    while True:
        message = await websocket.recv()
        print("Received message from server:", message)

async def main():
    async with websockets.connect('ws://localhost:3000') as websocket:
       
        send_task = asyncio.create_task(send_message(websocket))
        receive_task = asyncio.create_task(receive_messages(websocket))
        
    
        await asyncio.gather(send_task, receive_task)

if __name__ == "__main__":
    asyncio.run(main())