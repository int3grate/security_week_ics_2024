import binascii
import base64
import socket

# Below is the data we'd like to decrypt using a remote padding oracle.  You will need to implement the code yourself to solve it.
# I will upload the solution a week after the event.

b64_data = "rDxVtvcl/fA6x33iBY8Bwo/1l7wEUT8SqRhi5WZFDVEz4KmsUkBXLXHH/CWCD5qg/LA1EIhVImmxBQDeMgZSo1w8IvVyUcq+SUh6jAerndo="
b64_iv = "R40qxRE9vHKz18Oz1jaRjA=="

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_addr = 'boxofhorror.org'
port = 4321
sock.connect((ip_addr, port))

res = sock.recv(1024)
def call_decrypt(blocks):
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
  # implement attack here
