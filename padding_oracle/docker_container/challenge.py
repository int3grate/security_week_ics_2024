import zlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import logging
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import base64

# wifi password
current_wifi_password = "flag{ICS_C0nf_c0mpress_chaLL}"

# 128 bit key
encryption_key = b'l38%jalsdj933$11'

def decrypt_oracle(b64_data, b64_iv):
    print("data:" + b64_data)
    print("iv:" + b64_iv)
    key = b'1829647392123210'

    try:
        iv = base64.b64decode(b64_iv)
    except:
        return "error=B64_IV"

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    try:
        data = base64.b64decode(b64_data)
    except:
        return "error=B64_DATA"

    plaintext = cipher.decrypt(data)

    try:
        plaintext = unpad(plaintext, 16)
        return "success"
    except:
        return "error=AES_PADDING"


class Challenge(Protocol):

    def dataReceived(self, data):
        data = data.strip().decode('utf-8')
        fields = data.split(',')
        b64_data = fields[0].strip()
        b64_iv = fields[1].strip()
        res = decrypt_oracle(b64_data, b64_iv).encode('utf-8')
        self.transport.write(res + b'\r\n')
        self.transport.write(b"Encrypted Token: ")

    def connectionMade(self):
        self.transport.write(b"Welcome to token validator\r\n")
        self.transport.write(b"b64_t0k3n, b64_iv: ")

    def __init__(self, factory):
        self.factory = factory
        self.debug = True

class ChallengeFactory(Factory):
    protocol = Challenge

    def buildProtocol(self, addr):
        return Challenge(self)

reactor.listenTCP(4321, ChallengeFactory())
reactor.run()
