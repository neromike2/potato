import sys, pygame
import random
import pygame.font
pygame.font.init()
font=pygame.font.Font('freesansbold.ttf', 22)
health=3
cooldown=0
bullet=[]
rock=[]
rocknum=0
rockcount=0
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
pygame.display.set_caption('space shooter')


class rocks:
    def __init__(self):
        self.x=random.randrange(25,(width-25))
        self.y=-75
        self.vy=random.randrange(1,5)
        if self.x > width/2:
            self.vx=-(random.random())/5
        else:
            self.vx=(random.random())/5

def miss(rockn):
    global health
    health = health-1
    rock.remove(rockn)


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
    if rockcount > 0:
        for rockn in rock:
            screen.blit(asteroid,(rockn.x,rockn.y))
            rockn.x+=rockn.vx
            rockn.y+=rockn.vy
            if rockn.y>height+10:
                miss(rockn)
    text=font.render(("health " + str(health)), True, (255,255,255))
    textrect=text.get_rect()
    screen.blit(text,textrect)
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

    rockcount += 0.25/speed
    if rockcount>=1:
        rock.append(rocks())
        rockcount=0
        rocknum+=1

    if health<=0:
        sys.exit()








    reset()
pygame.quit()