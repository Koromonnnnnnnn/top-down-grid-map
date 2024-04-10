import pygame

pygame.init()
pygame.display.set_caption("top down grid game")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
gameover = False


FPS = 60

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5


class player:
    def __init__(self):

        self.xpos = 400
        self.ypos = 415
        self.vx = 0
        self.vy - 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))


def move(self, keys, map):

    if keys[LEFT] == True:
        self.vx = -3
        print("Moving left")
    elif keys[RIGHT] == True:
        self.vx = 3
        print("Moving right")
    else:
        self.vx = 0

    if map[int((self.ypos - 10) / 50)][int((self.xpos - 10) / 50)] == 2:
        self.xpos += 3
    if map[int((self.ypos) / 50)][int((self.xpos + 30 + 5) / 50)] == 2:
        self.xpos -= 3

    self.xpos += self.vx


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

    # render section

    screen.fill((0, 0, 0))

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
