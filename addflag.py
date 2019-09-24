from PIL import Image as img
import os

orig=r"avator.jpg"
flag=r"flag.png"
opic=img.open(orig)
fpic=img.open(flag)


x=opic.width//2
y=opic.height//2
if(x==y):
    opic=opic.resize((546,546),img.ANTIALIAS)
else:
    box=(x-546//2,y-546//2,x+546//2,y+546//2)
    opic=opic.crop(box)
fpic.resize((546,546),img.ANTIALIAS)
r,g,b,a=fpic.split()
opic.paste(fpic,(0,0),mask=a)
opic.save(r"withFlag.jpg")
