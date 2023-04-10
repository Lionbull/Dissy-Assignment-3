import socket
import threading

nickname = input("Enter your nickname: ")
current_channel = "channel_1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

print("### Type /help for a list of commands ###")

def show_current_channel():
    """Printing the current channel."""
    print(f"### Your current channel is {current_channel} ###")
    
show_current_channel()


def receive():
    """Receiving messages from the server and printing them to the console."""
    while True:
        try:
            # Receiving messages
            message = client.recv(1024).decode('ascii')
            
            if message == 'NICK':
                # Nickname requested
                client.send(nickname.encode('ascii'))
                
            elif message.split(":")[0] == f"({current_channel})":
                # Printing the message if matches the current channel
                print(message)
                
            elif message.split(":")[0] == f"(private)":
                # Printing private messages
                print(message)
                
            elif message.split(":")[0] == f"(global)":
                # Printing global messages (server messages)
                print(message)

        except:
            # Closing connection
            client.close()
            break
        
    return 0


def write():
    # Telling Python to use global variable, and not to create a new one with the same name
    global current_channel

    while True:
        raw_message = input("")
        
        if raw_message == "/help":
            # Printing a list of commands
            print("### List of commands ###")
            print("/exit - Leave the chat")
            print("/switch-<channel_name> - Switch to another channel")
            print("/current-channel - Show the current channel")
            print("/private-<target-user-nickname>-<message> - Send a private message to a user")
            
        elif raw_message[0:7] == "/switch":
            # Switching to another channel
            channel_name = raw_message.split("-")[1]
            print(f"### Switched to {channel_name}! ###")
            
            # Changing the current channel
            current_channel = channel_name
            
        elif raw_message[0:8] == "/private":
            # Switching to private chat
            raw_message = raw_message.split("-")
            message = f"(private):{nickname}:{raw_message[1]}:{raw_message[2]}"
            client.send(message.encode('ascii'))
            
        elif raw_message == "/current-channel":
            # Showing the current channel
            show_current_channel()
            
        elif raw_message == "/exit":
            # Leaving the server
            print("### You left the server! ###")
            message = f'({current_channel}):{nickname}: {raw_message}'
            client.send(message.encode('ascii'))
            client.close()
            break
        
        else:
            # Sending messages
            message = f'({current_channel}):{nickname}: {raw_message}'
            client.send(message.encode('ascii'))
            
    return 0
            
        
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
