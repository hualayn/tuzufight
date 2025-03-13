import pygame
from random import choice
from src.background import set_bg_music, display_background
from src.display import (
    display_logo,
    display_alien_stand,
    display_score,
    display_game_start,
    show_score,
)
from src.player import Alien
from src.enemies import Snail, Bee, Bat, Snake, Enemy
from src.collision import detect_collision
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE, GAME_FONT, FONT_SIZE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('土族大战土家族')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font(GAME_FONT, FONT_SIZE)
        self.game_active = False
        self.current_time = 0
        self.game_score = 0
        self.game_timer = 0
        self.setup()
    def setup(self) -> None:
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Alien())
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Enemy(Bee()))
        self.set_animal_timer()         
        set_bg_music()
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

                if event.type == self.game_timer:
                    animal = choice((Snake, Snail, Bee, Bat))
                    self.enemies.add(Enemy(animal()))

            if self.game_active:
                display_background(self.screen)
                self.game_score = display_score(self.game_font, self.screen, self.current_time)
                self.player.draw(self.screen)
                self.player.update()
                self.enemies.draw(self.screen)
                self.enemies.update()
                self.game_active = detect_collision(self.player, self.enemies)
            else:
                self.screen.fill((35, 135, 200))
                display_logo(self.game_font, self.screen)
                display_alien_stand(self.screen)
                self.reset_game()
                if self.game_score == 0:                    
                    display_game_start(self.game_font, self.screen)
                else:
                    show_score(self.game_font, self.screen, self.game_score)
                
            pygame.display.flip()
            self.clock.tick(FRAME_RATE)

    def reset_game(self) -> None:
        self.player.empty()
        self.player.add(Alien())

    def set_animal_timer(self) -> None:
        '''设置怪物出现频率'''
        self.game_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.game_timer, 3000)  # 3秒出现一个小怪物


if __name__ == '__main__':
    game = Game()
    game.run()