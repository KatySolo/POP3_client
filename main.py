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

# ----1------
#  =?UTF-8?B?0K/QvdC00LXQutGBLtCU0LXQvdGM0LPQuA==?= <inform@money.yandex.ru>
# Sender: inform@money.yandex.ru
# To: test.katy.solo@yandex.ru
# Message-ID: <1803317348.93894.1524732159702.JavaMail.tomcat55@vostok1>
# Subject: =?UTF-8?B?0KMg0LLQsNGBINC/0L7Rj9Cy0LjQu9GB0Y8g0LrQvtGI0LU=?=
#  =?UTF-8?B?0LvRkdC6INCyINCv0L3QtNC10LrRgS7QlNC10L3RjNCz0LDRhQ==?=
# MIME-Version: 1.0
# ----2------
#  =?utf-8?b?0JrQvtC80LDQvdC00LAg0K/QvdC00LXQutGBLtCU0LjRgdC60LA=?=
#  <disk-news@yandex.ru>
# To: test.katy.solo@yandex.ru
# Date: Wed, 25 Apr 2018 18:21:31 +0300
# List-ID: welcome
# Return-Path: disk-news@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
# ----3------
#  Katy Solo (test.katy.solo@yandex.ru)
# To: test.katy.solo@yandex.ru
# Subject: =?UTF-8?B?0JzQvtC1INGC0LXRgdGC0L7QstC+0LUg0L/QuNGB0YzQvNC+?=
# Content-Type: text/plain; charset=utf-8
# Return-Path: test.katy.solo@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
# X-Yandex-Forward: 638c42cf48857d61d95cd8c944a01674
# ----4------
#  Katy Solo (test.katy.solo@yandex.ru)
# To: colo18@yandex.ru,test.katy.solo@yandex.ru
# Subject: =?UTF-8?B?0JzQvtC1INGC0LXRgdGC0L7QstC+0LUg0L/QuNGB0YzQvNC+?=
# Content-Type: text/plain; charset=utf-8
# Return-Path: test.katy.solo@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
# X-Yandex-Forward: 638c42cf48857d61d95cd8c944a01674
# ----5------
#  Katy Solo (test.katy.solo@yandex.ru)
# To: colo18@yandex.ru,test.katy.solo@yandex.ru
# Subject: =?UTF-8?B?0JzQvtC1INGC0LXRgdGC0L7QstC+0LUg0L/QuNGB0YzQvNC+?=
# Content-Type: text/plain; charset=utf-8
# Return-Path: test.katy.solo@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
# X-Yandex-Forward: 638c42cf48857d61d95cd8c944a01674
# ----6------
#  Katy Solo (test.katy.solo@yandex.ru)
# To: colo18@yandex.ru,test.katy.solo@yandex.ru
# Subject: "=?UTF-8?B?0JzQvtC1INGC0LXRgdGC0L7QstC+0LUg0L/QuNGB0YzQvNC+?="
# Content-Type: text/plain; charset=utf-8
# Return-Path: test.katy.solo@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
# X-Yandex-Forward: 638c42cf48857d61d95cd8c944a01674
# ----7------
#  Katy Solo (test.katy.solo@yandex.ru)
# To: colo18@yandex.ru,test.katy.solo@yandex.ru
# Subject: Мое тестовое письмо
# Content-Type: multipart/mixed; boundary = +++
# Return-Path: test.katy.solo@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
# X-Yandex-Forward: 638c42cf48857d61d95cd8c944a01674
# ----8------
#  Katy Solo (test.katy.solo@yandex.ru)
# To: colo18@yandex.ru,test.katy.solo@yandex.ru
# Subject: My test letter
# Content-Type: multipart/mixed; boundary = +++
# Return-Path: test.katy.solo@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
# X-Yandex-Forward: 638c42cf48857d61d95cd8c944a01674
# ----9------
#  Katy Solo (test.katy.solo@yandex.ru)
# To: colo18@yandex.ru, test.katy.solo@yandex.ru
# Subject: My test letter
# Return-Path: test.katy.solo@yandex.ru
# X-Yandex-Forward: 8b2a5c0e53d0aaaaa9907c487ff912c8
#
# .
# ----10------
#  Katy Solo <test.katy.solo@yandex.ru>
# Envelope-From: test-katy-solo@yandex.ru
# To: test.katy.solo@yandex.ru,
# 	colo18@yandex.ru
# Subject: multi to field
# MIME-Version: 1.0
# Message-Id: <857241524649811@web50j.yandex.ru>
# ----11------
#  =?utf-8?b?0JrQvtC80LDQvdC00LAg0K/QvdC00LXQutGBLtCf0L7Rh9GC0Ys=?=
# 	<hello@yandex-team.ru>
# Subject: =?utf-8?b?0JrQsNC6INGH0LjRgtCw0YLRjCDQv9C+0YfRgtGDINGBINC80L7QsdC40Ls=?=
#  =?utf-8?b?0YzQvdC+0LPQvg==?=
# Message-ID: <236710bb-3652-4b96-9d0f-f30a09da9bad@robots.yandex.ru>
#
# --===============0057981868071609573==
# ----12------
#  =?utf-8?b?0K/QvdC00LXQutGB?= <hello@yandex.ru>
# Subject: =?utf-8?b?0KHQvtCx0LXRgNC40YLQtSDQstGB0Y4g0L/QvtGH0YLRgyDQsiDRjdGC0L4=?=
#  =?utf-8?b?0YIg0Y/RidC40Lo=?=
# Message-Id: <20110815165837.A26162B2802A@yaback1.mail.yandex.net>
# .

def get_sender_and_subject(data):
    # TODO normal parce
    for i in data:
        if i.lstrip().startswith('='):
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
