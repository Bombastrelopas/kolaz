import sys
import operator
import os, sys
from PIL import Image

#Important Variables
kolaz = Image.new("RGB", (6000,3000))
#Master


#constants
x0 = 0
y0 = 1
x1 = 2
y1 = 3

x = 0
y = 1

def nextbox(lastImageBB, dimensions):
    finalTup =(lastImageBB[x1], 0 , lastImageBB[x1]+dimensions[x], dimensions[y])
    return finalTup

imagelist = []
path = "C:/Users/ioann/Desktop/Images/"
for image in os.listdir(path):
    if os.path.isfile(path + image):
        try:
            print(os.path.isfile(path + image))
            imagelist.append(Image.open(path+image))
        except OSError:
            pass


print(imagelist)



agumon = Image.open("C:/Users/ioann/Desktop/agumon2.gif")
kolaz.paste(agumon, agumon.getbbox())
agumon2 = Image.open("C:/Users/ioann/Desktop/agumon.jpg")
#Get Bounding box for next image and paste it on the kolaz
newbbox = nextbox(kolaz.getbbox(), agumon2.size)
kolaz.paste(agumon2, newbbox)

#kolaz.show()
print(kolaz.getbbox())


