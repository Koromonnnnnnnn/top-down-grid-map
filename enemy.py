import pygame
import random

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

enemy = pygame.image.load("enemy.png")
ticker = 0

class enemy:
    def __init__(self):
        self.xpos = 400
        self.ypos = 200
        self.direction = RIGHT

    def draw(self, screen):
        screen.blit(enemy, (self.xpos, self.ypos, 20, 20))
    
    def move(self):
        if ticker % 40 == 0:
            num = random.randrange(0,4)
            if num == 0:
                self.direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction = UP
            elif num == 3:
                self.direction = DOWN
        if abs(int(py/50) - int(self.ypos/50)) < 2:
            if px < self.xpos:
                self.xpos -= 5
                self.direction = LEFT
            else:
                self.xpos += 5
                self.direction = RIGHT
