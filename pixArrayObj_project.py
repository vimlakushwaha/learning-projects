####import pygame
####
####pygame.init()
####
####white = (255,255,255)
####black = (0,0,0)
####
####red = (255,0,0)
####green = (0,255,0)
####blue = (0,0,255)
####
####gameDisplay = pygame.display.set_mode((800,600))
####gameDisplay.fill(black)
####
####
####pixAr = pygame.PixelArray(gameDisplay)
####pixAr[10][20] = red
####pixAr[10][50] = blue
####pixAr[78][26] = red
####pixAr[10][299] = red
####
####while True:
####    for event in pygame.event.get():
####        if event.type == pygame.QUIT:
####            pygame.quit()
####            quit()
####
####    pygame.display.update()
####
####
##
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 #Frames per second
fpsClock = pygame.time.Clock()

#set up the windows

display_surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Animation")

white = (255, 255, 255)
black= (0,0,0)
catImg = pygame.image.load("cat.png")
catgif = pygame.image.load("cat.gif")
catx = 0
caty = 0
direction = 'right'

while True:
    display_surface.fill(white)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty +=5
        if caty == 220:
            direction ='left'
    elif direction == 'left':
        catx -=5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -=5
        if caty == 10:
            direction = 'right'


    display_surface.blit(catImg,(catx,caty))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

##
##
##
##


##
##
##
##import pygame, sys
##from pygame.locals import *
##
##pygame.init()
##
##FPS = 30 # frames per second setting
##fpsClock = pygame.time.Clock()
##
### set up the window
##DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
##pygame.display.set_caption('Animation')
##
##WHITE = (255, 255, 255)
##catImg = pygame.image.load('cat.png')
##catx = 10
##caty = 10
##direction = 'right'
##
##while True: # the main game loop
##    DISPLAYSURF.fill(WHITE)
##
##    if direction == 'right':
##        catx += 5
##        if catx == 280:
##            direction = 'down'
##    elif direction == 'down':
##        caty += 5
##        if caty == 220:
##            direction = 'left'
##    elif direction == 'left':
##        catx -= 5
##        if catx == 10:
##            direction = 'up'
##    elif direction == 'up':
##        caty -= 5
##        if caty == 10:
##            direction = 'right'
##
##    DISPLAYSURF.blit(catImg, (catx, caty))
##
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            sys.exit()
##
##    pygame.display.update()
##    fpsClock.tick(FPS)
