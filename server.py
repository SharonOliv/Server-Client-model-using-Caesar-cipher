from socket import *

def main():
    server_ip = '10.1.95.93'  #server's IP address
    server_port = 21312
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print(f"Server started on {server_ip}:{server_port}. Waiting for connections...")
    try:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        while True:
            message = conn.recv(1024).decode()
            if not message or message.lower() == 'bye':
                print("Client disconnected.")
                break

            print(f"CLIENT SENT: {message}")
            server_message = input("SERVER: ")
            conn.send(server_message.encode())
            if server_message.lower() == "bye":
                print("Closing connection...")
                break

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        conn.close()
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    main()
