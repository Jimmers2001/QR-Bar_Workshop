from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('barcode.png') #open up the image to be decoded
result = decode(img) #decode and store a list of pieces of decoded data
print(result)

for i in result: #print out the results of the decoding in utf-8
    print(i.data.decode("utf-8"))