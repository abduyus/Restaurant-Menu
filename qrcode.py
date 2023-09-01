import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("https://127.0.0.1:8000")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("image.png")


