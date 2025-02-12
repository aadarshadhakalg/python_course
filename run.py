from animal.dog import Dog
from animal.human import Human
import os




jimmy = Dog("Jimmy")
harish = Human("Harish")

jimmy.make_sound()
harish.make_sound()

# Python standard library
# importing p[ackages that comes with pyhon
os.makedirs("folder", exist_ok=True)


# Third Party Packages
# From Python Package Index i.e pypi
# PIP looks for package in pypi

# pip install qrcode
# pip install pillow
# pip install requests
# pip freeze > requirements.txt
# pip install -r requirements.txt
# pip uninstall requests
import qrcode
qr = qrcode.QRCode()
qr.add_data("Hello!")
img = qr.make_image()
img.save("hello_qr.png")