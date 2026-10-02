import socket
import threading

# Server settings
HOST = "127.0.0.1"
PORT = 5000


# Receive messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message:
                print("\n" + message)
                print("You: ", end="")

        except:
            print("\nDisconnected from server.")
            break


# Create the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((HOST, PORT))

# Ask the user for their name
name = input("Enter your name: ")

print("Connected to the chat!")
print("Type your message and press Enter.")
print("Type 'quit' to leave.\n")


# Start a thread for receiving messages
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()


# Send messages
while True:
    message = input("You: ")

    # Leave the chat
    if message.lower() == "quit":
        client.close()
        break

    # Add the user's name
    full_message = f"{name}: {message}"

    # Send the message to the server
    client.send(full_message.encode())