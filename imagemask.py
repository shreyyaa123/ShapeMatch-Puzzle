'''from PIL import Image 
soup = Image.open("square.png")
(red, green, blue, transparency) = soup.getpixel((350,600))
print(red, green, blue, transparency)'''

def binarize(im):
  (width, height) = im.size
  for x in range (width):
    for y in range (height):
      (red, green, blue, transparency) = im.getpixel((x,y))
      if transparency == 0:
        transparency = 255
        red = 255
        blue = 255
        green = 255
        '''if green == 1:
          pass
        else: - code only added for extra outlines
          transparency = 0'''
      else:
        pass
      im.putpixel((x, y), (red, green, blue, transparency))

from PIL import Image 
soup = Image.open("square2.png")
binarize(soup)
soup.save("new.png")

''' pink = 225, red = (171, 1, 0), purple = 107, dark purple = (54, 18, 112) green = 65, cyan = (0, 226, 225), yellow = (228, 222, 51) random blacks = 40, 17, 15 19, 8, 7, 18, 39 probably'''

