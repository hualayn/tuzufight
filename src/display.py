import pygame
from pygame import Surface
from pygame.font import Font
from src.settings import SCREEN_WIDTH

def display_logo(font: Font, screen: Surface) -> None:
    '''游戏标题'''
    logo = font.render('土族大战土家族', True, (0, 0, 0))
    logo_rect = logo.get_rect(midbottom=(SCREEN_WIDTH/2, 150))
    screen.blit(logo, logo_rect)


def display_score(font: Font, screen: Surface, score: int) -> int:
    '''游戏分数'''
    pygame.time.get_ticks()
    score_surf = font.render(f'得分：{score}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(midbottom=(SCREEN_WIDTH/2, 150))
    screen.blit(score_surf, score_rect)
    return score

def display_game_start(font: Font, screen: Surface) -> None:
    '''游戏开始'''
    game_start = font.render('按下 空格 开始游戏', False, (0, 0, 0))
    game_start_rect = game_start.get_rect(midbottom=(SCREEN_WIDTH/2, 550))
    screen.blit(game_start, game_start_rect)

def display_alien_stand(screen: Surface) -> None:
    '''游戏开始或失败时，玩家站立的姿态'''
    alien_stand = pygame.transform.rotozoom(pygame.image.load('pics/charactors/AlienSprites/alienBlue_stand.png').convert_alpha(), 0, 2)
    alien_stand_rect = alien_stand.get_rect(midbottom=(SCREEN_WIDTH/2, 400))
    screen.blit(alien_stand, alien_stand_rect)

def display_game_over(font: Font, screen: Surface) -> None:
    '''游戏结束'''
    game_over = font.render('GAME OVER', False, (0, 0, 0))
    game_over_rect = game_over.get_rect(midbottom=(SCREEN_WIDTH/2, 350))
    screen.blit(game_over, game_over_rect)

def show_score(font: Font, screen: Surface, score: int) -> None:
    '''游戏结束，显示最终得分'''
    score_board = font.render(f'得分：{score}', False, (0, 0, 0))
    score_board_rect = score_board.get_rect(midbottom=(SCREEN_WIDTH/2, 550))
    screen.blit(score_board, score_board_rect)