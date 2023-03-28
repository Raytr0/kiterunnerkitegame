import pygame
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Start Cutscene')
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock()

font = pygame.font.Font("Baskic8.otf", 20)
font2 =  pygame.font.Font("Baskic8.otf", 23)
start_font = pygame.font.Font("Baskic8.otf", 30)
bg = pygame.image.load('RLGMLA.png').convert_alpha()



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    clock.tick(60)
    while True:

        screen.blit(bg, (0, 0))
        draw_text('With the help of Hassan', font, (255, 255, 255), screen, 100, 200)
        draw_text('You manage to beat everyone and win!', font, (255, 255, 255), screen, 100, 250)
        draw_text('It is the greatest moment of your life!', font, (255, 255, 255), screen, 100, 300)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)


main_menu()