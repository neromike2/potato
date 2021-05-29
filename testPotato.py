import sys, pygame
import random
cooldown=0
bullet=[]
maxbullets=3
bulletspeed=5
bulletcount=0
potatosize=50
potato = pygame.image.load("potato.png")
asteroid=pygame.image.load("Asteroid2.png")
potato = pygame.transform.scale(potato, (potatosize, potatosize))
pygame.init()
ship = pygame.image.load("ship2.png")
ship= pygame.transform.rotate(ship,180)
speed=20
agility=5
size = width, height = 800, 750
charpos=[width/2,height-50]
screen = pygame.display.set_mode(size)
GameClock = pygame.time.Clock()
backgroundcolor= 0,0,0


class bullets:
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img
        self.mask=pygame.mask.from_surface(img)
        self.active=False


for bulletn in range(maxbullets):
    bullet.append(bullets(0,0,potato))

def collide(obj1,obj2):
    offsetx=obj2.x-obj1.x
    offsety=obj2.y-obj2.y
    return obj1.mask.overlap(obj2.mask, (offsetx,offsety)) != None

def reset():
    global bulletcount
    screen.fill(backgroundcolor)
    if bulletcount > 0:
        for bulletn in range(maxbullets):
            if bullet[bulletn].active:
                screen.blit(bullet[bulletn].img, (bullet[bulletn].x,bullet[bulletn].y))
                if bullet[bulletn].y<-50:
                    bullet[bulletn].active=False
                    bulletcount-=1
    screen.blit(ship,charpos)
    pygame.display.flip()

while 1:
    GameClock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_LEFT] and charpos[0]>0:
        charpos[0] = charpos[0]-agility
    if keypressed[pygame.K_RIGHT] and charpos[0]<(width-40):
        charpos[0] = charpos[0]+agility

    if keypressed[pygame.K_SPACE] and cooldown==0:
        print(bulletcount)
        freebullet=-1
        for bulletn in range(maxbullets):

            if not bullet[bulletn].active:
                freebullet=bulletn
        if freebullet>-1:
            print("Found free bullet at " + str(freebullet))
            bulletcount+=1
            bullet[freebullet].active=True
            bullet[freebullet].x = charpos[0]
            bullet[freebullet].y = charpos[1]
            cooldown+=speed
    if bulletcount > 0:
        for bulletn in range(maxbullets):
            if bullet[bulletn].active:
                bullet[bulletn].y -= bulletspeed
    if cooldown >0:
        cooldown-=1

    reset()
pygame.quit()