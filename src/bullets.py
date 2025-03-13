import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10)).fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        ...