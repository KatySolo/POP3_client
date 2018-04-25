import base64

input_lines = ['USER test.katy.solo@yandex.ru',
               'PASS qwertyKate98'
               # base64.b64encode('test.katy.solo@yandex.ru'.encode()).decode(),
               # base64.b64encode('qwertyKate98'.encode()).decode(),
               # 'MAIL FROM: test.katy.solo@yandex.ru',
               # 'RCPT TO: colo18@yandex.ru',
               # 'RCPT TO: test.katy.solo@yandex.ru',
               # 'DATA',
               #  form_message(theme,addresses,message,attachments),
               # 'QUIT'
               ]
import socket
import ssl

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('pop.yandex.ru', 995))
ssl_sock = ssl.wrap_socket(sock)
data = ssl_sock.recv(1024)
print(data.decode())
for i in input_lines:
    ssl_sock.send((i + '\r\n').encode())
    data = ssl_sock.recv(1024)
    print(data.decode())
#
# ssl_sock.send(('RETR 10' + '\r\n').encode())
# data = ssl_sock.recv(2048)
# print(data.decode())
# ssl_sock.close()
