import pyqrcode

# String which represent the QR code
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

# Generate QR code
url = pyqrcode.create(s)
