import pygame

pygame.init()

surface = pygame.display.set_mode((1000,500))
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
        else:
            pass
    