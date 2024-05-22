import pygame
from player import player
from fireball import fireball
from enemy import enemy

#from menu import Menu

pygame.init()
pygame.display.set_caption("top down grid game")
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
gameover = False

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False]
ticker = 0

p1 = player()
e1 = enemy()
f1 = fireball()
#menu = Menu()
FPS = 60

map = [
    [2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 0, 0, 0, 2, 2, 4, 0, 2, 0, 0, 0, 0, 3, 0, 2, 2, 2, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 0, 2, 4, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 2],
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2],
    [2, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2],
    [2, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2],
    [2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 3, 2, 0, 0, 0, 2],
    [2, 3, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 0, 2, 2, 4, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 0, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 5],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

dirt = pygame.image.load("dirt.png")
nether = pygame.image.load("brick.png")
grass = pygame.image.load("grass.png")

while not gameover:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = False

    # physics section
    p1.move(keys, map)
    f1.move()
    if keys[SPACE] == True:
        f1.shoot(p1.xpos, p1.ypos, p1.direction)
    e1.move(map, ticker, p1.xpos, p1.ypos)
    # menu.input()

    # render section

    screen.fill((0, 0, 0))

    # draw map
    for i in range(16):
        for j in range(24):
            if map[i][j] == 1:
                screen.blit(
                    dirt,
                    (
                        j * 50,
                        i * 50,
                    ),
                    (0, 0, 50, 50),
                )
            if map[i][j] == 2:
                screen.blit(
                    nether,
                    (
                        j * 50,
                        i * 50,
                    ),
                    (0, 0, 50, 50),
                )
            if map[i][j] == 3:
                screen.blit(
                    grass,
                    (
                        j * 50,
                        i * 50,
                    ),
                    (0, 0, 50, 50),
                )

    p1.draw(screen)

    if f1.isAlive == True:
        f1.draw(screen)

    #menu.draw(screen)

    pygame.display.flip()

pygame.quit()
