import pygame
from random import choice
from src.background import set_bg_music, display_background
from src.display import (
    display_logo,
    display_alien_stand,
    display_game_over,
    display_score,
    display_game_start,
    show_score,
)
from src.player import Alien
from src.enemies import Snail, Bee, Enemy
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
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Alien())
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Enemy(Bee()))
        self.set_animal_timer()      
        self.setup()  

    def setup(self) -> None:
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

                if event.type == pygame.USEREVENT + 1:
                    animal = choice((Snail, Snail, Bee))
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
                if self.game_score == 0:                    
                    display_game_start(self.game_font, self.screen)
                else:
                    show_score(self.game_font, self.screen, self.game_score)
                
            pygame.display.flip()
            self.clock.tick(FRAME_RATE)

    def set_animal_timer(self) -> None:
        '''设置怪物出现频率'''
        game_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(game_timer, 5000)  # 2秒出现一个小怪物


if __name__ == '__main__':
    game = Game()
    game.run()