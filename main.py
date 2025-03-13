import pygame
import pygame.midi
from random import choice
from src.player import Alien
from src.enemies import Snail, Bee, Enemy
from src.collision import detect_collision
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE, GAME_FONT, FONT_SIZE, BG_MUSIC


class Game:
    def __init__(self):
        pygame.init()
        pygame.midi.init()
        pygame.display.set_caption('土族大战土家族')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font(GAME_FONT, FONT_SIZE)
        self.game_active = False
        self.current_time = 0
        self.game_score = 0
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Alien())
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Enemy(Bee()))
        self.set_animal_timer()
        self.set_bg_music()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if not self.game_active:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.game_active = True
                        self.current_time = int(pygame.time.get_ticks() / 1000)

                if event.type == pygame.USEREVENT + 1:
                    animal = choice((Snail, Snail, Bee))
                    self.enemies.add(Enemy(animal()))

            if self.game_active:
                self.display_background()
                self.display_score()
                self.player.draw(self.screen)
                self.player.update()
                self.enemies.draw(self.screen)
                self.enemies.update()
                self.game_active = detect_collision(self.player, self.enemies)
            else:
                self.screen.fill((35, 135, 200))
                self.display_logo()
                self.display_alien_stand()
                if self.game_score == 0:                    
                    self.display_game_start()
                else:
                    self.display_game_over()
                
            pygame.display.flip()
            self.clock.tick(FRAME_RATE)

    def set_bg_music(self) -> None:
        '''背景音乐'''
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.5)
    def set_animal_timer(self) -> None:
        '''设置怪物出现频率'''
        game_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(game_timer, 5000)  # 2秒出现一个小怪物

    def display_background(self) -> None:
        '''背景'''
        background = pygame.image.load('pics/Backgrounds/backgrounds.png').convert()
        self.screen.blit(background, (0, 0))

    def display_logo(self) -> None:
        '''游戏标题'''
        logo = self.game_font.render('土族大战土家族', True, (0, 0, 0))
        logo_rect = logo.get_rect(midbottom=(SCREEN_WIDTH/2, 150))
        self.screen.blit(logo, logo_rect)
    def display_score(self) -> int:
        '''游戏分数'''
        pygame.time.get_ticks()
        score = int(pygame.time.get_ticks() / 1000) - self.current_time
        score_surf = self.game_font.render(f'得分：{score}', False, (0, 0, 0))
        score_rect = score_surf.get_rect(midbottom=(SCREEN_WIDTH/2, 150))
        self.screen.blit(score_surf, score_rect)
        return score
    
    def display_game_start(self) -> None:
        '''游戏开始'''
        game_start = self.game_font.render('按下 空格 开始游戏', False, (0, 0, 0))
        game_start_rect = game_start.get_rect(midbottom=(SCREEN_WIDTH/2, 550))
        self.screen.blit(game_start, game_start_rect)

    def display_alien_stand(self) -> None:
        '''游戏开始或失败时，玩家站立的姿态'''
        alien_stand = pygame.transform.rotozoom(pygame.image.load('pics/charactors/AlienSprites/alienBlue_stand.png').convert_alpha(), 0, 2)
        alien_stand_rect = alien_stand.get_rect(midbottom=(SCREEN_WIDTH/2, 400))
        self.screen.blit(alien_stand, alien_stand_rect)

    def display_game_over(self) -> None:
        '''游戏结束'''
        game_over = self.game_font.render('GAME OVER', False, (0, 0, 0))
        game_over_rect = game_over.get_rect(midbottom=(SCREEN_WIDTH/2, 350))
        self.screen.blit(game_over, game_over_rect)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#         if not game_active:
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                 game_active = True            

#     if game_active:
#         screen.blit(background, (0, 0))
#         game_score = desplay_score()        

#         player.draw(screen)
#         player.update()
#         enemies.draw(screen)
#         enemies.update()
#     else:
#         screen.fill((35, 135, 200))        
#         pygame.draw.rect(screen, "pink", logo_rect)
#         screen.blit(logo, logo_rect)
#         score_board = game_font.render(f'得分：{game_score}', False, (0, 0, 0))
#         score_board_rect = score_board.get_rect(midbottom=(SCREEN_WIDTH/2, 550))
#         if game_score == 0:
#             screen.blit(game_start, game_start_rect)
#         else:
#             screen.blit(score_board, score_board_rect)
#         current_time = int(pygame.time.get_ticks() / 1000)

#     pygame.display.flip()
#     dt = clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()