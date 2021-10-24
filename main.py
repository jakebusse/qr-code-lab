import qrcode
import cv2
import os
from os.path import exists
import webbrowser

def runApp():
    print('Would you like to create a QR code, decode a QR code, or delete a QR code? (Type C (for create), D (for decode), or BS (for delete)).')
    action = input()

    if action.upper() == 'C':
        content = input("What do you want the QR Code to represent? ")
        create(content)
    elif action.upper() == 'D':
        decode()
    elif action.upper() == 'BS':
        delete()
    else:
        print('INVALID RESPONSE')
        runApp()

def create(content):
    name = input("What do you want the file name to be (omit the extension)? ")
    if '.' in name:
        print("File name cannot contain '.'")
        create(content)
    else:
        pass
    file_exists = exists(name + ".jpg")
    if file_exists == True:
        print("FILE ALREADY EXISTS")
        replace = input("Would you like to replace it? (Answer Y/N) ")
        if replace.upper() == "Y":
            pass
        else:
            create(content)
    newCode = qrcode.make(content)
    newCode.save(name + ".jpg")

def decode():
    name = input("File name of QR Code to decode (omit the extension): ")
    file_exists = exists(name + ".jpg")
    if file_exists == True:
        d = cv2.QRCodeDetector()
        val, _, _ = d.detectAndDecode(cv2.imread(name + ".jpg"))
        print("Decoded text is: ", val)
        if 'http' in val:
            url = True
        else:
            url = False
        if url == True:
            openUrl = input('Looks like this is a URL. Would you like to open it? (Answer Y/N) ')
            if openUrl.upper() == "Y":
                webbrowser.open(val)
            else:
                pass
    else:
        print("FILE DOES NOT EXIST")
        createFile = input("Would you like to create a new QR code with this file name. (Answer Y/N) ")
        if createFile.upper() == "Y":
            content = input('What do you want the QR Code to represent? ')
            create(content)
        else:
            decode()

def delete():
    name = input("File name of QR Code to be deleted (omit extension): ")
    file_exists = exists(name + ".jpg")
    if file_exists == True:
        os.remove(name + ".jpg")
    else:
        print("FILE DOES NOT EXIST")
        runApp()

runApp()