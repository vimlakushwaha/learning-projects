##Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
import pygame
from pygame.locals import *
pygame.init()
#setup the window
DisplaySurf = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("drawing")

#set up colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


#draw the surface object
DisplaySurf.fill(white)
pygame.draw.polygon(DisplaySurf,green,((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.line(DisplaySurf,blue,(60,60),(120,60),4)
pygame.draw.line(DisplaySurf,blue,(120,60),(60,120))
pygame.draw.line(DisplaySurf,blue,(60,120),(120,120),4)
pygame.draw.circle(DisplaySurf,blue,(300,50),20,0)
pygame.draw.ellipse(DisplaySurf,red,(300,250,40,80),1)
pygame.draw.rect(DisplaySurf,red,(200,150,100,50))

pixObj = pygame.PixelArray(DisplaySurf)
pixObj[200][120] = black
pixObj[201][120] = black
pixObj[202][120] = black
pixObj[203][120] = black
pixObj[204][120] = black
pixObj[305][120] = black
pixObj[306][120] = black
pixObj[487][120] = black
pixObj[488][120] = black
pixObj[489][120] = black
pixObj[490][120] = black
pixObj[491][120] = black
pixObj[492][120] = black
pixObj[493][120] = black
pixObj[494][120] = black


del pixObj
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
