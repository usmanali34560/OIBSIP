import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(2)  # Allow 2 connections

print("Server is running and waiting for connections...")

# Accept two client connections
client1, addr1 = server_socket.accept()
print(f"Connected to {addr1}")
client2, addr2 = server_socket.accept()
print(f"Connected to {addr2}")

while True:
    # Receive message from client1 and send it to client2
    message = client1.recv(1024).decode('utf-8')
    print(f"Client1: {message}")
    client2.send(message.encode('utf-8'))

    # Receive message from client2 and send it to client1
    message = client2.recv(1024).decode('utf-8')
    print(f"Client2: {message}")
    client1.send(message.encode('utf-8'))

client1.close()
client2.close()
server_socket.close()