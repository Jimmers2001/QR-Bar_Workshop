import qrcode

#function that takes data, encodes it into the QR code, and returns the png file of the QR Code
def create_QR(input):
    #Create the QR Code object
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L, #L, M, Q, H
        box_size = 10,
        border=5
    )

    qr.add_data(input)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('my_qrcode.png') #name of qrcode file to save it to

    return img

if __name__ == "__main__":
    text1 = "crab"
    text2 = "schnozz"
    text3 = "meg"

    qr1 = create_QR(text1)
    qr2 = create_QR(text2)
    qr3 = create_QR(text3)
    
