import sys, pygame
import random
import pygame.font
from pygame import rect
score=0
power=0
rockspawnspeed=0.25
rocksize=80
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
speed=40
agility=5
size = width, height = 800, 750
charpos=[width/2,height-50]
bg = pygame.image.load("background.jpg")
screen = pygame.display.set_mode(size)
GameClock = pygame.time.Clock()
pygame.display.set_caption('space shooter')
font = pygame.font.SysFont(None, 24)
textcolor=255,255,255
yellow=255, 236, 11

class rocks:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vy=random.randrange(1,7)
        self.img=pygame.image.load("Asteroid2.png")
        self.img= pygame.transform.scale(self.img, (rocksize, rocksize))
        self.rect= self.img.get_rect(topleft=(random.randrange(25,(width-25)),-75))

        if self.rect.x > width/2:
            self.vx=-(random.random())/3
        else:
            self.vx=(random.random())/3


def miss(rockn):
    global health
    health = health-1
    rock.remove(rockn)


class bullets:
    def __init__(self,x,y,img):
        self.img=pygame.image.load("potato.png")
        self.img=pygame.transform.scale(self.img,(potatosize,potatosize))
        self.active=False
        self.rect= self.img.get_rect(topleft=(x,y))



for bulletn in range(maxbullets):
    bullet.append(bullets(0,0,potato))

def collide(obj1, obj2):
    global score
    return (pygame.sprite.collide_rect(obj1,obj2))

def reset():
    global bulletcount
    screen.blit(bg, (0, 0))
    if bulletcount > 0:
        for bulletn in range(maxbullets):
            if bullet[bulletn].active:
                screen.blit(bullet[bulletn].img, (bullet[bulletn].rect.x,bullet[bulletn].rect.y))
                if bullet[bulletn].rect.y<-50:
                    bullet[bulletn].active=False
                    bulletcount-=1
    screen.blit(ship,charpos)
    if rockcount > 0:
        for rockn in rock:
            screen.blit(asteroid,(rockn.rect.x,rockn.rect.y))
            rockn.rect.x+=rockn.vx
            rockn.rect.y+=rockn.vy
            if rockn.rect.y>height+10:
                miss(rockn)
    screen.blit(font.render(("Health " + str(health)),True, textcolor),(0,0))
    screen.blit(font.render('Player Score: ' + str(score), True, textcolor), (0, 20))
    pygame.draw.rect(screen,yellow,(width-50,(height/2)-power/2,50,power))

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
        freebullet=-1
        for bulletn in range(maxbullets):

            if not bullet[bulletn].active:
                freebullet=bulletn
        if freebullet>-1:
            bulletcount+=1
            bullet[freebullet].active=True
            bullet[freebullet].rect.x = charpos[0]
            bullet[freebullet].rect.y = charpos[1]
            cooldown+=speed
    if bulletcount > 0:
        for bulletn in range(maxbullets):
            if bullet[bulletn].active:
                bullet[bulletn].rect.y -= bulletspeed
                for rockn in rock:
                    if collide(rockn,bullet[bulletn]):
                        bullet[bulletn].active=False
                        bulletcount-=1
                        score += 1
                        health+=1
                        miss(rockn)

    if cooldown >0:
        cooldown-=1
    if power<=200:
        power+=0.1
    if keypressed[pygame.K_c] and power>=200:
        power=0
        health+=1



    rockcount += rockspawnspeed/speed
    if rockcount>=1:
        rock.append(rocks())
        rockcount=0
        rocknum+=1
        rockspawnspeed+=0.015

    if health<=0:
        a=200
        while a>0:
            font = pygame.font.SysFont(None, 40)
            screen.blit(font.render('You lost but remember to not litter,', True, textcolor), (100, height/2))
            screen.blit(font.render('save money, and eat healthy', True, textcolor),(100,height/2+23))
        #enviorment, finance and health
            GameClock.tick(40)
            a-=1
            pygame.display.flip()
        sys.exit()


    reset()
pygame.quit()