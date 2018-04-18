class User:
    def __init__(self, client_socket, nickname = '', password = '', isAdmin = False):
        self.socket = client_socket
        self.password = password
        self.nickname = nickname
        self.isAdmin = isAdmin


    def makeAdmin(self):
        self.isAdmin = True

    def send(self, message):
        try:
            self.socket.sendall((message+'\n').encode('utf8'))
        except (ConnectionResetError, BrokenPipeError):
            pass

    def receive(self, size):
        response = self.socket.recv(size)
        return response.decode('utf8')
