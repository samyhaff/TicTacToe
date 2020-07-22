import pygame
from pygame.locals import *

def drawCross(x, y):


class UserInterface():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("TIC TAC TOE")
        self.clock = pygame.time.Clock()
        self.running = True
        self.x = 0
        self.y = 0

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.x < 2:
                    self.x += 1
                if event.key == pygame.K_LEFT and self.x > 0:
                    self.x -= 1
                if event.key == pygame.K_UP and self.y > 0:
                    self.y -= 1
                if event.key == pygame.K_DOWN and self.y < 2:
                    self.y += 1
                if event.key == pygame.K_RETURN:
                    pass

    def render(self):
        self.window.fill((0,0,0))
        for i in range(1, 3):
            pygame.draw.line(self.window, (255, 255, 255), (200 * i, 0), (200 * i, 600), 5)
            pygame.draw.line(self.window, (255, 255, 255), (0, 200 * i), (600, 200 * i), 5)
        pygame.draw.rect(self.window, (255, 0, 0), (self.x * 200, self.y * 200, 200, 200), 5)
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, 600, 600), 5)
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
user_interface.run()
pygame.quit()
