import pygame
import sys

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


kiteMove = True


while not done:

    clock.tick(60)
    if kiteMove:
        x -= 5

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

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
            else:
                x=450
                health_p1 -= 20

    if x < 0:
        health_p1 -= 20
        x = 450

    if health_p1 == 0:
        playerWin = font.render('You Win!', False, Colors["white"])
        screen.blit(playerWin, (150, 150))
        kiteMove = False
    elif health_p2 == 0:
        playerLose = font.render('You Lose...', False, Colors["white"])
        screen.blit(playerLose, (150, 150))
        kiteMove = False

    pygame.draw.polygon(screen, (255, 255, 255), ((50, 250), (75, 300), (100, 250), (75, 200)), width=5)

    pygame.draw.polygon(screen, (255, 255, 255), kite)

    pygame.display.update()

