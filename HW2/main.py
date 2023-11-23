import cv2
import pickle
import server
import client

Server = server.server('localhost', 8080)
Server.createConnect()

Client = client.client('localhost', 8080)
Client.link(Server)

connectionSocket, addr = Server.acceptConnect()

vid = cv2.VideoCapture(0)

while True:

    ret, frame = vid.read()
    cv2.imshow('Server sending...',frame)

    connectionSocket.sendall(pickle.dumps(frame))
    print("Sent all data")
    print("Total size:", len(pickle.dumps(frame)))

    data = Client.clientSocket.recv(1000000)

    framercv = pickle.loads(data)
    cv2.imshow('Client receiving...',framercv)

    #take screenshot when spacebar is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite('screenshot.png',framercv)
        cv2.imshow('Screenshot',framercv)
    #close connection when ESC is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        connectionSocket.close()
        Client.clientSocket.close()
        break

vid.release()
cv2.destroyAllWindows()
