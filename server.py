import socket
import threading

All_connections = []
All_address = []

print_lock = threading.Lock()

# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 1000
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Bind socket to port (the host and port the communication will take place) and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


# Establish connection with client (socket must be listening for them)
def socket_accept():
    while True:
        conn, address = s.accept()
        print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
        All_connections.append(conn)
        All_address.append(address)
        t = threading.Thread(target = threader,args=(conn,))
        t.daemon = True
        t.start()

def threader(conn):
    socket_communicate(conn)
# Send commands
def socket_communicate(conn):
    print(All_address)
    while True:
        data = conn.recv(1024)
        with print_lock:
            print(data.decode('utf-8'))
        for c in All_connections:
            c.send(data)

def main():
    socket_create()
    socket_bind()
    socket_accept()


main()