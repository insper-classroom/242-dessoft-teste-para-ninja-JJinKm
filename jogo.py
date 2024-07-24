import pygame
from tela_jogo import game_screen
from tela_final import end_screen
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (112,112,112)
BLACK = (0,0,0)
WHITE = (255,255,255)

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Ninja')

font = pygame.font.SysFont(None,78)
jogar = font.render('Jogar',True,BLACK)
jogar_rect = jogar.get_rect(center=(WIDTH/2,HEIGHT/2))
clicked = False
running = True
state = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or state == 2:
            running = False

    pos = pygame.mouse.get_pos()
    window.fill(WHITE)
    window.blit(jogar,jogar_rect)
    if jogar_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
            clicked = True
            pygame.time.wait(100)
            screengame = game_screen(window)
            state = screengame[0]
            correct_counter = screengame[1]
        if state == 0:
            end_screen(window,correct_counter)
            state = 1
            clicked = False
    pygame.display.flip()

pygame.quit()