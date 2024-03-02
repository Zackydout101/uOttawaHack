import asyncio
import websockets

# Store connected clients
clients = set()

# Broadcast message to all clients
async def broadcast(message):
    print("Broadcasting message:", message)
    tasks = [asyncio.create_task(client.send(message)) for client in clients]
    await asyncio.wait(tasks)

# Event handler for new client connections
async def connection_handler(websocket, path):
    # Add new client to the set
    clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast received message to all clients
            await broadcast(message)
    finally:
        # Remove disconnected client from the set
        clients.remove(websocket)

# Start WebSocket server
start_server = websockets.serve(connection_handler, "localhost", 3000)

print("WebSocket server is running...")

# Run the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()