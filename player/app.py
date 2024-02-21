import pygame
from pygame.locals import *

pygame.init()

screen_width, screem_height = 500, 500

screen = pygame.display.set_mode((screen_width, screem_height))
pygame.display.set_caption("gmsaw World")

clock = pygame.time.Clock()
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

class Player ():
    def __init__(self, x, y):
        self.image_idle = []
        self.image_right = []
        self.image_left = []
        self.image_top = []
        self.image_bottom = []
        self.index = 0
        self.counter = 0
        
        for num in range(1,5):
            # IDLE
            img_idle = pygame.image.load("assets\chara\chara_0.png").convert_alpha()
            img_idle = pygame.transform.scale(img_idle, (100, 100))
            # RIGHT
            img_right = pygame.image.load(f"assets\chara\chara_R_{num}.png").convert_alpha()
            img_right = pygame.transform.scale(img_right, (100, 100))
            # LEFT
            image_left = pygame.transform.flip(img_right, True, False)
            # TOP
            img_top = pygame.image.load(f"assets\chara\chara_T_{num}.png").convert_alpha()
            img_top = pygame.transform.scale(img_top, (100, 100))
            # BOTTOM
            img_bottom = pygame.image.load(f"assets\chara\chara_B_{num}.png").convert_alpha()
            img_bottom = pygame.transform.scale(img_bottom, (100, 100))
           
            self.image_idle.append(img_idle)
            self.image_left.append(image_left)
            self.image_right.append(img_right)
            self.image_top.append(img_top)
            self.image_bottom.append(img_bottom)
            
        self.image = self.image_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 0
        self.idle_counter = 0
        self.idle_cooldown = 160
        
    def update(self):
        speed = 3
        dx = 0
        dy = 0
        walk_cooldown = 4
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= speed
            self.counter += 1
            self.direction = -1
            self.idle_counter = 0
        if key[pygame.K_d]:
            dx += speed
            self.counter += 1
            self.direction = 1
            self.idle_counter = 0
        if key[pygame.K_w]:
            dy -= speed
            self.counter += 1
            self.direction = -2
            self.idle_counter = 0
        if key[pygame.K_s]:
            dy += speed
            self.counter += 1
            self.direction = 2
            self.idle_counter = 0
        if key[pygame.K_d] == False and key[pygame.K_a] == False and key[pygame.K_w] == False and key[pygame.K_s] == False:
            self.counter = 0
            self.index = 0
            self.idle_counter += 1
            if self.idle_counter < self.idle_cooldown:
                if self.direction == 0:
                    self.image = self.image_idle[self.index]
                if self.direction == 1:
                    self.image = self.image_right[self.index]
                if self.direction == -1:
                    self.image = self.image_left[self.index]
                if self.direction == -2:
                    self.image = self.image_top[self.index]
                if self.direction == 2:
                    self.image = self.image_bottom[self.index]
            else:
                self.image = self.image_idle[self.index]
        
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index == len(self.image_right):
                self.index = 1
            if self.direction == 0:
                self.image = self.image_idle[self.index]
            if self.direction == 1:
                self.image = self.image_right[self.index]
            if self.direction == -1:
                self.image = self.image_left[self.index]
            if self.direction == -2:
                self.image = self.image_top[self.index]
            if self.direction == 2:
                self.image = self.image_bottom[self.index]
        
        self.rect.x += dx
        self.rect.y += dy
        
        screen.blit(self.image, self.rect)

player = Player(100, screem_height - (screem_height - tile_size))
world = World(world_data)
object_tile = object_tile(object_data)

run = True
while run:
    clock.tick(60)
    screen.fill((208,228,225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    world.draw()
    object_tile.draw()
    player.update()
    # draw_grid()
    pygame.display.update()

pygame.quit()