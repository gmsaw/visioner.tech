import pygame
import pygame_gui
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("@gmsaw")

rect_1 = pygame.Rect(0, (3 * HEIGHT) // 4, WIDTH, HEIGHT // 4)

player = pygame.image.load('player/player_show.png').convert_alpha()
rect_2 = player.get_rect()
rect_2.bottomleft = rect_1.topleft
player_mask = pygame.mask.from_surface(player)
player_mask_image = player_mask.to_surface()

# object_grup = pygame.sprite.Group()

# object_grup.add(rect_1)

CLOCK = pygame.time.Clock()

def main():
    while True:
        CLOCK.tick(60)
        SCREEN.fill((208,228,255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
        
        pygame.draw.rect(SCREEN, (0,100,0), rect_1)
        pygame.draw.rect(SCREEN, (0,255,255), rect_2)
        
        SCREEN.blit(player, rect_2)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            rect_2.x -= 5
        if key[pygame.K_d] == True:
            rect_2.x += 5
        if key[pygame.K_w] == True:
            rect_2.y -= 5
        if key[pygame.K_s] == True:
            rect_2.y += 5
        
        pygame.display.update()

main()