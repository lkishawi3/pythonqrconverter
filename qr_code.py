import pyqrcode
import png
from pyqrcode import QRCode
text = input("Please enter the text to convert: ")
img = input("Please enter the image name: ")
img = img + ".png"
url = pyqrcode.create(text)
url.show()
url.png(img,scale=6)