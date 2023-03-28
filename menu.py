import pygame
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Game')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.Font("Baskic8.otf", 50)
start_font = pygame.font.Font("Baskic8.otf", 30)
button = pygame.image.load('FREE PIXEL ART BUTTONS.png').convert_alpha()
bg = pygame.image.load('RLGMLA.png').convert_alpha()
button = pygame.transform.scale(button, (1000, 1000))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.blit(bg, (0, 0))
        draw_text('Kite Game', font, (255, 255, 255), screen, 145, 100)
        screen.blit(button, (75, 170), (600, 0, 300, 160))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 250, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                import cutscene1
        draw_text('Start', start_font, (255, 255, 255), screen, 210, 260)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


main_menu()