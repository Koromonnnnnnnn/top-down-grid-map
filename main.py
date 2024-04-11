import pygame
from player import player

pygame.init()
pygame.display.set_caption("top down grid game")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
gameover = False

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False]

p1 = player()
FPS = 60

map = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 0, 0, 0, 2, 2, 0, 0, 2],
    [2, 0, 0, 0, 0, 2, 2, 0, 0, 2],
    [2, 0, 0, 2, 2, 2, 2, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 1, 1, 1, 1, 1, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False

    # physics section
    p1.move(keys, map)

    # render section

    screen.fill((0, 0, 0))
    p1.draw(screen)

    # draw map
    for i in range(10):
        for j in range(10):
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

    pygame.display.flip()

pygame.quit()
