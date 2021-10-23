from pyzbar.pyzbar import decode
from PIL import Image

def barcode_decode(barcode_file):
    img = Image.open(barcode_file) #open up the image to be decoded
    result = decode(img) #decode and store a list of pieces of decoded data

    for i in result: #print out the results of the decoding in utf-8
        print(i.data.decode("utf-8"))

if __name__ == "__main__":
    barcode_file = 'barcode.png'
    
    barcode_decode(barcode_file)

