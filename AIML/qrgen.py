import os
import qrcode

image = qrcode.make("https://www.linkedin.com/in/sayed-zaheer-abass/")
image.save("qr.png", "PNG")
os.system("qr.png")