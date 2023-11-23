import socket

class server:
    serverName = 'localhost'
    serverPort = 8080
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self, serverName, serverPort):
        self.serverName = serverName
        self.serverPort = serverPort
    def createConnect(self):
        self.serverSocket.bind(('',self.serverPort))
        self.serverSocket.listen()
        print("The server is ready to receive")
    def acceptConnect(self):
        connectionSocket, addr = self.serverSocket.accept()
        print("Connected to", addr)
        return connectionSocket, addr

