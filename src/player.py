import pygame
from .settings import SCREEN_WIDTH

class Alien(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        alien_frame_folder = 'pics/charactors/AlienSprites/'
        self.walk = [
            pygame.image.load(f'{alien_frame_folder}alienBlue_walk{i}.png').convert_alpha() for i in [1,2]
        ]
        self.index = 0
        self.image = self.walk[self.index]
        self.jump = pygame.image.load('pics/charactors/AlienSprites/alienBlue_jump.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200, 615))
        self.gravity = 0
        self.speed = 10

    def player_input(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.y == 520:
            self.gravity = -20
        if keys[pygame.K_a]:
            self.rect.x = max(0, self.rect.x - self.speed)
        if keys[pygame.K_d]:
            self.rect.x = min(SCREEN_WIDTH - 100, self.rect.x + self.speed)

    def apply_gravity(self) -> None:
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= 520:
            self.rect.y = 520

    def animation_state(self) -> None:
        if self.rect.y == 520:
            self.index += 0.1
            if self.index >= len(self.walk):
                self.index = 0
            self.image = self.walk[int(self.index)]
        else:
            self.image = self.jump

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()