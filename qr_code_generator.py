from urllib.request import url2pathname
import pyqrcode
from pyqrcode import QRCode

# input
url = "https://www.google.com/"

# Generate QR code
qr_url = pyqrcode.create(url)

# Create and save file"
qr_url.svg("qr.svg", scale=8)
