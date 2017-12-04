import socket
from urllib.parse import quote_plus

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent: Programacao_para_redes (Criado em aula)\r\n\
Connection: close\r\n\
\r\n\
"""

sock = socket.socket()
sock.connect(('maps.google.com',80))
request = request_text.format(quote_plus('Av. Senador Salgado Filho, 1559, Natal, RN'))
sock.sendall(request.encode('ascii'))
raw_reply = b''
while True:
    more = sock.recv(4096)
    if not more:
        break
    raw_reply += more
    print(raw_reply.decode('utf-8'))
