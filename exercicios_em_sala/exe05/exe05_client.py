from jsonsocket import Client, Server

host = '127.0.0.1'
port = '8001'

# Client code:
client = Client()
client.connect(host, int(port)).send({'some_list': [123, 456]})
response = client.recv()
print(response)
# response now is {'data': {'some_list': [123, 456]}}
client.close()
