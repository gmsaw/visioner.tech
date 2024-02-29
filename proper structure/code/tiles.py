import pygame
from settings import *

class TILE(pygame.sprite.Sprite):
    def __init__(self, pos, grups):
        super().__init__(grups)
        self.image = pygame.image.load('..\graphics\obstacle\\fence\\fence_4.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft= pos)