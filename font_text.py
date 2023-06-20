import pygame, sys
from pygame.locals import*

pygame.init()
window = pygame.display.set_mode((900,300))

pygame.display.set_caption('Hello World!')



white = (255,255,255)
green = (122,120,90)
blue = (0,0,255)

font_object = pygame.font.Font('freesansbold.ttf',32)
text_surface_object = font_object.render("Hey how's going your day?",True ,green,blue)
text_rect_obj = text_surface_object.get_rect()
text_rect_obj.center = (220,150)

while True:
    window.fill(white)
    window.blit(text_surface_object,text_rect_obj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()
    pygame.display.update()
