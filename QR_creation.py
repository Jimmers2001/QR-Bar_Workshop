import qrcode

#function that takes data, encodes it into the QR code, and returns the png file of the QR Code
def create_QR(text, file_name, qr_version):
    #Create the QR Code object
    qr = qrcode.QRCode(
        version = qr_version,
        error_correction = qrcode.constants.ERROR_CORRECT_L, #L, M, Q, H
        box_size = 10,
        border=5
    )

    qr.add_data(text) #encode the inputted text into the qrcode
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name) #name of qrcode file to save it to

    return img

if __name__ == "__main__":
    qr1_text = "Testing text 1"
    qr1_file = "my_qr1.png"

    qr2_text = "Testing text 2"
    qr2_file = "my_qr2.png"

    qr1 = create_QR(qr1_text, qr1_file, 1)
    qr2 = create_QR(qr2_text, qr2_file, 40)
    
