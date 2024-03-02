import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://18.223.252.46:3000') as websocket:
        while True:
            message = input("Enter your message: ")
            await websocket.send(message)

            message = await websocket.recv()
            print("Received message from server:", message)



async def main():
    # Run send_message() and receive_messages() concurrently
    await asyncio.gather(send_message())

# Create and run the event loop
if __name__ == "__main__":
    asyncio.run(main())


    