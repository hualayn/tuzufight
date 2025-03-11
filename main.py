# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

screen_width, screen_height = 1152, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

# 背景
background = pygame.image.load('pics/Backgrounds/backgrounds.png').convert()

game_logo = pygame.font.Font('fonts/SetoFont-1.ttf', 50)
logo = game_logo.render('土族大战土家族', True, (0, 0, 0))

# 外星人
alien_frame_folder = 'pics/charactors/AlienSprites/'
alien_frames = [
    pygame.image.load(f'{alien_frame_folder}alienBlue_walk{i}.png').convert_alpha() for i in [1,2]
]
alien_rect = alien_frames[0].get_rect(midbottom=(screen_width // 2, screen_height // 2))

# 小蜗牛
enemy_frame_folder = 'pics/charactors/EnemySprites/'
snail_frames = [
    pygame.image.load(f'{enemy_frame_folder}snail.png').convert_alpha(),
    pygame.image.load(f'{enemy_frame_folder}snail_walk.png').convert_alpha()
]
snail_rect = snail_frames[0].get_rect(midbottom=(800, screen_height // 2))

# 动画参数
frame_time = 0
frame_rate = 100
frame_index = 0

# 动画位置
x = alien_frames[0].get_width() // 2
y = screen_height // 1.5 - alien_frames[0].get_height() // 2
speed = 6

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(logo, (screen_width // 2 - logo.get_width() // 2, 50))

    frame_time += clock.get_rawtime()
    clock.tick()
    if frame_time >= 1000 / frame_rate:
        frame_index = (frame_index + 1) % len(alien_frames)
        frame_time = 0

    # 显示当前帧
    current_alien_frame = alien_frames[frame_index]
    current_snail_frame = snail_frames[frame_index]
    screen.blit(current_alien_frame, alien_rect)
    screen.blit(current_snail_frame, snail_rect)

    snail_rect.left -= 2

    alien_rect.left, alien_rect.top = x, y
    keys = pygame.key.get_pressed()

     # 获取按键状态
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y = max(y - speed, 0)
    if keys[pygame.K_s]:
        y = min(y + speed, screen_height - alien_frames[0].get_height())
    if keys[pygame.K_a]:
        x = max(x - speed, 0)
    if keys[pygame.K_d]:
        x = min(x + speed, screen_width - alien_frames[0].get_width())
    if keys[pygame.K_SPACE]:
        print('space')

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)

pygame.quit()