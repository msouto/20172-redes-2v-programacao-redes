import socket


TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

with open('arquivo_recebido.txt', 'wb') as f:
    print("Arquivo foi aberto!")
    while True:
        data = s.recv(BUFFER_SIZE)
        print('data=%s',(data))
        if not data:
            f.close()
            print("Arquivo fechado")
            break
        f.write(data)

print("Arquivo transferido com sucesso")
s.close()
print("Conexão encerrada")
