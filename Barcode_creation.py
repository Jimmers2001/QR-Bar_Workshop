from barcode import EAN13 # a type of format
from barcode.writer import ImageWriter #to save the barcode as a png file

def barcode_create(file_name, digits):
    with open(file_name, 'wb') as f: #write in binary mode
        #numbers written in barcode where the last one is automatically generated
        EAN13(digits, writer=ImageWriter()).write(f) 

if __name__ == "__main__":
    #Command to run: python3 barcode_creation.py
    file_name = "workshop_barcode.png"
    digits = "346297563925697"
    
    barcode_create(file_name, digits)
