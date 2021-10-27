from QR_decoder import QR_decode
import qrcode

#function takes in text to encode and file_name to save the encoding to
#it uses inputted version defaulting to 1 and inputted fill color defaulting to black
def QR_create(text, file_name, qr_version=1, qr_color="black"):
    #Create the QR Code object
    qr = qrcode.QRCode(
        version = qr_version,
        error_correction = qrcode.constants.ERROR_CORRECT_H, #Levels: L, M, Q, H
        box_size = 10,
        border=5
    )

    qr.add_data(text) #encode the inputted text into the qrcode
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color='white')
    img.save(file_name) #name of qrcode file to save it to

    return img

if __name__ == "__main__":
    #First QR Code being tested
    qr1_text = "Tiny baby QR Code :)"
    qr1_file = "qr1.png"

    #Second QR Code being tested
    qr2_text = "Scary looking QR Code!!!"
    qr2_file = "qr2.png"

    #Creation of both QR codes
    qr1 = QR_create(qr1_text, qr1_file, 1, "black")
    qr2 = QR_create(qr2_text, qr2_file, 40, "red") #unreadable at 20 or more 
    
