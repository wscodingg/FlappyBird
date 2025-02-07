import sys
import pygame
import math
from pygame import mixer

#canvas dimensions
screen_height = 600
screen_width = 350
screen_color = (255, 255, 255)
circle_color = (230, 0, 0)

#bird center
center_x = screen_width / 2
center_y = screen_height / 2
radius = 25

#init's
pygame.init()
mixer.init()

#canvas declaration
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

#background rect
bg_day = pygame.image.load("assets/background-day.png")
bg_day_width = bg_day.get_width()
tiles_bg = math.ceil(screen_width / bg_day_width)
scroll = 0;

#birds rect
bird_midflap = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_downflap = pygame.image.load("assets/bluebird-downflap.png").convert()
bird_upflap = pygame.image.load("assets/bluebird-upflap.png").convert()


bird_rect = bird_upflap.get_rect(center=(100, 300))

#base rects
base = pygame.image.load("assets/base.png")
base_width = base.get_width()
tiles_base = math.ceil(screen_width / base_width)

#wings sfx
wings = mixer.music.load("sound/sfx_wing.wav")
mixer.music.set_volume(0.2)


#gravity
gravity = 0.25
bird_movement = 0

clock = pygame.time.Clock()

#game loop
isPlaying = True
while True:
    clock.tick(60)
    #checking the close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
            pygame.quit()
            sys.exit()
    
    #loading the scrolling background 
    for i in range(0, tiles_bg+1):
        screen.blit(bg_day, (i * bg_day_width + scroll, 0))  
        
    for i in range (0, tiles_base+1):
        screen.blit(base, (i * base_width + scroll, 500))
    
    
    scroll -= 3.8
    bird_movement += gravity
    bird_rect.centery += bird_movement
    
    screen.blit(bird_upflap, bird_rect)
    if abs(scroll) > bg_day_width:
        scroll = 0
    
    
    #keys operations
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        screen.blit(bird_downflap, bird_rect)
        mixer.music.play()
        bird_movement = 0
        bird_movement -= 8
        
    
    
    
    pygame.display.update()


    