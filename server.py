import socket
import threading

# Using local host address for host
host = "127.0.0.1"
port = 8000

# Initiating the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

