import pygame
from pygame.locals import *

class Board():
    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]

    def allowed(self, x, y):
        if self.board[x][y] == 0:
            return True

    def update(self, x, y, move):
        self.board[x][y] = move

    def win(self, move):
        for i in range(3):
            if self.board[i] == [move, move, move]:
                return True 
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == move:
            return True 
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == move:
            return True 
        for j in range(3):
            if [self.board[i][j] for i in range(3)] == [move, move, move]:
                return True
        return False 

game = Board()

class UserInterface():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("TIC TAC TOE")
        self.clock = pygame.time.Clock()
        self.running = True
        self.x = 0
        self.y = 0

    def drawCross(self, x, y):
        pygame.draw.line(self.window, (0, 0, 255), 
                        (x * 200, y * 200), 
                        (x * 200 + 200, y * 200 + 200), 7)
        pygame.draw.line(self.window, (0, 0, 255), 
                        (x * 200, y * 200 + 200),
                        (x * 200 + 200, y * 200), 7)

    def drawMoves(self):
        for x in range(3):
            for y in range(3):
                if game.board[x][y] == 1:
                    user_interface.drawCross(x, y)
                elif game.board[x][y] == 2:
                    pygame.draw.circle(self.window, (255, 0, 0),
                                        (x * 200 + 100, y * 200 + 100), 100, 5)

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
                    if game.allowed(self.x, self.y):
                        game.update(self.x, self.y, 1)

    def render(self):
        self.window.fill((0,0,0))
        for i in range(1, 3):
            pygame.draw.line(self.window, (255, 255, 255), (200 * i, 0), (200 * i, 600), 5)
            pygame.draw.line(self.window, (255, 255, 255), (0, 200 * i), (600, 200 * i), 5)
        user_interface.drawMoves()
        pygame.draw.rect(self.window, (255, 0, 0), (self.x * 200, self.y * 200, 200, 200), 5)
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, 600, 600), 5)
        pygame.display.update()

    def run(self):
        while self.running and not (game.win(1) or game.win(2)):
            self.processInput()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
user_interface.run()
pygame.quit()
