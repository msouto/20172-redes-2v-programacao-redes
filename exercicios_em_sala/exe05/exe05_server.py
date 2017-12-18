from jsonsocket import Client, Server

host = 'localhost'
port = '8001'


# Server code:
server = Server(host, int(port))
server.accept()
data = server.recv()
print(data)
# data now is: {'some_list': [123, 456]}
server.send({'data': data}).close()
