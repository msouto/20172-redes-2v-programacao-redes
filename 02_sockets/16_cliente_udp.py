import socket
serverName = 'localhost'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Entre com a sting minuscula: ")
byte_msg = message.encode('utf-8')

clientSocket.sendto(byte_msg, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
