import sys
import pygame
import math
import random
from pygame import mixer

# canvas dimensions
screen_height = 600
screen_width = 350
screen_color = (255, 255, 255)
circle_color = (230, 0, 0)

# bird center
center_x = screen_width / 2
center_y = screen_height / 2
radius = 25

# init's
pygame.init()
mixer.init()


# pipe functions
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(450, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(450, random_pipe_pos - 200))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


# canvas declaration
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
pygame.display.set_caption("Flappy Bird")


# background rect
bg_day = pygame.image.load("assets/background-day.png")
bg_day_width = bg_day.get_width()
tiles_bg = math.ceil(screen_width / bg_day_width)
scroll = 0

# birds rect
bird_midflap = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_downflap = pygame.image.load("assets/bluebird-downflap.png").convert()
bird_upflap = pygame.image.load("assets/bluebird-upflap.png").convert()
bird_rect_up = bird_upflap.get_rect(center=(150, 300))
bird_rect_down = bird_downflap.get_rect()

# pipe rect
pipe_surface = pygame.image.load("assets/pipe-green.png")
pipe_surface = pygame.transform.scale(pipe_surface, (70, 320))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 400]


# base rects
base = pygame.image.load("assets/base.png")
base_width = base.get_width()
tiles_base = math.ceil(screen_width / base_width)

# wings sfx

mixer.music.set_volume(0.2)


# gravity
gravity = 0.25
bird_movement = 0


score = 0


clock = pygame.time.Clock()

# game over
game_over = pygame.image.load("assets/message.png").convert_alpha()
game_over_rect = game_over.get_rect(center=(175, 300))

mf_score = True

#collision sound
count = 0


previous_score = 0
# game loop
isPlaying = True
anotherScreen = False
while True:
    clock.tick(60)
    # checking the close event
    if isPlaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isPlaying = False
                pygame.quit()
                sys.exit()
            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())

        # loading the scrolling background
        for i in range(0, tiles_bg + 1):
            screen.blit(bg_day, (i * bg_day_width + scroll, 0))

        draw_pipes(pipe_list)

        for i in range(0, tiles_base + 1):
            screen.blit(base, (i * base_width + scroll, 500))

        scroll -= 3.8
        screen.blit(bird_upflap, bird_rect_up)
        bird_rect_up.clamp_ip(screen_rect)
        if abs(scroll) > bg_day_width:
            scroll = 0

    # gravity
    bird_movement += gravity
    bird_rect_up.centery += bird_movement

    # pipes
    pipe_list = move_pipes(pipe_list)

    collided = False
    for pipe in pipe_list:
        if bird_rect_up.colliderect(pipe):
            mixer.music.load("sound/sfx_die.wav")
            mixer.music.play()
            count += 1
            collided = True

    if isPlaying and collided:
        count += 1
        isPlaying = False
        anotherScreen = True

    # score
    if mf_score:
        score += 0.01
        current_score = int(score)
        game_font = pygame.font.Font(("04B_19.TTF"), 20)
        score_surface = game_font.render(
            f"score: {str(int(score))}", True, (255, 255, 255)
        )
        score_rect = score_surface.get_rect(center=(175, 40))
        screen.blit(score_surface, score_rect)

    if current_score > previous_score:
        mixer.music.load("sound/sfx_point.wav")
        mixer.music.play()
    previous_score = current_score

    events = pygame.event.get()

    # Check collision and handle death
    if isPlaying and (bird_rect_up.centery >= 600 or bird_rect_up.centery <= 10):
        mixer.music.load("sound/sfx_die.wav")
        mixer.music.play()
        isPlaying = False
        anotherScreen = True

    if anotherScreen:
        gravity = 0.25
        bird_movement = 0
        scroll = 0
        mf_score = False
        # Process window close event
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if keys[pygame.K_SPACE]:
                mf_score = True
                anotherScreen = False
                isPlaying = True
                score = 0

        # Draw game over screen
        game_over_rect.center = screen.get_rect().center
        screen.blit(game_over, game_over_rect)

    # keys operations
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        screen.blit(bird_downflap, bird_rect_up)
        bird_movement = 0
        bird_movement -= 8

    pygame.display.update()
