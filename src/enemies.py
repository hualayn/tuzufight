import pygame
from random import randint

pics_folder = 'pics/charactors/EnemySprites/'


class Snail:
    def __init__(self):
        self.move = [
            pygame.image.load(f'{pics_folder}snail.png').convert_alpha(),
            pygame.image.load(f'{pics_folder}snail_walk.png').convert_alpha()
        ]
        self.rect = self.move[0].get_rect(midbottom=(randint(1080, 1300), 615))
        self.frame_speed = 0.1  # 控制动画播放速度
        self.speed = 1


class Bee:
    def __init__(self):
        self.move = [
            pygame.image.load(f'{pics_folder}bee.png').convert_alpha(),
            pygame.image.load(f'{pics_folder}bee_fly.png').convert_alpha()
        ]
        self.rect = self.move[0].get_rect(midbottom=(randint(1080, 1300), 415))
        self.frame_speed = 0.3  # 控制动画播放速度
        self.speed = 5


class Snake:
    def __init__(self):
        self.move = [
            pygame.image.load(f'{pics_folder}snake.png').convert_alpha(),
            pygame.image.load(f'{pics_folder}snake_walk.png').convert_alpha()
        ]
        self.rect = self.move[0].get_rect(midbottom=(randint(1080, 1300), 615))
        self.frame_speed = 0.2
        self.speed = 3


class Bat:
    def __init__(self):
        self.move = [
            pygame.image.load(f'{pics_folder}bat.png').convert_alpha(),
            pygame.image.load(f'{pics_folder}bat_fly.png').convert_alpha()
        ]
        self.rect = self.move[0].get_rect(midbottom=(randint(1080, 1300), 415))
        self.frame_speed = 0.3
        self.speed = 7



class Enemy(pygame.sprite.Sprite):
    def __init__(self, animal: Snail | Bee = None):
        super().__init__()
        self.animation_index = 0
        self.animal = animal
        self.image = animal.move[self.animation_index]
        self.rect = animal.rect        
    def update(self):
        self.animation_state()
        self.destroy()
    def animation_state(self) -> None:
        self.animation_index += self.animal.frame_speed
        if self.animation_index >= len(self.animal.move):
            self.animation_index = 0        
        self.image = self.animal.move[int(self.animation_index)]

        self.rect.x -= self.animal.speed
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
