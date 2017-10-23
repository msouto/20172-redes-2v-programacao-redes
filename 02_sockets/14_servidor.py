import socket
HOST = socket.gethostbyname('localhost')
PORT = 2000

tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()
client, addr = tcp_server_socket.accept()
print('Conexão de:', addr)
while True:
    data = client.recv(1024)
    message = "Recebida"
    byte_msg = message.encode('utf-8')
    client.send(byte_msg)
    if not data: break
    print("\n Mensagem Recebida", data)
client.close()
tcp_server_socket.close()
