import socket

# Server setup
HOST = ""  # Symbolic name meaning all available interfaces
PORT = 8000  # Choose an arbitrary non-privileged port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Explain: AF_INET = IPv4, SOCK_STREAM = TCP

server_socket.bind((HOST, PORT))
print(f"Server socket bound to port {PORT}")

server_socket.listen(1)  # Allow a backlog of 1 connection
print("Server is listening for incoming connections...")

# Connection handling loop
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Received connection from {client_address}")

    # Data handling
    data = client_socket.recv(1024)  # Receive up to 1024 bytes
    print("Received data:", data.decode())  # Decode from bytes to string

    # Echo back the data
    client_socket.sendall(data)

    # Close the client connection (for this simple echo server)
    client_socket.close()
    print("Connection closed.")
