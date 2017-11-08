#Implemente um cliente multithread em Python, que concete na porta 2000 e envie pelo 5 mensagens em threads diferentes no cliente. As mensagens enviadas devem ser enumeradas, ex: Mensagem da thread 1, Mensagem da thread 2 e etc.)
import socket
import threading

HOST = socket.gethostbyname('localhost')
PORT = 2000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

while True:
    threading.Thread().start()
    message = input("Digite mensagem: ")
    byte_message = message.encode('utf-8')
    client_socket.send(byte_message)

    data = client_socket.recv(1024)
    print(data)

tcp_client_socket.close
