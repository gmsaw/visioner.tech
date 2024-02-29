import pygame
from settings import *

class PLAYER(pygame.sprite.Sprite):
    def __init__(self, pos, grups):
        super().__init__(grups)
        self.image = pygame.image.load('../graphics/main_chara/npc_1_B_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft= pos)