import socket
import threading

# Using local host address for host
address = ("127.0.0.1", 8000)

# Initiating the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen()

print("Server started! Waiting for connections...")

clients = []
client_nicknames = []


def stream_messages(message):
    for client in clients:
        client.send(message)
        
        
def handle_client(client):
    while True:
        try:
            # Sending messages
            message = client.recv(1024)
            clean_message = message.decode("ascii")
            clean_message = clean_message.split(":")[2].strip()
            
            if clean_message == "/exit" and client in clients:
                # If "/exit" is typed, the client will be removed from the channel
                leave_channel(client)
                
            else:
                stream_messages(message)
        except:
            # Removing and closing clients
            if client in clients:
                leave_channel(client)
            break
        
def leave_channel(client):
    """Closing client's connection."""""
    client_index = clients.index(client)
    clients.pop(client_index)
    client.close()
    nickname = client_nicknames[client_index]
    client_nicknames.pop(client_index)
    stream_messages(f"(global):User {nickname} disconnected from the server!".encode("ascii"))
        
def recieve():
    while True:
        # Accepting connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        # Requesting the nickname
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        
        # Storing client info and welcoming the user
        clients.append(client)
        client_nicknames.append(nickname)
        print(f"Nickname of the client is {nickname}")
        stream_messages(f"(global):User {nickname} connected to the server!".encode("ascii"))
        
        # Starting personal thread for client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        
recieve()