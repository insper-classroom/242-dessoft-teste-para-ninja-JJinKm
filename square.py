import pygame

class Square():
    def __init__(self,y):
        self.rect = pygame.Rect(350,y,100,100)
        self.clicked = False

    def draw(self,surface,color):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        pygame.draw.rect(surface,color,self.rect)
        return action