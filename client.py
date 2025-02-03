import socket

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = '10.1.95.93'  # server's IP address
        server_port = 21312
        client_socket.connect((server_ip, server_port))
        print(f"Connected to the server at {server_ip}:{server_port}")
        while True:
            client_message = input("CLIENT: ")
            client_socket.send(client_message.encode())
            if client_message.lower() == "bye":
                print("Closing connection...")
                break
            server_response = client_socket.recv(1024).decode()
            print(f"SERVER SENT: {server_response}")
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
