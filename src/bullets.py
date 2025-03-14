import pygame
from pygame.math import Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, direction: Vector2):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.direction = direction.normalize() # 确保方向向量长度为1
        self.speed = 10
        self.radius = 4  # 子弹大小


    def update(self):
        """更新子弹位置"""
        self.position += self.direction * self.speed
        self.rect.center = self.position
