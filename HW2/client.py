import socket

class client:
    serverName = 'localhost'
    serverPort = 8080
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self, serverName, serverPort):
        self.serverName = serverName
        self.serverPort = serverPort
    def link(self, server):
        self.clientSocket.connect((server.serverName,server.serverPort))
        print("The client is ready to send")