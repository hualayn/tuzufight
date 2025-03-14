import pygame
from src.bullets import Bullet

def detect_collision(player: pygame.sprite.Sprite, enemies: pygame.sprite.Group):
    if pygame.sprite.spritecollide(player.sprite, enemies, False):
        enemies.empty()
        return False 
    return True


def detect_bullet_collision(bullets: pygame.sprite.Group, enemies: pygame.sprite.Group):
    if pygame.sprite.groupcollide(bullets, enemies, True, True):
        return True