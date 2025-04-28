# Server-Client Model using Caesar Cipher
This repository contains the implementation of the **Caesar cipher** in a **client-server model**, enabling secure **dual communication** between the server and client.

## Overview

This repo demonstrates:
- Secure message exchange between a client and server using the **Caesar cipher** encryption technique.
- Encrypting outgoing messages and decrypting incoming messages on both sides.
- A simple yet effective way to integrate classical encryption methods into network communication.

The **Caesar cipher** is one of the earliest and simplest encryption techniques, based on shifting characters by a fixed number of positions.

## Features

- Encrypt messages using the Caesar cipher.
- Decrypt received messages using the Caesar cipher.
- Enable two-way (dual) encrypted communication between server and client.
- Simple TCP socket communication for real-time message transfer.

## Technologies Used

- Python 3
- Socket programming (TCP sockets)
- Basic string manipulation (for cipher logic)

## How to Run

1. Clone the repository

2. Navigate to the project directory

3. Run the server:
   ```bash
   python caesar_server.py
   ```

4. In a new terminal, run the client:
   ```bash
   python caesar_client.py
   ```

5. Start sending encrypted and decrypted messages securely!

## Notes

- The Caesar cipher provides basic security and is primarily for educational purposes.
- Modern encryption techniques like AES or RSA are recommended for real-world secure communication.
- This repo demonstrates how simple encryption can be integrated into socket-based communication.
