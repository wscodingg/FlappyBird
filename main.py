import sys
import pygame


screen_height = 512
screen_width = 288
screen_color = (255, 255, 255)
circle_color = (230, 0, 0)

center_x = screen_width / 2
center_y = screen_height / 2
radius = 25

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")
bg_day = pygame.image.load("assets/background-day.png")
bird_midflap = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_downflap = pygame.image.load("assets/bluebird-downflap.png").convert()
bird_upflap = pygame.image.load("assets/bluebird-upflap.png").convert()


clock = pygame.time.Clock()

isPlaying = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
            pygame.quit()
            sys.exit()
    
    
    screen.blit(bg_day, (0, 0))  
    screen.blit(bird_upflap, (center_x, center_y))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        center_y -= 5 
        screen.blit(bird_midflap, (center_x, center_y))
        screen.blit(bird_downflap, (center_x, center_y))
    if keys[pygame.K_s]:
        center_y += 5
    if keys[pygame.K_a]: center_x -= 5
    if keys[pygame.K_d]: center_x += 5
    
    
    
    clock.tick(60)
    # pygame.draw.circle(screen, circle_color, (center_x, center_y), radius)
    pygame.display.update()


    