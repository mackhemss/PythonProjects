import pyqrcode
import png

print("Welcome to Qr Generator")

msg = input("Type your secret message ")

code = pyqrcode.create(msg)

code.png("QrCode.png",scale=5)

print("QR code generated Succesfully")