from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def decrypt_oracle(b64_data, b64_iv):
    key = b'unknown_key12345'
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
