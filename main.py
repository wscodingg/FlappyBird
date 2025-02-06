import sys
import pygame
import math
from pygame import mixer

screen_height = 600
screen_width = 350
screen_color = (255, 255, 255)
circle_color = (230, 0, 0)

center_x = screen_width / 2
center_y = screen_height / 2
radius = 25

pygame.init()
mixer.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")
bg_day = pygame.image.load("assets/background-day.png")
bg_day_width = bg_day.get_width()
tiles_bg = math.ceil(screen_width / bg_day_width)
scroll = 0;


bird_midflap = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_downflap = pygame.image.load("assets/bluebird-downflap.png").convert()
bird_upflap = pygame.image.load("assets/bluebird-upflap.png").convert()

base = pygame.image.load("assets/base.png")
base_width = base.get_width()
tiles_base = math.ceil(screen_width / base_width)

wings = mixer.music.load("sound/sfx_wing.wav")
mixer.music.set_volume(0.2)

clock = pygame.time.Clock()

isPlaying = True
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
            pygame.quit()
            sys.exit()
    
    for i in range(0, tiles_bg):
        screen.blit(bg_day, (i * bg_day_width + scroll, 0))  
        
    for i in range (0, tiles_base):
        screen.blit(base, (i * base_width + scroll, 500))
    screen.blit(bird_upflap, (center_x, center_y))
    scroll -= 3.8
    
    if abs(scroll) > bg_day_width:
        scroll = 0
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        center_y -= 5 
        screen.blit(bird_downflap, (center_x, center_y))
        mixer.music.play()
    if keys[pygame.K_s]:
        center_y += 5
        screen.blit(bird_midflap, (center_x, center_y))
    if keys[pygame.K_a]: center_x -= 5
    if keys[pygame.K_d]: center_x += 5
    
    
    
    
    
    # pygame.draw.circle(screen, circle_color, (center_x, center_y), radius)
    pygame.display.update()


    