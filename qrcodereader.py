from pyzbar.pyzbar import decode
from PIL import Image

print("QR-Code Reader")

img = Image.open("QrCode.png")

d = decode(img)

print(d)

#brew install zbar if error