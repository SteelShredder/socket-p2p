import selectors
import socket
#Sample code adapted from Python docs

HOST = 'localhost'
PORT = 2222
sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        # if the client is closed, close the connection
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

# creates socket object
sock = socket.socket()

# binds with the host and the port number
sock.bind((HOST, 2222))

sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
