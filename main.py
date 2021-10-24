import qrcode
import cv2
from os.path import exists

def runApp():
    print('Would you like to create or decode a QR code? (Type C (for create) or D (for decode)).')
    action = input()

    if action.upper() == 'C':
        create()
    elif action.upper() == 'D':
        decode()
    else:
        print('INVALID RESPONSE')
        runApp()

def create():
    content = input("What do you want the QR Code to represent? ")
    name = input("What do you want the file name to be (omit the extension)? ")
    file_exists = exists(name + ".jpg")
    print(file_exists)
    if file_exists == True:
        print("FILE ALREADY EXISTS")
        create()
    else:
        fileName = name
        newCode = qrcode.make(content)
        newCode.save(fileName + ".jpg")

def decode():
    name = input("File name of QR Code to decode (omit the extension): ")
    file_exists = exists(name + ".jpg")
    if file_exists == True:
        fileName = name
        d = cv2.QRCodeDetector()
        val, _, _ = d.detectAndDecode(cv2.imread(fileName + ".jpg"))
        print("Decoded text is: ", val)
    else:
        print("FILE DOES NOT EXIST")
        decode()

runApp()