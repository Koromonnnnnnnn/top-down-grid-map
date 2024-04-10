import pygame
from player import player

pygame.init()
pygame.display.set_caption("top down grid game")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
gameover = False

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

    pygame.display.flip()

pygame.quit()
