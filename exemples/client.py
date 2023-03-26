import socket
import struct

HOST = "192.168.0.194"
PORT = 8080

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Send data
while True:
    gen_prompt = int(input("Enter length of generate a prompt, 0 to exit: "))
    if gen_prompt == 0:
        break
    message = struct.pack("<i", gen_prompt)
    message += input("Enter a message: ").encode()
    sock.send(message)
    answer = sock.recv(1024)
    print("Received: ", answer.decode())

sock.close()

