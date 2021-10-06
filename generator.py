import qrcode
# Link for website
input_data = "https://drive.google.com/file/d/12AyZoyaL49sQbV_RBJ8puNAR6Uvf84G3/view?usp=drivesdk"
#Creating an instance of qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=3)
qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('elizabeth.png')
