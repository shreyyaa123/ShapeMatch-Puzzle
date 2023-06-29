import pygame
import os
import time
#Screen
screenLength = 800
screenHeight = 500
dim_field = (screenLength, screenHeight)
screen = pygame.display.set_mode(dim_field)

#420, 420 = frame sizes

#Background
background = pygame.image.load(os.path.join("wood1.jpg")).convert()
background = pygame.transform.scale(background, dim_field)

# WIN TEXT LEVEL 1
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50)
winText = font.render("Congratulations! Level 1 Complete!", True, (255, 255, 255))
winText2 = font.render("Press ENTER to advance to Level 2", True, (255, 255, 255))
rect_frame = pygame.Rect(270,200,260,260)
rect_frame1 = pygame.Rect(255,190,305,305)
#Text Level 2
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50)
endText = font.render("Yay! You've completed this game!", True, (255, 255, 255))

pygame.font.init()
font1 = pygame.font.SysFont("comicsans", 50)

#Level 1 Dragging
#Pink Dragging
rectangle_dragingp = False
#Yellow Dragging
rectangle_dragingy = False
#Red Dragging
rectangle_dragingr = False
#Cyan Dragging
rectangle_dragingc = False
#Green Dragging
rectangle_dragingg = False
#Violet Dragging
rectangle_dragingv = False
#Purple Dragging
rectangle_dragingpu = False
#Level 1 Sprites
#Cat Sprite
catSprite = pygame.image.load(os.path.join("catsquare.jpg")).convert()
catSprite = pygame.transform.scale(catSprite, (260,260))
#Frame
frameSprite = pygame.image.load(os.path.join("frame.png")).convert()
frameSprite = pygame.transform.scale(frameSprite, (260,260))
#Pink Sprites
pinkSprite = pygame.image.load(os.path.join("Shapes", "Pink_T.png"))
pinkSprite = pygame.transform.scale(pinkSprite, (126,126))
pinkSprite.convert
rect_pink = pygame.Rect(50, 350, 200,200)
#Red Sprite
redSprite = pygame.image.load(os.path.join("Shapes", "Red_T.png"))
redSprite = pygame.transform.scale(redSprite, (252,126))
redSprite.convert
rect_red = pygame.Rect(170,45,200,200)
#Violet Sprite
violetSprite = pygame.image.load(os.path.join("Shapes","Violet_P.png"))
violetSprite = pygame.transform.scale(violetSprite, (63,189))
violetSprite.convert
rect_violet = pygame.Rect(65,50,200,200)
#Green Sprite
greenSprite = pygame.image.load(os.path.join("Shapes","Green_T.png"))
greenSprite = pygame.transform.scale(greenSprite, (63,124))
greenSprite.convert
rect_green = pygame.Rect(515,30,200,200)
#Cyan Sprite
cyanSprite = pygame.image.load(os.path.join("Shapes","Cyan_T.png"))
cyanSprite = pygame.transform.scale(cyanSprite, (124,62))
cyanSprite.convert
rect_cyan = pygame.Rect(45,260,200,200)
#Purple Sprite
purpleSprite = pygame.image.load(os.path.join("Shapes","Purple_S.png"))
purpleSprite = pygame.transform.scale(purpleSprite, (126,126))
purpleSprite.convert
rect_purple = pygame.Rect(650,330,200,200)
#Yellow Sprite
yellowSprite = pygame.image.load(os.path.join("Shapes","Yellow_T.png"))
yellowSprite = pygame.transform.scale(yellowSprite, (126,252))
yellowSprite.convert
rect_yellow = pygame.Rect(610,50,200,200)
# instructions Sprite
instructionsSprite = pygame.image.load(os.path.join( "instructions.png")).convert()
instructionsSprite = pygame.transform.scale(instructionsSprite, (800, 500))
rect_instructions = pygame.Rect(0, 0, 800, 500)
(mx, my) = pygame.mouse.get_pos()

