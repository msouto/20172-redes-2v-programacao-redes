import socket
HOST = socket.gethostbyname('localhost')
PORT = 2000

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_socket.connect((HOST,PORT))
message = "Hello, World!"
byte_msg = message.encode('utf-8')
tcp_client_socket.send(byte_msg)
data = tcp_client_socket.recv(1024)
tcp_client_socket.close
print("MSG recebida:", repr(data))
