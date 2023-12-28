import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1 , 
error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=10,
border=4 ,)
qr.add_data("http://www.linkedin.com/in/prerna-arora-6677-cse")
qr.make(fit = True)
img=qr.make_image(fill_color = "BLUE",back_color = "black")
img.save("PrernaArora_LINKDIN.png")
