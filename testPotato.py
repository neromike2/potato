import sys, pygame
pygame.init()
speed=20
agility=2
size = width, height = 800, 750
charpos=[width/2,height-50]

screen = pygame.display.set_mode(size)
GameClock = pygame.time.Clock()
backgroundcolor= 0,0,0
rectcolor= 200,0,0
rectpos=[100,100,100,100]
def reset():
    screen.fill(backgroundcolor)
    pygame.draw.rect(screen, rectcolor,rectpos,0)
while 1:
    GameClock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    reset()
   # screen.blit(char, charpos)
    pygame.display.flip()
    keypressed= pygame.key.get_pressed()
    if keypressed==K_LEFT:
        charpos(0)=charpos(0)-agility





pygame.quit()