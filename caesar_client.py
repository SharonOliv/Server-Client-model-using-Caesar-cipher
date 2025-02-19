import socket

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
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = '10.1.95.68'  # server's IP address
        server_port = 21312
        client_socket.connect((server_ip, server_port))
        print(f"Connected to the server at {server_ip}:{server_port}")

        while True:
            client_message = input("CLIENT (plaintext): ")
            encrypted_message = caesar_cipher_encrypt(client_message, 4)

            print(f"CLIENT SENDING (plaintext): {client_message}")
            print(f"CLIENT SENDING (encrypted): {encrypted_message}")
            client_socket.send(encrypted_message.encode())

            if client_message.lower() == "bye":
                print("Closing connection...")
                break

            encrypted_response = client_socket.recv(1024).decode()
            print(f"SERVER SENT (encrypted): {encrypted_response}")

            decrypted_response = caesar_cipher_decrypt(encrypted_response, 4)
            print(f"SERVER SENT (decrypted): {decrypted_response}")
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
