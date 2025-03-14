import pygame
from src.settings import BG_MUSIC
def set_bg_music() -> None:
    '''背景音乐'''
    pygame.mixer.music.load(BG_MUSIC)
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.5)


def display_background(screen: pygame.Surface) -> None:
    '''背景'''
    background = pygame.image.load('pics/Backgrounds/backgrounds.png').convert()
    screen.blit(background, (0, 0))
