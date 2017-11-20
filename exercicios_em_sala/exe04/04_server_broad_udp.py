import socket
serverHost = '10.25.255.255'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
serverSocket.bind((serverHost, serverPort))

print("Servidor pronto para receber: ")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Conexão de: ', clientAddress)
    #Processa a stringe para lestras maiusculas
    modifiedMessage = message.upper()
    print("\n", modifiedMessage)
serverSocket.sendto(modifiedMessage, clientAddress)
