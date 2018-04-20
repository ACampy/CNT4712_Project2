import socket 
import sys

class Client:
    def __init__(self):
        self.isClientConnected = False
        self.toSend = ""

    def connect(self, host='', port=50000):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((host, port))
            self.isClientConnected = True
            return True
        except socket.error as errorMessage:
            if errorMessage.errno == socket.error.errno:
                return False
            else:
                return False

    def disconnect(self):
        if self.isClientConnected:
            self.clientSocket.close()
            self.isClientConnected = False

    def send(self, data):
        if not self.isClientConnected:
            return

        self.clientSocket.sendall(data.encode('utf8'))

    def receive(self, size=4096):
        if not self.isClientConnected:
            return ""

        return self.clientSocket.recv(size).decode('utf8')