#Implemente um cliente multithread em Python, que concete na porta 2000 e envie pelo 5 mensagens em threads diferentes no cliente. As mensagens enviadas devem ser enumeradas, ex: Mensagem da thread 1, Mensagem da thread 2 e etc.)
import socket
import threading

HOST = socket.gethostbyname('localhost')
PORT = 2000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
COUNT = 0
VAL = True
while VAL == True:
    threading.Thread().start()
    COUNT = COUNT+1
    if COUNT > 5:
         VAL = False
    message = "Mensagem da thread "+str(COUNT)+"."
    byte_message = str(message).encode('utf-8')
    client_socket.send(byte_message)

    data = client_socket.recv(1024)
    print(data)

client_socket.close
