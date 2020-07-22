import pygame
from pygame.locals import *

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Tic Tac Toe')
running = True
clock = pygame.time.Clock() 

while running:

    eventList = pygame.event.get()
    for event in enventList:
        if event.type = pygame.QUIT:
            running = False 
            break

    pygame.display.update()
    clock.tick(60)

pygame.quit()
