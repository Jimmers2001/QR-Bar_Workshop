from pyzbar.pyzbar import decode
from PIL import Image

def QR_decode(qr_file):
    img = Image.open(qr_file) #open up the image to be decoded
    result = decode(img) #decode and store a list of pieces of decoded data

    for i in result: #print out the results of the decoding in utf-8
        print(i.data.decode("utf-8"))

if __name__ == "__main__":
    #command to run: python QR_decoder.py
    qr_file1 = 'qr1.png'
    qr_file2 = 'qr2.png'
    
    QR_decode(qr_file1)
    QR_decode(qr_file2)
