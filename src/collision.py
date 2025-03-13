import pygame

def detect_collision(player: pygame.sprite.Sprite, enemies: pygame.sprite.Group):
    if pygame.sprite.spritecollide(player.sprite, enemies, False):
        enemies.empty()
        return False
    return True