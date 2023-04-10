# Dissy-Assignment-3
Repository for Distributed Systems course assignment 3.

Demonstration video: [Assignment 3 - Distributed Systems](https://youtu.be/sSgK4cWTxXI)

The project was developed on Python 3.8.10. The server is running on the localhost address and port which is "127.0.0.1:8000"
<br>
<br>
To run the code type following commands in different consoles.
<br>
Starting the server:<br>
```python3 server.py```

Starting the client:<br>
```python3 client.py```


You need to start several clients to fully experience the functionality.

The main functionality is to send messages on different channels. Users might use following console commands (commands are type straight to the chat):

/exit - Leave the chat <br>
/switch-<channel_name/user_name> - Switch to another channel / private chat <br>
/current-channel - Show the current channel <br>
/private-<target-user-nickname>-<message> - Send a private message to a user <br>
/help - Show list of commands