import pygame
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Start Cutscene')
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock()

font = pygame.font.Font("Baskic8.otf", 29)
font2 =  pygame.font.Font("Baskic8.otf", 23)
start_font = pygame.font.Font("Baskic8.otf", 30)
bg = pygame.image.load('RLGMLA.png').convert_alpha()
kite1 = pygame.image.load('kite1.png').convert_alpha()
kite2 = pygame.image.load('kite2.png').convert_alpha()
kite3 = pygame.image.load('kite3.png').convert_alpha()
kite1 = pygame.transform.scale(kite1, (150, 150))
kite2 = pygame.transform.scale(kite2, (150, 150))
kite3 = pygame.transform.scale(kite3, (150, 150))



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
        screen.blit(kite1, (0, 0))
        screen.blit(kite2, (200, 0))
        screen.blit(kite3, (300, 100))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0, 350, 500, 200)))
        draw_text('Today is the kite fighting competition', font, (255, 255, 255), screen, 10, 360)
        draw_text('You must achieve victory to make Baba Proud', font2, (255, 255, 255), screen, 10, 410)
        draw_text('Press Space to start', font, (255, 255, 255), screen, 10, 460)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    import Instructions

        pygame.display.update()
        mainClock.tick(60)


main_menu()