import pygame
from copy import deepcopy
from pygame.locals import *

class Board():
    def __init__(self):
        self.board = [[0 for i in range(3)] for j in range(3)]

    def allowed(self, x, y):
        if self.board[x][y] == 0:
            return True

    def update(self, x, y, move):
        self.board[y][x] = move

    @staticmethod
    def win(board, move):
        for i in range(3):
            if board[i] == [move, move, move]:
                return True 
        if board[0][0] == board[1][1] == board[2][2] == move:
            return True 
        if board[0][2] == board[1][1] == board[2][0] == move:
            return True 
        for j in range(3):
            if [board[i][j] for i in range(3)] == [move, move, move]:
                return True
        return False 

game = Board()

class Bot():
    def __init__(self, difficulty):
        self.depth = difficulty       

    @staticmethod
    def staticEvaluation(position):
        if game.win(position, 1):
            return 1
        if game.win(position, 2):
            return -1
        return 0
    
    @staticmethod
    def listMoves(position, move):
        l = []
        for i in range(3):
            for j in range(3):
                pos = deepcopy(position)
                if pos[i][j] == 0:
                    pos[i][j] = move
                    l.append(pos)
        return l

    @staticmethod
    def minimax(position, max_player, depth):
        if max_player:
            opponent_move = 2
        else: opponent_move = 1
        if depth == 0 or game.win(position, opponent_move):
            return (bot.staticEvaluation(position), position)
        
        if max_player:
            move = 1
            max_eval = -2
            for child in bot.listMoves(position, move):
                e = bot.minimax(child, False, depth - 1)[0]
                if e > max_eval:
                  max_eval = e
                  pos = child
            return (max_eval, pos)

        min_eval = 2 
        move = 2
        for child in bot.listMoves(position, move):
            e = bot.minimax(child, True, depth - 1)[0]
            if e < min_eval:
                min_eval = e
                pos = child
        return (min_eval, pos)

    @staticmethod
    def choseMove(position):
        e, pos = bot.minimax(position, False, bot.depth)
        for i in range(3):
            for j in range(3):
                if position[i][j] != pos[i][j]:
                    print((e, pos, (i, j)))
                    return (i, j)

bot = Bot(3)

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
                    user_interface.drawCross(y, x)
                elif game.board[x][y] == 2:
                    pygame.draw.circle(self.window, (255, 0, 0),
                                        (y * 200 + 100, x * 200 + 100), 100, 5)

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
                    if game.allowed(self.y, self.x):
                        game.update(self.x, self.y, 1)
                        move = bot.choseMove(game.board)
                        game.update(move[1], move[0], 2)

    def render(self):
        self.window.fill((0,0,0))
        for i in range(1, 3):
            pygame.draw.line(self.window, (255, 255, 255), (200 * i, 0), (200 * i, 600), 5)
            pygame.draw.line(self.window, (255, 255, 255), (0, 200 * i), (600, 200 * i), 5)
        user_interface.drawMoves()
        pygame.draw.rect(self.window, (0, 255, 0), (self.x * 200, self.y * 200, 200, 200), 5)
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, 600, 600), 5)
        pygame.display.update()

    def run(self):
        board = game.board
        while self.running and not (game.win(board, 1) or game.win(board, 2)):
            self.processInput()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
user_interface.run()
pygame.quit()
