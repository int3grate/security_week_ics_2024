import random
import re

import socket
import base64

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_addr = 'boxofhorror.org'
port = 1234
sock.connect((ip_addr, port))

sock.recv(1024)

def do_encrypt(sock, password):
    password += "\r\n"
    sock.send(password.encode('utf-8'))
    data = sock.recv(2048)
    lines = data.split()
    data = base64.b64decode(lines[0])
    return len(data)

rand_chars = "!@#$%^&*()-+=><,.?/';:\\/|`~"
cur_buf = "flag{"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}"

print("setting up initial buffer...")
pre_buf = ""
cur_len = do_encrypt(sock, cur_buf)
for i in range(0,16):
    pre_buf += random.choice(rand_chars)
    if(do_encrypt(sock, pre_buf + cur_buf) > cur_len):
        cur_buf = pre_buf[:-1] + cur_buf
        break

print("cracking...")
while(True):
    if("}" in cur_buf):
        break
    for c in charset:
        enc = do_encrypt(sock, cur_buf + c)
        if(enc == cur_len):
                cur_buf += c
                print("cur_buf: %s" % cur_buf)
                break

    if(cur_len != enc):
        cur_len = enc
        print("adjusting buffer...")
        pre_buf = ""
        for i in range(0,16):
            pre_buf += random.choice(rand_chars)
            if(do_encrypt(sock, pre_buf + cur_buf) > cur_len):
                cur_buf = pre_buf[:-1] + cur_buf
                break

m = re.search("(flag{.+})", cur_buf)
print("done")
print("flag: " + m.group(1))
