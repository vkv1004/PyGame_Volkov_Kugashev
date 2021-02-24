import pygame

pygame.init()
size = (500, 500)
win = pygame.display.set_mode(size)

pygame.display.set_caption("Bomberman")

x = 50
y = 50
width = 40
height = 60
speed = 50

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - width:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < 500 - width:
        x += speed
    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < 500 - width:
        y += speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()