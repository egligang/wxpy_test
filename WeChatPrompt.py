import pyzbar.pyzbar as pyzbar
from PIL import Image
from wxpy import *

bot = Bot()

@bot.register(test_group, PICTURE)
def analysisPicture(msg):
	#分析是否包含二维码
        #打开图片
        img = Image.open(msg.picture)
        #如果有二维码，分析是否是入群码
        barcodes = pyzbar.decode(img)
        barcodeData = barcodes[0].data.decode("utf-8")
        #如果不是入群邀请则返回
        if barcodeData[8:23] != 'weixin.qq.com/g':
                return
        else:
                #如果是入群邀请，提醒用户操作
	return

embed()
