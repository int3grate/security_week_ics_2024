from PIL import Image 

im = Image.open("atlanta2.png")
pixels = im.getdata()
width = im.width
height = im.height

data = bytearray()
for pixel in pixels:
    data.append(pixel[0])
    data.append(pixel[1])
    data.append(pixel[2])

from Crypto.Cipher import AES

# changing key bytes results in different colors in resulting image
key = b'xqsxsqqxxcxqqqol'

# try out ECB vs CBC mode
cipher = AES.new(key, AES.MODE_ECB)
#cipher = AES.new(key, AES.MODE_CBC)

padding_count = len(data) % 16

for i in range(0, 16-padding_count):
    data.append(0)

data_encrypted = cipher.encrypt(data)

im1 = Image.new(mode="RGB", size=(width, height))
pixels_new = im1.load()

for x in range(0, width):
    for y in range(0, height):
        offset = (y*width*3) + (x*3)
        pixels_new[x, y] = (data_encrypted[offset], data_encrypted[offset+1], data_encrypted[offset + 2])
        
print("done")
im1.save("atlanta2_encrypted.png")

# uncomment this to display in jupyter notebook
#display(im)
#display(im1)
