#Implemente um cliente multithread em Python, que concete na porta 2000 e envie pelo 5 mensagens em threads diferentes no cliente. As mensagens enviadas devem ser enumeradas, ex: Mensagem da thread 1, Mensagem da thread 2 e etc.)

import socket, threading

class ThreadedClient(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.host, self.port))

	def threading(self):
		threading.Thread(target = self.send, args = msg)

	def send(self, msg):
		self.msg = msg
		self.data = msg.encode('utf-8')		
		self.sock.send(self.data)
		self.sock.close()

for i in range(5):
    mensagem = 'Mensagem thread ' + str(i + 1)
ThreadedClient('127.0.0.1', 2000).send(mensagem)
