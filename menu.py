import pygame


class menu:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.mousePos = (self.xpos, self.ypos)
        self.mouseDown = False
        self.state = 1

    def draw(self, screen):
        if self.state == 1:
            button1 = 100 < self.mousePos[0] < 300 and 400 < self.mousePos[1] < 550
            button2 = 400 < self.mousePos[0] < 600 and 400 < self.mousePos[1] < 550
            button3 = 700 < self.mousePos[0] < 900 and 400 < self.mousePos[1] < 550

        if button1 and self.mouseDown:
            self.state = 2
        elif button2 and self.mouseDown:
            self.state = 3
        elif button3 and self.mouseDown:
            self.state = 4
        if self.state == 2:
            screen.fill((80, 200, 100))
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150))
        elif self.state == 3:
            screen.fill((50, 197, 200))
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
        elif self.state == 4:
            screen.fill((100, 150, 200))
            pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))
        else:
            screen.fill((230, 100, 100))
            pygame.draw.rect(
                screen,
                (100, 230, 100) if not button1 else (200, 230, 200),
                (100, 400, 200, 150),
            )
            pygame.draw.rect(
                screen,
                (100, 230, 100) if not button2 else (200, 230, 200),
                (400, 400, 200, 150),
            )
            pygame.draw.rect(
                screen,
                (100, 230, 100) if not button3 else (200, 230, 200),
                (700, 400, 200, 150),
            )
    
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.mousePos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseDown = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.state = 1  # Return to menu when 'q' is pressed
        
