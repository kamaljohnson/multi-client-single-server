import socket
import threading

# Create a socket
def socket_create():
    try:
        global host
        global port
        global s
        host = '192.168.1.100'          #this is the server ip address
        port = 1000
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Connect to a remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print("Socket connection error: " + str(msg))


# Receive commands from remote server and run on local machine

def threader():
    while True:
        data = s.recv(1024)
        print(data.decode())

def socket_communicate():
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
    while True:
        data = input()
        s.send(str.encode(data))
def main():
    socket_create()
    socket_connect()
    socket_communicate()
main()