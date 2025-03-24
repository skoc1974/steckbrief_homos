import os
import qrcode
import base64

data = {
    'HomoSapiens': "https://skoc1974.github.io/steckbrief_homos/homo%20sapiens.html",
    'HomoNeanderthalensis': "https://skoc1974.github.io/steckbrief_homos/homo%20neanderthalensis.html",
    'HomoHeidelbergensis': "https://skoc1974.github.io/steckbrief_homos/homo%20heidelbergensis.html"
}

for homo, url in data.items():

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img.save(f"{homo}.png")


