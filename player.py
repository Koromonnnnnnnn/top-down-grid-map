import pygame

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False]

Link = pygame.image.load("player.png")
Link.set_colorkey((255, 0, 255))


class player:
    def __init__(self):

        self.xpos = 400
        self.ypos = 415
        self.vx = 0
        self.vy = 0
        self.direction = LEFT

        self.frameWidth = 64
        self.frameHeight = 96
        self.RowNum = 0  # for left animation
        self.frameNum = 0
        self.ticker = 0

        self.frameWidth = 64
        self.frameHeight = 96
        self.RowNum = 1  # for Right animation
        self.frameNum = 0
        self.ticker = 0

        self.frameWidth = 64
        self.frameHeight = 96
        self.RowNum = 2  # for Up animation
        self.ticker = 0

        self.frameWidth = 64
        self.frameHeight = 96
        self.RowNum = 3  # for Down animation
        self.frameNum = 0
        self.ticker = 0

    def draw(self, screen):
        screen.blit(
            Link,
            (self.xpos, self.ypos),
            (
                self.frameWidth * self.frameNum,
                self.RowNum * self.frameHeight,
                self.frameWidth,
                self.frameHeight,
            ),
        )

    def move(self, keys, map):

        if keys[LEFT] == True:
            self.vx = -3
            self.direction = LEFT
            self.RowNum = 0
        elif keys[RIGHT] == True:
            self.vx = 3
            self.direction = RIGHT
            self.RowNum = 1
        elif keys[UP] == True:
            self.vy = -3
            self.direction = UP
            self.RowNum = 2
        elif keys[DOWN] == True:
            self.vy = 3
            self.direction = DOWN
            self.RowNum = 3
        else:
            self.vx = 0
            self.vy = 0

        if self.vx < 0:
            self.ticker += 1
            if self.ticker % 10 == 0:
                self.frameNum += 1
            if self.frameNum > 7:
                self.frameNum = 0

        if self.vx > 0:
            self.ticker += 1
            if self.ticker % 10 == 0:
                self.frameNum += 1
            if self.frameNum > 7:
                self.frameNum = 0

        if self.vy < 0:
            self.ticker += 1
            if self.ticker % 10 == 0:
                self.frameNum += 1
            if self.frameNum > 7:
                self.frameNum = 0

        if self.vy > 0:
            self.ticker += 1
            if self.ticker % 10 == 0:
                self.frameNum += 1
            if self.frameNum > 7:
                self.frameNum = 0

        if map[int((self.ypos - 10) / 50)][int((self.xpos - 10) / 50)] == 2:
            self.xpos += 3
        if map[int((self.ypos) / 50)][int((self.xpos + 30 + 5) / 50)] == 2:
            self.xpos -= 3

        self.xpos += self.vx
        self.ypos += self.vy
