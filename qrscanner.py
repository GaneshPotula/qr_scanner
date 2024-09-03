import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

my_scanner = qrcode.make("https://vrseconline.in/sahe/")
my_scanner.save("scan.png")

decoded_data = decode(Image.open("scan.png"))
print(decoded_data[0].data.decode("ascii"))
