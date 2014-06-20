from PIL import Image
import os
import random
from bisect import bisect

pwd = os.getcwd()

greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
            ]

zonebounds=[36,72,108,144,180,216,252]

FILE_PATH = r"E:\code\pythonStd\resource\3.jpg"

img = Image.open(FILE_PATH)

print img.format
print img.size
print img.mode

box = (100,100,500,500) #设置拷贝区域
#将图片的指定区域拷贝到region中，大小为box的大小
# region = img.crop(box)

# region = region.transpose(Image.ROTATE_180) #图片反转180 度

# img.paste(region,box)


# r, g , b , a = img.split() # 分割成4个通道
# r.show()
# g.show()
# b.show()
# a.show()

#img = Image.merge("RGBA",(b,g,r,a))  #将通道混合

img.show()
img = img.resize((160, 75),Image.BILINEAR)
img = img.convert("L")

str = ""

for y in range(0,img.size[1]):
    for x in range(0,img.size[0]):
        lum = 255 - img.getpixel((x,y))
        row=bisect(zonebounds,lum)
        possibles=greyscale[row]
        str=str+possibles[random.randint(0,len(possibles)-1)]
    str = str + "\n"

print str
