import pygame
from pygame.locals import *

class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True 

    def processInput(self):
        for event in pygame.event.get():
            if event.type = pygame.QUIT:
                self.running = False
                break 

    def update(self):
        pass

    def render(self):
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

game = Game()
game.run()

pygame.quit()
