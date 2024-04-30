# reverse-shell
small reverse sell 


Project Structure:

    client.py: Manages the client-side interaction, sending commands to the server and receiving responses.
    server.py: Handles incoming requests from the client, executes user-level commands, and sends responses back.

Start the Server:


    python serve.py

Run the Client:



    python client.py


Client Interaction:

    You'll see a cli >>> prompt in the client window.
    Enter user-level commands (e.g., ls, pwd, etc.) that the client's account has permission to execute.
    Press Enter to send the command to the server.
    The server's response will be displayed in the client window.


Disclaimer:

This project is for educational purposes only. The provided code is not suitable for production use due to the security vulnerabilities associated with direct sudo execution. Always prioritize security measures when implementing remote access solutions.
