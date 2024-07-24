import pygame
from gerador import gera_numeros
import square
import time

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (112,112,112)
BLACK = (0,0,0)
WHITE = (255,255,255)

def game_screen(window):
    game = True

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None,48)
    rand_list = gera_numeros()
    n_rect_list = []
    n_list = []
    for i in range(len(rand_list) - 1):
        n = font.render(str(rand_list[i]),True,BLACK)
        n_list.append(n)
        n_rect = n.get_rect(center=(WIDTH/2,500-100*(i)))
        n_rect_list.append(n_rect)

    correct = font.render('Certo!',True,BLACK)
    wrong = font.render('Errado!',True,BLACK)

    sum = font.render(str(rand_list[3]),True,BLACK)
    sum_rect = sum.get_rect(center=(20,20))

    b_square = square.Square(450)
    g_square = square.Square(350)
    r_square = square.Square(250)

    rect_ground = pygame.Rect(0,550, WIDTH, 50)

    counter = 60
    timer = font.render(str(counter),True,BLACK)
    timer_rect = timer.get_rect(center=(780,20))
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    vida = 3

    correct_counter = 0

    while game:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                state = 2
            if event.type == pygame.USEREVENT:
                counter -= 1
                timer = font.render(str(counter),True,BLACK)
                timer_rect = timer.get_rect(center=(780,20))

        window.fill(WHITE)

        if b_square.draw(window,BLUE):
            print(rand_list[0])
            if rand_list[1] + rand_list[2] == rand_list[3]:
                correct_counter += 1
                window.fill(WHITE)
                correct_rect = correct.get_rect(center=(WIDTH/2,500))
                window.blit(correct,correct_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
            else:
                vida -= 1
                window.fill(WHITE)
                wrong_rect = wrong.get_rect(center=(WIDTH/2,500))
                window.blit(wrong,wrong_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
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

        if g_square.draw(window,GREEN):
            print(rand_list[1])
            if rand_list[2] + rand_list[0] == rand_list[3]:
                correct_counter += 1
                window.fill(WHITE)
                correct_rect = correct.get_rect(center=(WIDTH/2,400))
                window.blit(correct,correct_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
            else:
                vida -= 1
                window.fill(WHITE)
                wrong_rect = wrong.get_rect(center=(WIDTH/2,400))
                window.blit(wrong,wrong_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
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

        if r_square.draw(window,RED):
            print(rand_list[2])
            if rand_list[0] + rand_list[1] == rand_list[3]:
                correct_counter += 1
                window.fill(WHITE)
                correct_rect = correct.get_rect(center=(WIDTH/2,300))
                window.blit(correct,correct_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
            else:
                vida -= 1
                window.fill(WHITE)
                wrong_rect = wrong.get_rect(center=(WIDTH/2,300))
                window.blit(wrong,wrong_rect)
                pygame.display.flip()
                pygame.time.wait(1000)
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


        for i in range(len(n_list)):
            window.blit(n_list[i],n_rect_list[i])

        pygame.draw.rect(window, GRAY, rect_ground)

        window.blit(sum,sum_rect)
        window.blit(timer,timer_rect)
        
        if vida == 0:
            game = False
            state = 0
        if counter == 0:
            game = False
            state = 0

        pygame.display.flip()
    return [state,correct_counter]