#Level 2 Sprites/Rectangles 
#tiger Sprite
tigerSprite = pygame.image.load(os.path.join("tiger.jpg")).convert()
tigerSprite = pygame.transform.scale(tigerSprite, (305,305))
#Frame
frame1Sprite = pygame.image.load(os.path.join("frame.png")).convert()
frame1Sprite = pygame.transform.scale(frame1Sprite, (305,305))
#Pink2 Sprites
pink2Sprite = pygame.image.load(os.path.join("Shapes2","Pink2.png"))
pink2Sprite = pygame.transform.scale(pink2Sprite, (189,95))
pink2Sprite.convert
rect_pink2 = pygame.Rect(250, 50, 200,200)
#Blue2 Sprite
blue2Sprite = pygame.image.load(os.path.join("Shapes2","Blue2.png"))
blue2Sprite = pygame.transform.scale(blue2Sprite, (194,192))
blue2Sprite.convert
rect_blue2 = pygame.Rect(575, 30, 200,200)
#white2 Sprite
white2Sprite = pygame.image.load(os.path.join("Shapes2","White2.png"))
white2Sprite = pygame.transform.scale(white2Sprite, (192, 98))
white2Sprite.convert
rect_white2 = pygame.Rect(430, 50, 200,200)
#Green2 Sprite
green2Sprite = pygame.image.load(os.path.join("Shapes2","Green2.png"))
green2Sprite = pygame.transform.scale(green2Sprite, (98,98))
green2Sprite.convert
rect_green2 = pygame.Rect(50, 275, 200,200)
#Orange2 Sprite
orange2Sprite = pygame.image.load(os.path.join("Shapes2","Orange2.png"))
orange2Sprite = pygame.transform.scale(orange2Sprite, (192,194))
orange2Sprite.convert
rect_orange2 = pygame.Rect(50, 50, 200,200)
#Purple2 Sprite
purple2Sprite = pygame.image.load(os.path.join("Shapes2","Purple2.png"))
purple2Sprite = pygame.transform.scale(purple2Sprite, (93,92))
purple2Sprite.convert
rect_purple2 = pygame.Rect(50, 400, 200,200)
#Red2 Sprite
red2Sprite = pygame.image.load(os.path.join("Shapes2","Red2.png"))
red2Sprite = pygame.transform.scale(red2Sprite, (93,92))
red2Sprite.convert
rect_red2 = pygame.Rect(600, 250, 200,200)
#Yellow2 Sprite
yellow2Sprite = pygame.image.load(os.path.join("Shapes2","Yellow2.png"))
yellow2Sprite = pygame.transform.scale(yellow2Sprite, (194,98))
yellow2Sprite.convert
rect_yellow2 = pygame.Rect(570, 400, 200,200)

#Level 2 Dragging
rectangle_draggingb = False
rectangle_draggingg = False
rectangle_draggingo = False
rectangle_draggingp = False
rectangle_draggingpu = False
rectangle_draggingr = False
rectangle_draggingw = False
rectangle_draggingy = False

clock = pygame.time.Clock()
FPS = 60

#While loop Variables
level1 = True
level2 = False
qPressed = False
gameWon = False
gameWon2 = False
endGame = False
movecounter = 0

#Snap function for placement of Sprites
def snap1(rect_col, rect_f, y1, y2, y3, x1, x2, x3):
  if (rect_col.y > rect_f.y + y1) and (rect_col.y < rect_f.y + y2) and (rect_col.x > rect_f.x + x1) and (rect_col.x < rect_f.x + x2):
    rect_col.x = x3
    rect_col.y = y3
    
#Offset for mouse button down
def mousedown (rect_col, rectangle_dragingz, mouse_x, mouse_y):
    rectangle_dragingz = True
    offset_x = rect_col.x - mouse_x
    offset_y = rect_col.y - mouse_y
    return offset_x, offset_y, rectangle_dragingz

