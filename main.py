import socket
import ssl

def auth_user(socket,credentials):
    for i in credentials:
        socket.send((i + '\r\n').encode())
        data = socket.recv(1024)
        print(data.decode())


def establlish_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('pop.mail.ru', 995))
    ssl_sock = ssl.wrap_socket(sock)
    data = ssl_sock.recv(1024)
    print(data.decode())
    return ssl_sock


if __name__ == '__main__':
    try:
        socket = establlish_connection()
        auth_user(socket,['USER test.katy.solo@mail.ru','PASS qwertyKate98'])
    except:
        pass
    finally:
        socket.close()
