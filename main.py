# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

alien_frame_folder = 'src/charactors/AlienSprites/'
frames = [
    pygame.image.load(f'{alien_frame_folder}alienBlue_walk{i}.png') for i in [1,2]
]
# 动画参数
frame_time = 0
frame_rate = 100
frame_index = 0

# 动画位置
x = frames[0].get_width() // 2
y = screen_height // 1.5 - frames[0].get_height() // 2
speed = 6

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    frame_time += clock.get_rawtime()
    clock.tick()
    if frame_time >= 1000 / frame_rate:
        frame_index = (frame_index + 1) % len(frames)
        frame_time = 0

    # 显示当前帧
    current_frame = frames[frame_index]
    screen.blit(current_frame, (x, y))


    keys = pygame.key.get_pressed()

     # 获取按键状态
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y = max(y - speed, 0)
    if keys[pygame.K_s]:
        y = min(y + speed, screen_height - frames[0].get_height())
    if keys[pygame.K_a]:
        x = max(x - speed, 0)
    if keys[pygame.K_d]:
        x = min(x + speed, screen_width - frames[0].get_width())
    if keys[pygame.K_SPACE]:
        print('space')

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()