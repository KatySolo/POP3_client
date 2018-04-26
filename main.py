import socket
import ssl
import re

class AuthenticationError(Exception):
    pass

def auth_user(socket,credentials):
    for i in credentials:
        socket.send((i + '\r\n').encode())
        data = socket.recv(1024)
        if data.decode()[:2] == '-E':
            raise AuthenticationError
        # print(data.decode())
    print ("Connection established")

def establlish_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('pop.yandex.ru', 995))
    ssl_sock = ssl.wrap_socket(sock)
    data = ssl_sock.recv(1024)
    # print(data.decode())
    return ssl_sock


def get_sender_and_subject(data):
    for i in data:
        print (i)
    return ('a','s')


def list_messages(socket, data_count):
    # from_pattern = re.compile(r"\a+From: \a+<\a+>")
    # subject_pattern = re.compile(r"\w+Subject: \w+")

    #From: =?UTF-8?B?0JrQvtC80LDQvdC00LAg0J/QvtGH0YLRiyBNYWlsLlJ1?=<welcome@corp.mail.ru>
    #Subject: =?UTF-8?B?0JrQsNC6INCy0L7RgdC/0L7Qu9GM0LfQvtCy0LDRgtGM0YHRjyDQv9C+?==?UTF-8?B?0YfRgtC+0Lkg0YEg0LzQvtCx0LjQu9GM0L3QvtCz0L4/?=
    # \r\n.\r\n
    for i in range(1,data_count+1):
        print ('----'+str(i)+'------')
        socket.send(("TOP " + str(i) + " 0" + '\r\n').encode())
        data = ""
        raw_data = ''
        while not raw_data.startswith('.') and not raw_data.startswith('\r\n'):
            raw_data = socket.recv(1024).decode()
            if raw_data[:2] == '-E':
                print (raw_data)
                break
            data += raw_data
        from_field = data.split('\nFrom:')[1].split("\n")[:7]
        sender, subject = get_sender_and_subject(from_field)
        # from, subject
        # print (sender, subject)

def show_inbox(socket):
    socket.send(("LIST" + '\r\n').encode())
    data=""
    raw_data = ''
    while raw_data[-3:] != '.\r\n':
        raw_data = socket.recv(1024).decode()
        data += raw_data
    data_count = len(data.split('\r\n'))-3
    print ("You have "+ str(data_count) + " messages in your mailbox")
    list_messages(socket, data_count)

    # print (data)

if __name__ == '__main__':
    email = 'test.katy.solo@yandex.ru'
    password = 'qwertyKate98'
    try:
        socket = establlish_connection()
        auth_user(socket,['USER '+email,'PASS '+password])
        show_inbox(socket)
    except AuthenticationError:
        print('Wrong login/password')
    finally:
        socket.close()
