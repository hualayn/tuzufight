import pygame
from pygame.math import Vector2


class Bullet:
    def __init__(self, position: Vector2, direction: Vector2):
        self.position = position
        self.direction = direction.normalize() # 确保方向向量长度为1
        self.speed = 10
        self.radius = 4  # 子弹大小


    def update(self):
        """更新子弹位置"""
        self.position += self.direction * self.speed

    def draw(self, screen):
        """绘制子弹"""        
        self.rect = pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)