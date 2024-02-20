import pygame
from pygame.locals import *

pygame.init()

screen_width, screem_height = 500, 500

screen = pygame.display.set_mode((screen_width, screem_height))
pygame.display.set_caption("gmsaw World")

tile_size = 25

def draw_grid():
    for line in range(0,20):
        pygame.draw.line(screen, (255,255,255), (0, line*tile_size), (screen_width, line*tile_size))
        pygame.draw.line(screen, (255,255,255), (line*tile_size, 0), (line*tile_size, screem_height))

class World():
    def __init__(self, data):
        self.tile_list = []
        
        grass1_img = pygame.image.load('assets\grass\grass_1.png').convert_alpha()
        grass2_img = pygame.image.load('assets\grass\grass_2.png').convert_alpha()
        grass3_img = pygame.image.load('assets\grass\grass_3.png').convert_alpha()
        grass4_img = pygame.image.load('assets\grass\grass_4.png').convert_alpha()
        grass5_img = pygame.image.load('assets\grass\grass_5.png').convert_alpha()
        grass6_img = pygame.image.load('assets\grass\grass_6.png').convert_alpha()
        grass7_img = pygame.image.load('assets\grass\grass_7.png').convert_alpha()
        grass8_img = pygame.image.load('assets\grass\grass_8.png').convert_alpha()
        grass9_img = pygame.image.load('assets\grass\grass_9.png').convert_alpha()
        grass10_img = pygame.image.load('assets\grass\grass_10.png').convert_alpha()
        grass11_img = pygame.image.load('assets\grass\grass_11.png').convert_alpha()
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(grass1_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass2_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(grass3_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(grass4_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(grass5_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(grass6_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(grass7_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(grass8_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 9:
                    img = pygame.transform.scale(grass9_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 10:
                    img = pygame.transform.scale(grass10_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 11:
                    img = pygame.transform.scale(grass11_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            
world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,11,2,2,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,2,1,1,1,11,11,1,1,1,1,1,1,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,11,1,1,1,1,1,2,1,8,0],
    [0,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,0],
    [0,4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,6,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

class object_tile():
    def __init__(self, data):
        self.object_tile_list = []
       
        fence1_img = pygame.image.load('assets\\fence\\fence_1.png').convert_alpha() 
        fence2_img = pygame.image.load('assets\\fence\\fence_2.png').convert_alpha() 
        fence3_img = pygame.image.load('assets\\fence\\fence_3.png').convert_alpha() 
        fence4_img = pygame.image.load('assets\\fence\\fence_4.png').convert_alpha() 
        fence5_img = pygame.image.load('assets\\fence\\fence_5.png').convert_alpha() 
        fence6_img = pygame.image.load('assets\\fence\\fence_6.png').convert_alpha() 
       
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(fence1_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.object_tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(fence2_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.object_tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(fence3_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.object_tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(fence4_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.object_tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(fence5_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.object_tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(fence6_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.object_tile_list.append(tile)
                col_count += 1
            row_count += 1
            
    def draw(self):
        for tile in self.object_tile_list:
            screen.blit(tile[0], tile[1])

object_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,6,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,5,5,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,4,0,0,4,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world = World(world_data)
object_tile = object_tile(object_data)

run = True
while run:
    screen.fill((208,228,225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    world.draw()
    object_tile.draw()
    # draw_grid()
    pygame.display.update()

pygame.quit()