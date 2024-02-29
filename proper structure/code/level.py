import pygame
from settings import *
from tiles import TILE
from player import PLAYER

class LEVEL:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        #sprite Setup
        self.visible_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()
        
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    TILE((x,y), [self.visible_sprite])
                if col == 'p':
                    PLAYER((x,y), [self.visible_sprite])
                    
    def run(self):
        self.visible_sprite.draw(self.display_surface)