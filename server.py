import socket
import threading

# Server settings
HOST = "127.0.0.1"
PORT = 5000

# Store connected clients
clients = []


# Send a message to all connected clients
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)


# Handle messages from one client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            # Send the message to everyone
            broadcast(message, client)

        except:
            break

    # Remove disconnected client
    if client in clients:
        clients.remove(client)

    client.close()


# Create the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the server to the address and port
server.bind((HOST, PORT))

# Start listening for connections
server.listen()

print(f"Chat server is running on {HOST}:{PORT}")


# Accept new clients
while True:
    client, address = server.accept()

    print(f"New connection from {address}")

    # Add client to the list
    clients.append(client)

    # Create a separate thread for the client
    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()