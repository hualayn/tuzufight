# Example file showing a circle moving on screen
import pygame
from random import randint

# pygame setup
pygame.init()

screen_width, screen_height = 1080, 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game_active = False
dt = 0

current_time = 0
game_score = 0

enemies_list = []
def desplay_score():
    pygame.time.get_ticks()
    score = int(pygame.time.get_ticks() / 1000) - current_time
    score_surf = game_font.render(f'得分：{score}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(midbottom=(screen_width/2, 150))
    screen.blit(score_surf, score_rect)
    return score

def display_enemies_move(enemies_list: list):
    global game_active
    if not enemies_list: return

    for enemy in enemies_list:
        enemy.x -= randint(1, 10)
        if enemy.x <= -100:
            enemies_list.remove(enemy)
        if alien_rect.colliderect(enemy):
            game_active = False
        if enemy.bottom == 615:
            screen.blit(current_snail_frame, enemy)
        else:
            screen.blit(current_bee_frame, enemy)

# 背景
background = pygame.image.load('pics/Backgrounds/backgrounds.png').convert()

game_font = pygame.font.Font('fonts/SetoFont-1.ttf', 80)
logo = game_font.render('土族大战土家族', True, (0, 0, 0))
logo_rect = logo.get_rect(midbottom=(screen_width/2, 150))

game_start = game_font.render('按下 空格 开始游戏', False, (0, 0, 0))
game_start_rect = game_start.get_rect(midbottom=(screen_width/2, 550))

game_over = game_font.render('GAME OVER', False, (0, 0, 0))
game_over_rect = game_over.get_rect(midbottom=(screen_width/2, 350))
# 外星人
alien_frame_folder = 'pics/charactors/AlienSprites/'
alien_frames = [
    pygame.image.load(f'{alien_frame_folder}alienBlue_walk{i}.png').convert_alpha() for i in [1,2]
]

alien_jump_frames = pygame.image.load('pics/charactors/AlienSprites/alienBlue_jump.png').convert_alpha()
alien_rect = alien_frames[0].get_rect()
alien_gravity = 0

# 静态外星人站立
alien_stand_frame = pygame.image.load('pics/charactors/AlienSprites/alienBlue_stand.png').convert_alpha()
alien_stand_frame_scaled = pygame.transform.rotozoom(alien_stand_frame, 0, 2)
alien_stand_frame_rect = alien_stand_frame_scaled.get_rect(midbottom=(screen_width/2, 400))


# 小蜗牛
enemy_frame_folder = 'pics/charactors/EnemySprites/'
snail_frames = [
    pygame.image.load(f'{enemy_frame_folder}snail.png').convert_alpha(),
    pygame.image.load(f'{enemy_frame_folder}snail_walk.png').convert_alpha()
]
snail_rect = snail_frames[0].get_rect(midbottom=(1080, 615))

# 小蜜蜂
bee_frames = [
    pygame.image.load(f'{enemy_frame_folder}bee.png').convert_alpha(),
    pygame.image.load(f'{enemy_frame_folder}bee_fly.png').convert_alpha()
]
bee_rect = bee_frames[0].get_rect(midbottom=(1080, 415))

# 动画参数
frame_time = 0
frame_rate = 100
frame_index = 0

# 动画位置
x = 50
y = 520
speed = 6

game_timer = pygame.USEREVENT + 1
pygame.time.set_timer(game_timer, 2000)

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:           
            if event.type == pygame.KEYDOWN and alien_rect.y == 520:
                if event.key == pygame.K_SPACE:
                    alien_gravity = -20
            if event.type == game_timer:
                if randint(0, 1):
                    enemies_list.append(snail_frames[0].get_rect(midbottom=(randint(1080, 1400), 615)))
                else:
                    enemies_list.append(bee_frames[0].get_rect(midbottom=(randint(1080, 1400), 415)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                alien_rect.x, alien_rect.y = 0, 0
                x, y = 50, 520
                alien_gravity = 0
                snail_rect.x = 1180
                bee_rect.x = 1180
                enemies_list.clear()

    if game_active:
        screen.blit(background, (0, 0))
        game_score = desplay_score()

        frame_time += clock.get_rawtime()
        
        if frame_time >= 1000 / frame_rate:
            frame_index = (frame_index + 1) % len(alien_frames)
            frame_time = 0

        # 显示当前帧
        current_snail_frame = snail_frames[frame_index]
        # screen.blit(current_snail_frame, snail_rect)
        # snail_rect.x -= randint(1, 10)
        # if snail_rect.x <= -100:
        #     snail_rect.x = 1180

        # 显示小蜜蜂
        current_bee_frame = bee_frames[frame_index]
        # screen.blit(current_bee_frame, bee_rect)
        # bee_rect.x -= randint(1,5)
        # if bee_rect.x <= -100:
        #     bee_rect.x = 1180

        current_alien_frame = alien_frames[frame_index]
        if alien_rect.y == 520:
            screen.blit(current_alien_frame, alien_rect)
        else:
            screen.blit(alien_jump_frames, alien_rect)
        alien_rect.x = x
        
        alien_gravity += 1
        alien_rect.y += alien_gravity
        if alien_rect.y >= 520:
            alien_rect.y = 520   

        if alien_rect.colliderect(snail_rect):
            game_active = False

        if alien_rect.colliderect(bee_rect):
            game_active = False

        # 获取按键状态
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     y = max(y - speed, 0)
        # if keys[pygame.K_s]:
        #     y = min(y + speed, screen_height - alien_frames[0].get_height())
        if keys[pygame.K_a]:
            x = max(x - speed, 0)
        if keys[pygame.K_d]:
            x = min(x + speed, screen_width - alien_frames[0].get_width())

        display_enemies_move(enemies_list)
    else:
        screen.fill((35, 135, 200))        
        pygame.draw.rect(screen, "pink", logo_rect)
        screen.blit(logo, logo_rect)
        screen.blit(alien_stand_frame_scaled, alien_stand_frame_rect)
        score_board = game_font.render(f'得分：{game_score}', False, (0, 0, 0))
        score_board_rect = score_board.get_rect(midbottom=(screen_width/2, 550))
        if game_score == 0:
            screen.blit(game_start, game_start_rect)
        else:
            screen.blit(score_board, score_board_rect)
        current_time = int(pygame.time.get_ticks() / 1000)

    pygame.display.flip()
    dt = clock.tick(60)
