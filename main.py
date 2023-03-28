import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Kite Game')
clock = pygame.time.Clock()
done = False
font = pygame.font.Font("freesansbold.ttf", 50)
bg = pygame.image.load('sunsetbackground.png').convert_alpha()
bg = pygame.transform.scale(bg, (500, 500))

x = 450
y = 250
move = 5

health_p1 = 100
health_p2 = 100

Colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "darkRed": (55, 0, 0),
    "lightRed": (255, 108, 23),
    "green": (0, 255, 0),
    "darkGreen": (0, 55, 0),
    "blue": (0, 0, 255),
    "darkBlue": (0, 0, 55),
    "navyBlue": (0, 30, 100),
    "lightPurple": (113, 0, 155),
    "darkPurple": (55, 0, 55),
    "lightGrey": (200, 200, 200),
    "paleTurquoise": (175, 238, 238),
    "lightYellow": (255, 240, 23)
}

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


kiteMove = True


while not done:

    clock.tick(60)
    if kiteMove:
        x -= move

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    healthbar_p1 = pygame.Rect(50, 50, health_p1, 50)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((45, 45, 110, 60)), width=5)
    pygame.draw.rect(screen, (0, 255, 0), healthbar_p1)

    healthbar_p2 = pygame.Rect(350, 50, health_p2, 50)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((345, 45, 110, 60)), width=5)
    pygame.draw.rect(screen, (255, 0, 0), healthbar_p2)

    kite = ((x + 25, y), (x, y + 50), (x - 25, y), (x, y - 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if x < 100 and x > 60 and event.key == pygame.K_SPACE:
                x=450
                health_p2 -= 20
                move = random.randint(5, 10)
            else:
                x=450
                health_p1 -= 20
                move = random.randint(5, 10)

    if x < 0:
        health_p1 -= 20
        x = 450

    if health_p2 == 0:
        playerWin = font.render('You Win!', False, Colors["white"])
        screen.blit(playerWin, (150, 150))
        kiteMove = False
        import endCutscene
    elif health_p1 == 0:
        playerLose = font.render('You Lose...', False, Colors["white"])
        screen.blit(playerLose, (150, 150))
        kiteMove = False
        pygame.time.wait(2000)
        import badCutscene

    pygame.draw.polygon(screen, (255, 255, 255), ((50, 250), (75, 300), (100, 250), (75, 200)), width=5)

    pygame.draw.polygon(screen, (255, 255, 255), kite)

    pygame.display.update()


