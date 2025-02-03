from socket import *

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    server_ip = '10.1.95.68'  #server's IP address
    server_port = 21312
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Server started on {server_ip}:{server_port}. Waiting for connections...")
    
    try:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        while True:
            encrypted_message = conn.recv(1024).decode()
            if not encrypted_message or encrypted_message.lower() == 'bye':
                print("Client disconnected.")
                break
            print(f"CLIENT SENT (encrypted): {encrypted_message}")

            decrypted_message = caesar_cipher_decrypt(encrypted_message, 4)
            print(f"CLIENT SENT (decrypted): {decrypted_message}")

            server_message = input("SERVER (plaintext): ")
            encrypted_response = caesar_cipher_encrypt(server_message, 4)
            
            print(f"SERVER SENDING (plaintext): {server_message}")
            print(f"SERVER SENDING (encrypted): {encrypted_response}")

            conn.send(encrypted_response.encode())

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
