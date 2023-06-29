from PIL import Image 
soup = Image.open("Purple2.png")
print (soup.size)
# blue triangle = 257, 256
#orange triangle = 255, 257
# Green = 129, 129
#red = 123, 122
#yellow = 257, 129
# pink = 251, 125
# white = 256, 129
def imageoverlay(im, im2):
  (width, height) = im.size
  for x in range (width):
    for y in range (height):  
      (red, green, blue, transparency) = im.getpixel((x,y))
      if transparency == 255:
        (red1,green1,blue1)=im2.getpixel((x + 129, y + 258))
        im.putpixel((x, y), (red1, green1, blue1))
      else:
        pass

from PIL import Image 
soup = Image.open("Purple2.png")
bear = Image.open("tiger.jpg")
imageoverlay(soup, bear)
soup.save("new.png")
