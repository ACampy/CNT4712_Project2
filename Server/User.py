class User:
    def __init__(self, client_socket, nickname = '', password = '', isAdmin = False):
        self.socket = client_socket
        self.password = password
        self.nickname = nickname
        self.isAdmin = isAdmin


    def makeAdmin(self):
        self.isAdmin = True

    def send(self, message):
        self.socket.sendall((message+'\n').encode('utf8'))

    def receive(self, size):
        return self.socket.recv(size).decode('utf8')
