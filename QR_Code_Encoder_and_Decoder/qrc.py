import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=40s

def encoder():
    data = input('Enter your data : ')
    fcolor = input('Enter your fill color : ')
    bcolor = input('Enter your back color : ')
    address = input('Enter your save file name and address (Ex. C:\Dir\img.png) : ')
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color = f'{fcolor}', back_color = f'{bcolor}')
    img.save(f'{address}')

def decoder():
    address = input('Enter your file name and address (Ex. C:\Dir\img.png) : ')
    
    img = Image.open(f'{address}')
    result = decode(img)
    
    print(result)
    
if __name__ == '__main__':
    print('Welcome to QR Code Encoder and Decoder\n')
    pick = input('Do you want to encode (0) or decode (1) ? ')
    pick = int(pick)
    if pick == 0:
        encoder()
    elif pick == 1:
        decoder()
    else:
        print('Error! Command is not valid!')
