# Create a tcp socket that listens on port 1111 on local host,

# When a user connects to the socket, the following should happen:

# If the user sends a string containing only the word "exit", the socket and connection
# should close and the function should end.
# For any other string the user sends, the server should send a copy of the string
# back to the user.
# you can assume short strings all ending in "\n" other than "exit"


from socket import socket, create_connection, create_server


def socket_server():
    with create_server(("127.0.0.1", 1111), reuse_port=True) as server:
        sv, _ = server.accept()
        while True:
            msg: str = sv.recv(1024).decode()
            # bs = t.recv(0xDEAD) Read maximum bytes from the socket

            if msg == "exit" or msg == "":
                # if bs == b'exit': Read directly in binary
                sv.close()
                return

            sv.send("".join(msg).encode())
            
# using the socket module directly     

# import socket

# def socket_server():    
#     # Create a TCP socket
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#     # Bind the socket to the specified host and port
#     server.bind(('127.0.0.1', 1111))
    
#     # Listen for incoming connections
#     server.listen(1)
    
#     while True:
#         connection, client_address = server.accept()
        
#         while True:
#             # Receive data from the client
#             data = connection.recv(1024).decode()

#             # Respond
#             if data == 'exit':
#                 connection.close()
#             connection.send(data.encode())
