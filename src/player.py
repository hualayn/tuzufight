import pygame
from src.bullets import Bullet
from .settings import SCREEN_WIDTH
from typing import List


class Alien(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        alien_frame_folder = 'pics/charactors/AlienSprites/'
        self.walk_frames = [
            pygame.image.load(f'{alien_frame_folder}alienBlue_walk{i}.png').convert_alpha() for i in [1,2]
        ]        
        self.jump_frame = pygame.image.load('pics/charactors/AlienSprites/alienBlue_jump.png').convert_alpha()
        self.stand_frame = pygame.image.load('pics/charactors/AlienSprites/alienBlue_stand.png').convert_alpha()
        self.index = 0
        self.image = self.walk_frames[self.index]
        self.rect = self.image.get_rect(midbottom=(200, 615))
        self.gravity = 0
        self.speed = 10
        self.bullets: List[Bullet] = []

    def walk(self) -> None:
        self.index += 0.1
        if self.index >= len(self.walk_frames):
            self.index = 0
        self.image = self.walk_frames[int(self.index)]

    def stand(self) -> None:
        self.image = self.stand_frame

    def jump(self) -> None:
        self.image = self.jump_frame

    def shoot(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        director = pygame.math.Vector2(mouse_x - self.rect.x, mouse_y - self.rect.y)
        bullet = Bullet(self.rect.midtop, director)
        self.bullets.append(bullet)

    def player_input(self) -> str:
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.shoot()
        if keys[pygame.K_SPACE] and self.rect.y == 520:
            self.gravity = -20
        if keys[pygame.K_a]:
            self.rect.x = max(0, self.rect.x - self.speed)
            return 'left'
        if keys[pygame.K_d]:
            self.rect.x = min(SCREEN_WIDTH - 100, self.rect.x + self.speed)
            return 'right'
        return 'stand'

    def apply_gravity(self) -> None:
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= 520:
            self.rect.y = 520

    def animation_state(self, status: str) -> None:
        if self.rect.y < 520:
            self.jump()
        else:
            if status == 'stand':
                self.stand()
            elif status in('left', 'right'):
                self.walk()

    def update(self, screen: pygame.Surface):
        status = self.player_input()
        self.apply_gravity()
        self.animation_state(status)
        for bullet in self.bullets:
            if bullet.position[0] > SCREEN_WIDTH or bullet.position[0] < 0 or bullet.position[1] < 0 or bullet.position[1] > SCREEN_WIDTH: 
                self.bullets.remove(bullet)
            bullet.draw(screen)
            bullet.update()
