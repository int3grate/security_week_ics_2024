import random
import re
import socket
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import binascii

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_addr = 'boxofhorror.org'
port = 4321
sock.connect((ip_addr, port))

res = sock.recv(1024)

qrs = 0
def call_decrypt(blocks):
    global qrs
    qrs += 1
    data = b''
    for i in range(1, len(blocks)):
        data += blocks[i]
    iv = blocks[0]

    to_send = base64.b64encode(data) + b"," + base64.b64encode(iv) + b"\r\n"
    sock.send(to_send)
    data = sock.recv(2048)
    data = data.strip()
    data = data.decode('utf-8')

    fields = data.split('\r')
    return fields[0]

b64_data = "rDxVtvcl/fA6x33iBY8Bwo/1l7wEUT8SqRhi5WZFDVEz4KmsUkBXLXHH/CWCD5qg/LA1EIhVImmxBQDeMgZSo1w8IvVyUcq+SUh6jAerndo="
b64_iv = "R40qxRE9vHKz18Oz1jaRjA=="

data = base64.b64decode(b64_data)
data_len = len(data)
print("Data: %s" % binascii.hexlify(data).decode('utf-8'))
print("Data Length: %d" % data_len)

num_blocks = int(data_len / 16)
print("Number Blocks: %d" % int(data_len / 16))

iv = base64.b64decode(b64_iv)
print("IV: %s" % binascii.hexlify(iv).decode('utf-8'))

blocks = []
blocks.append(iv)
for i in range(0, num_blocks):
    block = data[i*16:(i*16)+16]
    blocks.append(block)

recovered_plaintext = b''
for i in range(len(blocks)-2, -1, -1):
    orig_bytes = blocks[i]
    tamper_block = bytearray(b'xxxxxxxxxxxxxxxx')
    pad_bytes = 1
    solved_bytes = bytearray(b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0')

    for j in range(15, -1, -1):
        # setup padding from already discovered bytes
        if(j < 15):
            for l in range(15, j, -1):
                tamper_block[l] = solved_bytes[l] ^ pad_bytes

        for k in range(0, 256):
            tamper_block[j] = k
            tamper_block_bytes = bytes(tamper_block)
            blocks[i] = tamper_block_bytes
            retval = call_decrypt(blocks)
            if(retval == "success"):
                s = k ^ pad_bytes
                solved_bytes[j] = s
                pad_bytes += 1
                break

    blocks = blocks[0:-1]
    tmp = bytearray()
    for q in range(0, 16):
        tmp.append(solved_bytes[q] ^ orig_bytes[q])

    # reset block
    blocks[i] = orig_bytes
    recovered_plaintext = bytes(tmp) + recovered_plaintext

print(recovered_plaintext)
print(qrs)
