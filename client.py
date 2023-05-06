import socket

HOST = 'localhost'
PORT = 2222 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        x = input("Your data ")
        if (x == ""):
            break
        s.sendall(str.encode(x))
        data = s.recv(1024)
        print(f"Received {data!r}")
        
