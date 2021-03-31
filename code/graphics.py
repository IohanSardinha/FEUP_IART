import pygame
from tenpair import *
from time import time


selectedPiece = (-1,-1)

def drawBoard(board, screen, fontsmall, fontbig, moves):
    startx, starty = (15,40)

    deal = pygame.draw.rect(screen, (210,210,210), pygame.Rect(245, 10, 40,25))
    screen.blit( fontsmall.render("Deal", False, (0,0,0)) ,(248, 10))

    screen.blit( fontsmall.render("Moves: "+str(moves), False, (255,255,255)) ,(startx, 10))

    numbers = []
    for i, line in enumerate(board):
        for j, value in enumerate(line):
            screen.blit( fontbig.render(" " if value == 0 else str(value), False, (255,255,0) if selectedPiece == (j, i) else (255,255,255)) ,(startx+ j*30 + 8, starty + i*30 - 3))
            number = pygame.draw.rect(screen, (255,255,0) if selectedPiece == (j, i) else (255,255,255), pygame.Rect(startx+ j*30, starty+ i*30, 30,30),1)
            numbers.append((number, j, i, value))
    return numbers, deal

def pieceClick(board, moves, i, j, value):

    global selectedPiece

    if value == 0:
        pass
    
    elif selectedPiece == (-1,-1):
        selectedPiece = (i,j)
        
    elif selectedPiece == (i,j):
        selectedPiece = (-1,-1)

    elif validRemove((i,j), selectedPiece, board):
        board = removePiece((i, j), selectedPiece, board)
        moves += 1
        selectedPiece = (-1,-1)
        
    else:
        selectedPiece = (-1,-1)

    return board, moves

def humanPlayer(screen, clock):
    level = 0

    board, moves = initialState(level)

    fontsmall = pygame.font.SysFont('Arial', 20)
    fontbig = pygame.font.SysFont('Arial', 30)

    while True:
        screen.fill((0,0,0))

        numbers, dealButton = drawBoard(board, screen, fontsmall, fontbig, moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:                
                mousePos = pygame.mouse.get_pos()
                if dealButton.collidepoint(mousePos):
                    board = deal(board)
                else:
                    for number, i, j ,value in numbers:
                        if number.collidepoint(mousePos):
                            board, moves = pieceClick(board, moves, i, j, value)

        if win(board):
            print("Congratulations you won level "+str(level)+" in "+str(moves)+" moves!!!")
            
            if level < initialState(size=True):
                level += 1
                board, moves = initialState(level)
            else:
                return True
        
        pygame.display.update()
        clock.tick(60)    

def mainMenu(screen, clock):
    while True:

        fontbig = pygame.font.SysFont('Bauhaus 93', 50)
        screen.blit( fontbig.render("Tenpair", False, (200,200,255)) ,(60, 50))

        play_button =      pygame.draw.rect(screen, (210,210,210), pygame.Rect(60, 150, 170, 50))
        solve_button =     pygame.draw.rect(screen, (210,210,210), pygame.Rect(60, 210, 170, 50))
        howtoplay_button = pygame.draw.rect(screen, (210,210,210), pygame.Rect(60, 280, 170, 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        pygame.display.update()
        clock.tick(60) 

def main():

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Tenpair')
    screen = pygame.display.set_mode((300,600))

    clock = pygame.time.Clock()

    nextScreen = mainMenu(screen, clock)
    while not nextScreen == False:
        nextScreen = nextScreen(screen,clock)
        
    pygame.quit()


if __name__ == "__main__":
    main()
