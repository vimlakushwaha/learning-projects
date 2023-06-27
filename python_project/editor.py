from typing import Any
import pygame, settings

class Editor:
    def __init__(self):
        self.display_surface =  pygame.display.get_surface()
    
    def run(self, dt):
        self.display_surface.fill('white')
