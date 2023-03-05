import pygame
import time

pygame.init()
screen = pygame.display.set_mode([500, 500])
x = 125
y = 200
xt = 325
yt = 200
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 0, 255), (x,y,50,50), False)
    pygame.draw.rect(screen, (255, 0, 0), (xt, yt, 50, 50), False)
    pygame.display.update()
    move_ticker = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x = x + 2.5
    if keys[pygame.K_a]:
        x = x + -2.5
    if keys[pygame.K_w]:
        y = y + -2.5
    if keys[pygame.K_s]:
        y = y + 2.5
    if x > 450:
        x = 0
    elif x < 0:
        x = 450
    elif y > 450:
        y = 0
    elif y < 0:
        y = 450
    if keys[pygame.K_RIGHT]:
        xt = xt + 2.5
    if keys[pygame.K_LEFT]:
        xt = xt + -2.5
    if keys[pygame.K_UP]:
        yt = yt + -2.5
    if keys[pygame.K_DOWN]:
        yt = yt + 2.5
    if xt > 450:
        xt = 0
    elif xt < 0:
        xt = 450
    elif yt > 450:
        yt = 0
    elif yt < 0:
        yt = 450
    time.sleep(0.01)