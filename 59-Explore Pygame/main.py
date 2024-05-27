import pygame

# Init
pygame.init()
# Variable running game
running = True
# membuat display surface object
screen_X = 640
screen_Y = 480
screen = pygame.display.set_mode((screen_X,screen_Y))
# Limit fPS
clock = pygame.time.Clock()

# object game
# koordinat posisi
x = 295
y = 210
# ukuran
panjang = 30
lebar = 25
# kecpatan gerak
speed = 10

while running:
    # User input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # action keyboard press
    keys = pygame.key.get_pressed()
    # kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < (screen_X-lebar):
        x += speed
    if keys[pygame.K_DOWN] and y < (screen_Y-panjang):
        y += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # update asset
    screen.fill("white")
    pygame.draw.rect(screen,"cyan",(x,y,lebar,panjang))
    # render display
    pygame.display.flip()
    # Limit FPS
    clock.tick(60)

pygame.quit()

