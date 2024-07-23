import pygame
from gerador import gera_numeros
import square
pygame.init()

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jogo')

game = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (112,112,112)
BLACK = (0,0,0)
font = pygame.font.SysFont(None,48)
rand_list = gera_numeros()
n_rect_list = []
n_list = []
for i in range(len(rand_list) - 1):
    n = font.render(str(rand_list[i]),True,BLACK)
    n_list.append(n)
    n_rect = n.get_rect(center=(WIDTH/2,500-100*(i)))
    n_rect_list.append(n_rect)

sum = font.render(str(rand_list[3]),True,BLACK)
sum_rect = sum.get_rect(center=(20,20))

b_square = square.Square(450)
g_square = square.Square(350)
r_square = square.Square(250)
rect_ground = pygame.Rect(0,550, WIDTH, 50)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.fill((255,255,255))
    if b_square.draw(window,BLUE):
        print(rand_list[0])
    if g_square.draw(window,GREEN):
        print(rand_list[1])
    if r_square.draw(window,RED):
        print(rand_list[2])
    pygame.draw.rect(window, GRAY, rect_ground)
    for i in range(len(n_rect_list)):
        window.blit(n_list[i],n_rect_list[i])

    window.blit(sum,sum_rect)

    pygame.display.update()

pygame.quit()