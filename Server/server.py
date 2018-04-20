import socket
import sys, os
import threading
import User
import getopt

class Server:

    def __init__(self, host=socket.gethostbyname('localhost'), port =50000, allowReuseAddress=True, timeout = 3, max_connections=10):
        self.address = (host, port)
        self.max_connections = max_connections # max number of users that can connect to the server
        self.client_thread_list = [] # A list of all threads that are either running or have finished their task.
        self.users = [] # A list of all the users who are connected to the server.
        self.exit_signal = threading.Event()
        self.state = ''

        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as errorMessage:
            sys.stderr.write("Failed to initialize the server. Error - {0}".format(errorMessage))
            raise

        self.serverSocket.settimeout(timeout)

        if allowReuseAddress:
            self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.serverSocket.bind(self.address)
        except socket.error as errorMessage:
            sys.stderr.write('Failed to bind to address {0} on port {1}. Error - {2}'.format(self.address[0], self.address[1], errorMessage))
            raise

    def start_listening(self, defaultGreeting="\n> Welcome to our chat app!!! What is your full name?\n"):
        self.serverSocket.listen(self.max_connections)

        print("\nListening on {0} with max connections set to {1}\n".format(self.address, self.max_connections))
        try:
            while not self.exit_signal.is_set():
                try:
                    print("Waiting for a client to establish a connection\n")
                    clientSocket, clientAddress = self.serverSocket.accept()
                    print("Connection established with IP address {0} and port {1}\n".format(clientAddress[0], clientAddress[1]))
                    user = User.User(clientSocket)
                    user.ip = clientAddress[0]
                    self.users.append(user)
                    clientThread = threading.Thread(target=self.client_thread, args=(user,))
                    clientThread.start()
                    self.client_thread_list.append(clientThread)
                except socket.timeout:
                    pass
        except KeyboardInterrupt:
            self.exit_signal.set()

        for client in self.client_thread_list:
            if client.is_alive():
                client.join()


    def client_thread(self, user, size=4096):
        user.send("Please select a nickname:")
        nickname = user.receive(size)

        while not nickname or "$Line" in nickname or "$Circle" in nickname or "$SCircle" in nickname:
            user.send("Please select a nickname:")
            username = user.receive(size)
        
        user.nickname = nickname
        user.send(self.state)
        user.send("$Clear|Chat$")
        user.send("Welcome to \nPaint With Friends, {0}".format(user.nickname))


        while True:
            try:
                chatMessage = user.receive(size)
            except ConnectionResetError:
                quit(user)
                break

            if self.exit_signal.is_set():
                break

            if chatMessage == "/Quit":
                quit(user)
                break

            stripped = chatMessage.strip()
            # print(chatMessage)
            if("$Circle" in chatMessage or "$Line" in chatMessage or "$SCircle" in chatMessage):
                self.state += chatMessage
                self.server_broadcast_command(chatMessage, user)
            elif("$Clear$" in chatMessage):
                self.server_broadcast_command("$Clear|Canvas|{0}$".format(user.nickname), user)
                self.state = ''
            else:
                # print("###{0}###".format(chatMessage))
                self.server_broadcast(chatMessage, user)
        
    def server_broadcast_command(self, message, user):
        for usr in self.users:
            if usr != user:
                try:
                    usr.send(message)
                except ConnectionResetError:
                    quit(user)
                    break

    def server_broadcast(self, message, user):
        for usr in self.users:
            try:
                usr.send("{0}: {1}".format(user.nickname, message))
            except ConnectionResetError:
                quit(user)
                break


    def quit(self, user):
        # user.socket.sendall('/quit'.encode('utf8'))
        user.socket.close()
        self.users.remove(user)

    def server_shutdown(self):
        print("Shutting down chat server.\n")
        self.serverSocket.close()


def main(argv):
    pFlag = False
    cFlag = False
    mFlag = False
    port = 8300
    maxC = 10
    script_dir = os.path.dirname(__file__)
    config = "conf/chatserver.conf"

    try:
        opts, args = getopt.getopt(argv,"hp:c:m:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('chatServer.py -c <configFile> -d <dbpath> [-p <port>] [--interactive]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('server.py [-c <configFile>] [-p <port>]')
            sys.exit()
        elif opt in ("-p", "--port"):
            pFlag = True
            gPort = int(arg)
        elif opt in ("-c", "--configfile"):
            cFlag = True
            config = arg
        elif opt in ("-m", "--max"):
            mFlag = True
            gMax = int(arg)

    # Read and load contents of config
    try:
        config_path = os.path.join(script_dir, config)
        with open(config_path) as conf:
            content = conf.readlines()
            for line in content:
                item = line.strip().split()
                if item[0] == 'port':
                    port = int(item[1])
                elif item[0] == 'max_connections':
                    maxC = int(item[1])
    except FileNotFoundError:
        print("\nError: Config file not found \nUsing default values for port and max connections")
        port = 8300
        maxC = 10

    
    if pFlag:
        port = gPort
    if mFlag:
        maxC = gMax

    drawServer = Server(socket.gethostbyname('localhost'), port, True, 3, maxC)
    drawServer.start_listening()
    drawServer.server_shutdown()
if __name__ == "__main__":
    main(sys.argv[1:])


