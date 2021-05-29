import sys, pygame
potato = pygame.image.load("potato.png")
pygame.init()
speed=20
agility=5
size = width, height = 800, 750
charpos=[width/2,height-50,50,40]
screen = pygame.display.set_mode(size)
GameClock = pygame.time.Clock()
backgroundcolor= 0,0,0
rectcolor= 200,0,0
#potato= pygame.image.load("potato.png")

#class bullets:
 #   def __init__(x,y,self,img):



def collide(obj1,obj2):
    offsetx=obj2.x-obj1.x
    offsety=obj2.y-obj2.y
    return obj1.mask.overlap(obj2.mask, (offsetx,offsety))

def reset():
    screen.fill(backgroundcolor)
    pygame.draw.rect(screen, rectcolor,charpos,0)
while 1:
    GameClock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_LEFT] and charpos[0]>0:
        charpos[0] = charpos[0]-agility
    if keypressed[pygame.K_RIGHT] and charpos[0]<(width-charpos[2]):
        charpos[0] = charpos[0]+agility
    reset()
   # if keypressed[pygame.K_SPACE]

    pygame.display.flip()
pygame.quit()