import pygame
from tela_jogo import game_screen
import time

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (112,112,112)
BLACK = (0,0,0)
WHITE = (255,255,255)

def end_screen(window,correct_counter):
    game = True
    font = pygame.font.SysFont(None,48)
    score = font.render("Acertou: {0}".format(correct_counter),True,BLACK)
    score_rect = score.get_rect(center=(WIDTH/2,HEIGHT/2))

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        window.fill(WHITE)
        window.blit(score,score_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        game = False
