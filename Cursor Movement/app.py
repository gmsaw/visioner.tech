import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Follow @gmsaw_")

icon = pygame.image.load('./spaceship.png')
pygame.display.set_icon(icon)
player_img = pygame.transform.scale(icon, (50, 50))

player_width, player_height = player_img.get_rect().size
playerX = (screen_width - player_width) // 2
playerY = (screen_height - player_height) // 2

def player(x, y):
    screen.blit(player_img, (x, y))

pygame.mouse.set_visible(False)

# FOLLOW @visioner.tech FOR MORE CONTENT
# FOLLOW @gmsaw_ FOR MORE GITHUB CODE

print("FOLLOW @visioner.tech FOR MORE CONTENT")
print("FOLLOW @gmsaw_ FOR MORE GITHUB CODE")

running = True
while running:
    screen.fill((0, 0, 0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    player(mouse_x - player_width / 2, mouse_y - player_height / 2) 
    pygame.display.update() 

pygame.quit()