while (qPressed == False):
  while (level1):
    screen.blit(instructionsSprite, rect_instructions)
    pygame.display.update()
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
      break

  #Level 1 Starts Here
  while (level1):
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    #https://stackoverflow.com/questions/41332861/click-and-drag-a-rectangle-with-pygame for event in pygame.event.get():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        level1 = False

      #Mousebuttondown = while at certain location, sets the drag of that shape to true. Offset fixes mouse location

      elif event.type == pygame.MOUSEBUTTONDOWN:
        (mx, my) = pygame.mouse.get_pos()
        movecounter += 1
        if (my > rect_pink.y + 63) and (my < rect_pink.y + 126) and (mx > rect_pink.x) and (mx < rect_pink.x + 63):
          mouse_x, mouse_y = event.pos
          offset_x, offset_y, rectangle_dragingp = mousedown (rect_pink, rectangle_dragingp, mouse_x, mouse_y)
        
        if (my > rect_yellow.y + 45) and (my < rect_yellow.y + 155) and (mx > rect_yellow.x + 35) and (mx < rect_yellow.x + 126):
          mouse_x, mouse_y = event.pos
          offset_x, offset_y, rectangle_dragingy = mousedown (rect_yellow, rectangle_dragingy, mouse_x, mouse_y)

        if (my > rect_red.y) and (my < rect_red.y + 63) and (mx > rect_red.x + 84) and (mx < rect_red.x + 168):
          mouse_x, mouse_y = event.pos
          offset_x, offset_y, rectangle_dragingr = mousedown (rect_red, rectangle_dragingr, mouse_x, mouse_y)

        if (my > rect_green.y + 42) and (my < rect_green.y + 84) and (mx > rect_green.x) and (mx < rect_green.x + 32):
          mouse_x, mouse_y = event.pos
          offset_x, offset_y, rectangle_dragingg = mousedown (rect_green, rectangle_dragingg, mouse_x, mouse_y)

        if (my > rect_purple.y + 35) and (my < rect_purple.y + 100) and (mx > rect_purple.x + 35) and (mx < rect_purple.x + 100):
          mouse_x, mouse_y = event.pos
          offset_x, offset_y, rectangle_dragingpu = mousedown (rect_purple, rectangle_dragingpu, mouse_x, mouse_y)

        if (my > rect_cyan.y + 20) and (my < rect_cyan.y + 70) and (mx > rect_cyan.x + 35) and (mx < rect_cyan.x + 95):
          mouse_x, mouse_y = event.pos
          offset_x, offset_y, rectangle_dragingc = mousedown (rect_cyan, rectangle_dragingc, mouse_x, mouse_y)

        if (my > rect_violet.y) and (my < rect_violet.y + 189) and (mx > rect_violet.x) and (mx < rect_violet.x + 63):
          mouse_x, mouse_y = event.pos
          offset_x, offset_y, rectangle_dragingv = mousedown (rect_violet, rectangle_dragingv, mouse_x, mouse_y)
      
      #Mousebuttonup = release the shape  
      #Rectangle draging = false = shape does not move  
      elif event.type == pygame.MOUSEBUTTONUP:
        rectangle_dragingp = False
        rectangle_dragingy = False
        rectangle_dragingr = False
        rectangle_dragingg = False
        rectangle_dragingpu = False
        rectangle_dragingc = False
        rectangle_dragingv = False

      #Mousemotion = while mouse is moving, dragging is true, and the shape's x and y coordinates are set to the mouse's coordinates (aka drag), along with offset to make the shape location more accurate and centered
      elif event.type == pygame.MOUSEMOTION:
        if rectangle_dragingp:
          mouse_x, mouse_y = event.pos
          rect_pink.x = mouse_x + offset_x
          rect_pink.y = mouse_y + offset_y
          
        if rectangle_dragingy:
          mouse_x, mouse_y = event.pos
          rect_yellow.x = mouse_x + offset_x
          rect_yellow.y = mouse_y + offset_y

        if rectangle_dragingr:
          mouse_x, mouse_y = event.pos
          rect_red.x = mouse_x + offset_x
          rect_red.y = mouse_y + offset_y
        
        if rectangle_dragingg:
          mouse_x, mouse_y = event.pos
          rect_green.x = mouse_x + offset_x
          rect_green.y = mouse_y + offset_y
        
        if rectangle_dragingpu:
          mouse_x, mouse_y = event.pos
          rect_purple.x = mouse_x + offset_x
          rect_purple.y = mouse_y + offset_y

        if rectangle_dragingc:
          mouse_x, mouse_y = event.pos
          rect_cyan.x = mouse_x + offset_x
          rect_cyan.y = mouse_y + offset_y
  
        if rectangle_dragingv:
          mouse_x, mouse_y = event.pos
          rect_violet.x = mouse_x + offset_x
          rect_violet.y = mouse_y + offset_y

    #Pink Snap
    snap1(rect_pink, rect_frame, 110, 260, 330, 0, 150, 275)
    #Red Snap
    snap1(rect_red, rect_frame, 0, 130, 206, 0, 260, 275)
    #Yellow Snap
    snap1(rect_yellow, rect_frame, 0, 200, 205, 100, 150, 400)
    #Cyan Snap
    snap1(rect_cyan, rect_frame, 180, 260, 395, 110, 260, 405)
    #Violet Snap
    snap1(rect_violet, rect_frame, 0, 170, 205, 0, 70, 276)
    #Green Snap
    snap1(rect_green, rect_frame, 60, 130, 271, 45, 100, 339)
    #Purple Snap
    snap1(rect_purple, rect_frame, 115, 260, 332, 55, 170, 339)

    #Final location of pieces 
    purple = (rect_purple.x, rect_purple.y)
    green = (rect_green.x, rect_green.y)
    cyan = (rect_cyan.x, rect_cyan.y)
    pink = (rect_pink.x, rect_pink.y)
    red = (rect_red.x, rect_red.y)
    violet = (rect_violet.x, rect_violet.y)
    yellow = (rect_yellow.x, rect_yellow.y)

    MoveText = font1.render(str(movecounter), True, (0, 0, 0))
   
    #Drawing Everything
    screen.blit(background, (0,0))
    screen.blit(frameSprite,rect_frame)
    screen.blit(violetSprite, rect_violet)
    screen.blit(redSprite, rect_red)
    screen.blit(violetSprite, rect_violet)
    screen.blit(greenSprite, rect_green)
    screen.blit(cyanSprite, rect_cyan)
    screen.blit(yellowSprite, rect_yellow)
    screen.blit(pinkSprite, rect_pink)
    screen.blit(purpleSprite, rect_purple)
    screen.blit(MoveText, (750, 25))
    #Conditions for gameWon to be true
    
    if purple == ((339, 332)) and green == ((339, 271)) and violet == ((276,205)) and cyan == ((405,395)) and yellow == ((400, 205)) and red == ((275, 206)) and pink == ((275, 330)):
      rect_cyan.x = 339
      screen.blit(catSprite, (rect_frame.x, rect_frame.y))
      pygame.display.update()
      time.sleep(2)
      gameWon = True
    
    if (gameWon):
      screen.fill((0,0,0))
      screen.blit(winText, (105, 200))
      screen.blit(winText2, (105,240))
      gameWon2 = True
    
    if (gameWon2):
      pygame.event.get()
      keys = pygame.key.get_pressed()
      if keys[pygame.K_RETURN]:
        movecounter = 0
        level1 = False
        level2 = True

    pygame.display.update()
  
    #Level 2 Button Press 
    #Breaks out of level 1 WHILE LOOP and enters level 2 WHILE LOOP
    #Level 2 Starts Here
    while (level2): 
      clock.tick(FPS)
      keys = pygame.key.get_pressed()
      for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
          level2 = False
      
        elif event.type == pygame.MOUSEBUTTONDOWN:
          movecounter += 1
          (mx, my) = pygame.mouse.get_pos()

          if (my > rect_pink2.y + 49) and (my < rect_pink2.y + 92) and (mx > rect_pink2.x + 48) and (mx < rect_pink2.x + 142):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingp = mousedown (rect_pink2, rectangle_draggingp, mouse_x, mouse_y)

          if (my > rect_yellow2.y) and (my < rect_yellow2.y + 98) and (mx > rect_yellow2.x) and (mx < rect_yellow2.x + 194):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingy = mousedown (rect_yellow2, rectangle_draggingy, mouse_x, mouse_y)

          if (my > rect_red2.y + 46) and (my < rect_red2.y + 92) and (mx > rect_red2.x + 47) and (mx < rect_red2.x + 93):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingr = mousedown (rect_red2, rectangle_draggingr, mouse_x, mouse_y)
          if (my > rect_green2.y) and (my < rect_green2.y + 95) and (mx > rect_green2.x) and (mx < rect_green2.x + 95):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingg = mousedown (rect_green2, rectangle_draggingg, mouse_x, mouse_y)

          if (my > rect_purple2.y) and (my < rect_purple2.y + 46) and (mx > rect_purple2.x ) and (mx < rect_purple2.x + 46):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingpu = mousedown (rect_purple2, rectangle_draggingpu, mouse_x, mouse_y)

          if (my > rect_white2.y) and (my < rect_white2.y + 45) and (mx > rect_white2.x + 48) and (mx < rect_white2.x + 144):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingw = mousedown (rect_white2, rectangle_draggingw, mouse_x, mouse_y)

          if (my > rect_blue2.y + 96) and (my < rect_blue2.y + 192) and (mx > rect_blue2.x + 97) and (mx < rect_blue2.x + 194):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingb = mousedown (rect_blue2, rectangle_draggingb, mouse_x, mouse_y)

          if (my > rect_orange2.y) and (my < rect_orange2.y + 97) and (mx > rect_orange2.x) and (mx < rect_orange2.x + 96):
            mouse_x, mouse_y = event.pos
            offset_x, offset_y, rectangle_draggingo = mousedown (rect_orange2, rectangle_draggingo, mouse_x, mouse_y)

            #Mousebuttonup = release the shape  
            #Rectangle draging = false = shape does not move  
        elif event.type == pygame.MOUSEBUTTONUP:
          rectangle_draggingp = False
          rectangle_draggingy = False
          rectangle_draggingr = False
          rectangle_draggingg = False
          rectangle_draggingpu = False
          rectangle_draggingb = False
          rectangle_draggingw = False
          rectangle_draggingo = False

          #Mousemotion = while mouse is moving, dragging is true, and the shape's x and y coordinates are set to the mouse's coordinates (aka drag), along with offset to make the shape location more accurate and centered
        elif event.type == pygame.MOUSEMOTION:
          if rectangle_draggingp:
            mouse_x, mouse_y = event.pos
            rect_pink2.x = mouse_x + offset_x
            rect_pink2.y = mouse_y + offset_y
            
          if rectangle_draggingy:
            mouse_x, mouse_y = event.pos
            rect_yellow2.x = mouse_x + offset_x
            rect_yellow2.y = mouse_y + offset_y

          if rectangle_draggingr:
            mouse_x, mouse_y = event.pos
            rect_red2.x = mouse_x + offset_x
            rect_red2.y = mouse_y + offset_y
          
          if rectangle_draggingg:
            mouse_x, mouse_y = event.pos
            rect_green2.x = mouse_x + offset_x
            rect_green2.y = mouse_y + offset_y
          
          if rectangle_draggingpu:
            mouse_x, mouse_y = event.pos
            rect_purple2.x = mouse_x + offset_x
            rect_purple2.y = mouse_y + offset_y

          if rectangle_draggingb:
            mouse_x, mouse_y = event.pos
            rect_blue2.x = mouse_x + offset_x
            rect_blue2.y = mouse_y + offset_y
    
          if rectangle_draggingw:
            mouse_x, mouse_y = event.pos
            rect_white2.x = mouse_x + offset_x
            rect_white2.y = mouse_y + offset_y

          if rectangle_draggingo:
            mouse_x, mouse_y = event.pos
            rect_orange2.x = mouse_x + offset_x
            rect_orange2.y = mouse_y + offset_y
      #Snaps the shape in place at a specific coordinate
          
      #Pink Snap
      snap1(rect_pink2, rect_frame, 80, 200, 298, -15, 100, 260)
      #Red Snap
      snap1(rect_red2,rect_frame, 0, 92, 199, 130, 300, 462)
      #Yellow Snap
      snap1(rect_yellow2, rect_frame, -10, 140, 195, 100, 200, 360)
      #Blue Snap
      snap1(rect_blue2, rect_frame, 30, 300, 298, 75, 300, 360)
      #White Snap
      snap1(rect_white2, rect_frame, 70, 200, 295, 80, 175, 355)
      #Green Snap
      snap1(rect_green2, rect_frame, 94, 284, 392, -15, 105, 263)
      #Purple Snap
      snap1(rect_purple2, rect_frame, 98, 284, 394, 98, 191, 363)
      #Orange Snap
      snap1(rect_orange2, rect_frame, -15, 200, 195, -15, 200, 262)


      purple2 = (rect_purple2.x, rect_purple2.y)
      green2 = (rect_green2.x, rect_green2.y)
      white2 = (rect_white2.x, rect_white2.y)
      pink2 = (rect_pink2.x, rect_pink2.y)
      red2 = (rect_red2.x, rect_red2.y)
      blue2 = (rect_blue2.x, rect_blue2.y)
      yellow2 = (rect_yellow2.x, rect_yellow2.y) 
      orange2 = (rect_orange2.x, rect_orange2.y) 


      MoveText = font1.render(str(movecounter), True, (0, 0, 0))

      screen.blit(background, (0,0))
      screen.blit(frame1Sprite, rect_frame1)
      screen.blit(yellow2Sprite, rect_yellow2)
      screen.blit(blue2Sprite, rect_blue2)
      screen.blit(red2Sprite, rect_red2)
      screen.blit(green2Sprite, rect_green2)
      screen.blit(orange2Sprite, rect_orange2)
      screen.blit(pink2Sprite, rect_pink2)
      screen.blit(purple2Sprite, rect_purple2)
      screen.blit(white2Sprite, rect_white2)
      screen.blit(MoveText, (750,25))
      
      if purple2 == ((363, 394)) and green2 == ((263, 392)) and white2 == ((355,295)) and pink2 == ((260,298)) and red2 == ((462, 199)) and blue2 == ((360, 298)) and yellow2 == ((360, 195)) and orange2 == ((262,195)):
        rect_purple2.y = 290
        screen.blit(tigerSprite, (rect_frame1.x, rect_frame1.y))
        pygame.display.update()
        time.sleep(2)
        endGame = True

      if (endGame):
        screen.fill((0,0,0))
        screen.blit(endText, (105, 200)) 
        level2 = False
      pygame.display.update()


#w = 772 
#h = 770