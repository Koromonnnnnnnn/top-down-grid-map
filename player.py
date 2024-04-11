import pygame

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False]


class player:
    def __init__(self):

        self.xpos = 400
        self.ypos = 415
        self.vx = 0
        self.vy = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))

    def move(self, keys, map):

        if keys[LEFT] == True:
            self.vx = -3
        elif keys[RIGHT] == True:
            self.vx = 3
        elif keys[UP] == True:
            self.vy = -3
        elif keys[DOWN] == True:
            self.vy = 3
        else:
            self.vx = 0
            self.vy = 0

        if map[int((self.ypos - 10) / 50)][int((self.xpos - 10) / 50)] == 2:
            self.xpos += 3
        if map[int((self.ypos) / 50)][int((self.xpos + 30 + 5) / 50)] == 2:
            self.xpos -= 3

        self.xpos += self.vx
        self.ypos += self.vy
