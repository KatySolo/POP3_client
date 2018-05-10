import base64
import datetime
import socket
import ssl

import re


class AuthenticationError(Exception):
    pass


def auth_user(socket, credentials):
    for i in credentials:
        socket.send((i + '\r\n').encode())
        data = socket.recv(1024)
        if data.decode()[:2] == '-E':
            raise AuthenticationError
            # print(data.decode())
    print("Connection established")


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

def encode_subject(data):
    subject_data = ''
    if data[0].lstrip()[9:].rstrip('"').startswith('='):
        for i in range(len(data)):
            if i == 0:
                subject_data += base64.b64decode(data[i].lstrip()[9:].rstrip('\r')[10:-2]).decode('utf-8')
            else:
                if data[i].lstrip().startswith('='):
                    subject_data += base64.b64decode(data[i].lstrip().rstrip('\r')[10:-2]).decode('utf-8')
                else:
                    break
        return subject_data
    else:
        return data[0].lstrip()[9:].rstrip('\r')


def get_sender_and_subject(data):
    sender, address = encode_sender(data[:2])
    subject = '<no subject>'
    for i in range(2, len(data)):
        if data[i].startswith('Subject:'):
            subject = encode_subject(data[i:])
            break
    return (sender, address, subject)


def encode_sender(data):
    sender_data = ''
    if data[0].lstrip().startswith('='):
        for i in range(2):
            if i == 0:
                sender_data += data[i].lstrip().rstrip('\r')
            elif i == 1:
                if data[i].lstrip().startswith('<'):
                    sender_data += ' ' + data[i].lstrip()
                else:
                    continue
        splitted_data = sender_data.split(' ')
        a = splitted_data[0][10:-2]
        email = splitted_data[1].rstrip('\r').replace('(', '<').replace(')', '>')
        return (base64.b64decode(a).decode('utf-8'), email)
    else:
        a = data[0].lstrip().rstrip('\r').replace('(', '<').replace(')', '>')
        if a.index('<') == -1:
            return (a.split('(')[0].rstrip(), '<' + a.split('(')[1].replace(')', '>'))
        return (a.split('<')[0].rstrip(), '<' + a.split('<')[1].replace(')', '>'))


def list_messages(socket, data_count):
    for i in range(1, data_count + 1):
        socket.send(("TOP " + str(i) + " 0" + '\r\n').encode())
        data = ""
        raw_data = ''
        while not raw_data.startswith('.') and not raw_data.startswith('\r\n'):
            raw_data = socket.recv(1024).decode()
            if raw_data[:2] == '-E':
                break
            data += raw_data
        from_field = data.split('\nFrom:')[1].split("\n")[:7]
        sender, address, subject = get_sender_and_subject(from_field)
        print('({0})---{3} | {1} {2}'.format(str(i), sender, address, subject))


def show_inbox(socket):
    socket.send(("LIST" + '\r\n').encode())
    data = ""
    raw_data = ''
    while raw_data[-3:] != '.\r\n':
        raw_data = socket.recv(1024).decode()
        data += raw_data
    data_count = len(data.split('\r\n')) - 3
    print("You have " + str(data_count) + " messages in your mailbox")
    list_messages(socket, data_count)

    # print (data)


def get_letter_parts(data, boundary):
    parts = data.split('--'+boundary)
    for i in range(1,len(parts)-1):
        content_type = re.findall(r'Content-Type.*', parts[i])
        if content_type[0].startswith('Content-Type: text'):
            print (parts[i][len(content_type[0])+5:])
        else:
            filename = re.findall(r'name=.*', parts[i])[0]
            code = re.findall(r'=?(.*?)?=',filename)[-1].split('?')[3]
            name = base64.b64decode(code).decode('utf-8')
            buffer = ''
            img_data = ''
            for j in range(len(parts[i])):
                buffer += parts[i][j]
                if buffer.endswith('\r\n\r\n'):
                    # print('puw')
                    buffer = ''
                    img_data = parts[i][j+1:].encode()
                    # print (img_data)
                    break

            # img_data = parts[i][parts[i].index(r'\r\n\r\n'):]
            with open ('attachments/'+str(datetime.datetime.now())+'_'+name, 'wb') as f:
                f.write(base64.decodebytes(img_data))
            print(name)
        # print (content_type)

    # print (len(parts[0]))
    return []


def encode_letter(data):
    date = ""
    sender = ""
    address = ""
    reciever = ""
    subject = ""
    parts = data.split('\r\n')
    for i in range(len(parts)):
        if parts[i].lstrip('\t').startswith("Date"):
            date = parts[i].lstrip('\t')
        elif parts[i].lstrip('\t').startswith("From:"):
            sender, address = encode_sender(parts[i:i+2])
        elif parts[i].lstrip('\t').startswith("To:"):
            reciever = parts[i].lstrip('\t')
        elif parts[i].lstrip('\t').startswith("Subject:"):
            subject = encode_subject(parts[i:i+2])
        elif parts[i].lstrip('\t').startswith("Content-Type:"):
            boundary = re.findall(r'boundary.*', parts[i])
            if len(boundary) != 0:
                boundary_value = boundary[0].split('=')[1].lstrip().rstrip()
                # print (boundary_value)
                print_header(address, date, reciever, sender, subject)
                get_letter_parts(data, boundary_value)
                break
            else:
                print_formatted_letter(address, date, i, parts, reciever, sender, subject)
        else:
            pass

            # get boundary and process each part in multipart
        # 'Content-Type: multipart/mixed; boundary =6417766050356464863'
        # elif not parts[i]:

        #     break

    pass


def print_formatted_letter(address, date, i, parts, reciever, sender, subject):
    print_header(address, date, reciever, sender, subject)
    # print ('Found text in '+ str(i) + ' line')
    content = ''
    for j in range(i + 5, len(parts)):
        if not parts[j]:
            content += '|\n'
        elif parts[j] != '.':
            content += '| ' + parts[j] + '\n'
    print(content)


def print_header(address, date, reciever, sender, subject):
    print(
        ''.zfill(max(len(date) + 2, len(sender + address) + 3, len(reciever) + 2, len(subject) + 11)).replace('0', '-'))
    print('| {0}\n| {1} {2}\n| {3}\n| Subject: {4}'.format(date, sender, address, reciever, subject))
    print(
        ''.zfill(max(len(date) + 2, len(sender + address) + 3, len(reciever) + 2, len(subject) + 11)).replace('0', '-'))


def show_letter(socket, choice):
    socket.send(('RETR ' + choice + '\r\n').encode())
    data = ""
    raw_data = ''
    while not raw_data.startswith('.'):
        raw_data = socket.recv(1024).decode()
        if raw_data[:2] == '-E':
            break
        data += raw_data
    encode_letter(data)
    # print (data)


if __name__ == '__main__':
    email = 'test.katy.solo@yandex.ru'
    password = 'qwertyKate98'
    try:
        socket = establlish_connection()
        auth_user(socket, ['USER ' + email, 'PASS ' + password])
        show_inbox(socket)
        choice = input('Enter letter number to open: ')
        show_letter(socket, choice)
    except AuthenticationError:
        print('Wrong login/password')
    finally:
        socket.close()
