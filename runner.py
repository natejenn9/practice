
import pygame

import random

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
WIDTH = 450
HIGHT = 300

#game var
score = 0
player_x = 50
player_y = 0
y_change = 0
gravity = 1
x_change = 0
obs = [300, 450, 600]
obs_speed = 2
active = False
c = [200, 350]


screen = pygame.display.set_mode([WIDTH, HIGHT])
pygame.display.set_caption("runner")
bg = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()


running = True
while running:
    timer.tick(fps)
    screen.fill(bg)
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, HIGHT])
    score_text = font.render(f'Score: {score}', True, black, white)
    screen.blit(score_text, (160,250))
    player = pygame.draw.rect(screen, green, [player_x, player_y, 20, 20])
    obs_0 = pygame.draw.rect(screen, red, [obs[0],200, 20, 20])
    obs_1 = pygame.draw.rect(screen, red, [obs[1],200, 20, 20])
    obs_2 = pygame.draw.rect(screen, red, [obs[2],200, 20, 20])
    coin_1 = pygame.draw.rect(screen, yellow, [c[0], 75, 15, 15])
    coin_2 = pygame.draw.rect(screen, yellow, [c[1], 75, 15, 15])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obs = [300, 450, 600]
                player_x = 50
                score = 0
                active = True
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            if event.key == pygame.K_RIGHT:
                x_change = 2
            if event.key == pygame.K_LEFT:
                x_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0
    for i in range(len(obs)):
        if active: 
            obs[i] -= obs_speed
            if obs[i] < -20:
                obs[i] = random.randint(470,570)
                score += 1
            if player.colliderect(obs_0) or player.colliderect(obs_1) or player.colliderect(obs_2):
                active = False
    for i in range(len(c)):
        if active:
            c[i] -= obs_speed
            if c[i] < -15:
                c[i] = random.randint(500,1000)
            if player.colliderect(coin_1) or player.colliderect(coin_2):
                score += 1
                break            
    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x >430: 
        player_x = 430

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity 
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()
pygame.quit()

