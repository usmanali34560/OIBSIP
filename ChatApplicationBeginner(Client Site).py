import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

print("Connected to the server. You can start chatting!")

while True:
    # Send message to the server
    message = input("You: ")
    client_socket.send(message.encode('utf-8'))

    # Receive message from the server
    reply = client_socket.recv(1024).decode('utf-8')
    print(f"Friend: {reply}")

client_socket.close()
