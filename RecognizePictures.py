@bot.register(test_group, PICTURE)
def analysisPicture(msg):
	#分析是否包含二维码
	#如果有二维码，分析是否是入群码
	#如果是入群邀请，点击确认加入群聊
	return


import pyzbar.pyzbar as pyzbar
from PIL import Image

image = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\Test\\Picture\\IMG_7139.JPG'
img = Image.open(image)
img.show()
barcodes = pyzbar.decode(img)

for barcode in barcodes:
	barcodeData = barcode.data.decode("utf-8")
	print (barcodeData)
