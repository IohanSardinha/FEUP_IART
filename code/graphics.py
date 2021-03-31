import pygame
from ai import *
from tenpair import *
from time import time,sleep
from bfs import BFS
from dfs import DFS
from itdep import IDDFS
from astar import aStar
from greedy import greedy
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

def playStopButton(screen, clock, playing, ticks = 50):
    tick = 0
    while tick < ticks:
        button = pygame.draw.rect(screen, (0,0,0), pygame.Rect(195, 5, 30,30))
        if playing:
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(202, 10, 5, 20))
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(212, 10, 5, 20))
            tick += 1
        else:
            pygame.draw.polygon(screen, (255,0,0), [[200, 10], [200, 30], [220, 20]])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:                
                mousePos = pygame.mouse.get_pos()
                if button.collidepoint(mousePos):
                    playing = not playing
        
        pygame.display.update()
        clock.tick(60)
    return playing

def showSolution(screen, clock, board, moves, solution):

    global selectedPiece

    playing = False
    
    fontsmall = pygame.font.SysFont('Arial', 20)
    fontbig = pygame.font.SysFont('Arial', 30)

    for move in solution:
        screen.fill((0,0,0))
        numbers, dealButton = drawBoard(board, screen, fontsmall, fontbig, moves)
        playing =  playStopButton(screen, clock, playing)

        if move == "( deal )":
            board = deal(board)
            screen.fill((0,0,0))
            numbers, dealButton = drawBoard(board, screen, fontsmall, fontbig, moves)
            playing =  playStopButton(screen, clock, playing)
            
        else:
            p1, p2 = move
            
            pos = p1[0]+p1[1]*len(board[0])
            selectedPiece = (numbers[pos][1],numbers[pos][2])

            screen.fill((0,0,0))
            numbers, dealButton = drawBoard(board, screen, fontsmall, fontbig, moves)
            playing =  playStopButton(screen, clock, playing)
                
            pos = p2[1]*len(board[0])+p2[0]
            board, moves = pieceClick(board, moves, p2[0], p2[1], numbers[pos][3])
        
    screen.fill((0,0,0))
    numbers, dealButton = drawBoard(board, screen, fontsmall, fontbig, moves)
    playing =  playStopButton(screen, clock, playing)
    
    return lambda: mainMenu(screen, clock)

def calculateSolution(screen, clock, selectedLevel, selectedAlg):

    screen.fill((0,0,0))

    font1 = pygame.font.SysFont('Arial', 30)
    screen.blit( font1.render("Generating solution...", False, (200,200,255)) ,(25, 200))
    pygame.display.update()
    
    board, moves = initialState(selectedLevel)

    maxDepth = 25
    
    if selectedAlg == "BFS":
        solution, time_s = timeToRun(lambda : BFS(board), 1)
    elif selectedAlg == "DFS":
        solution, time_s = timeToRun(lambda : DFS(board,shouldDealOnlyFirst=True), 1)
    elif selectedAlg == "IDEP":
        solution, time_s = timeToRun(lambda : IDDFS(board, maxDepth), 1)
    elif selectedAlg == "GREEDY":
        solution, time_s = timeToRun(lambda : greedy(board), 1)
    elif selectedAlg == "A*":
        solution, time_s = timeToRun(lambda : aStar(board), 1)

    print("Solution generated in: "+str(time_s)+" seconds")
    
    sleep(0.5)

    return lambda: showSolution(screen, clock, board, moves, solution)

    

def solveMenu(screen, clock):
    selectedLevel = 0
    selectedAlg = "BFS"
    while True:
        screen.fill((0,0,0))
        font1 = pygame.font.SysFont('Arial', 30)
        font2 = pygame.font.SysFont('Arial bold', 30)
        font3 = pygame.font.SysFont('Arial bold', 20)
        font4 = pygame.font.SysFont('Arial', 40)
        screen.blit( font1.render("Level:", False, (200,200,255)) ,(20, 20))

        levels = []
        for i in range(7):
            lvl = pygame.draw.rect(screen, (210,210,0) if selectedLevel == i else (210,210,210), pygame.Rect(20+35*(i%7), 60+35*(i//7), 30, 30))
            levels.append((lvl, i))
            screen.blit( font2.render(str(i), False, (0,0, 0)) ,(29+35*(i%8), 65+35*(i//8)))

        screen.blit( font1.render("Algorithm:", False, (200,200,255)) ,(20, 200))
        BFS_button = pygame.draw.rect(screen, (210,210,0) if selectedAlg == "BFS" else (210,210,210), pygame.Rect(70, 245, 150, 30))
        screen.blit( font2.render("BFS", False, (0,0, 0)) ,(130, 250))
        DFS_button = pygame.draw.rect(screen, (210,210,0) if selectedAlg == "DFS" else (210,210,210), pygame.Rect(70, 245+35, 150, 30))
        screen.blit( font2.render("DFS", False, (0,0, 0)) ,(130, 250+35))
        IDEP_button = pygame.draw.rect(screen, (210,210,0) if selectedAlg == "IDEP" else (210,210,210), pygame.Rect(70, 245+35*2, 150, 30))
        screen.blit( font3.render("Iterative Deepening", False, (0,0, 0)) ,(85, 250+35*2))
        GREEDY_button = pygame.draw.rect(screen, (210,210,0) if selectedAlg == "GREEDY" else (210,210,210), pygame.Rect(70, 245+35*3, 150, 30))
        screen.blit( font3.render("Greedy Search", False, (0,0, 0)) ,(100, 250+35*3))
        ASTAR_button = pygame.draw.rect(screen, (210,210,0) if selectedAlg == "A*" else (210,210,210), pygame.Rect(70, 245+35*4, 150, 30))
        screen.blit( font2.render("A*", False, (0,0, 0)) ,(140, 250+35*4))

        solve_button = pygame.draw.rect(screen, (210,210,210), pygame.Rect(60, 500, 170, 50))
        screen.blit( font4.render("SOLVE", False, (0,0, 0)) ,(90, 500))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()

                for btn, i in levels:
                    if btn.collidepoint(mousePos):
                        selectedLevel = i
                
                if BFS_button.collidepoint(mousePos):
                    selectedAlg = "BFS"
                elif DFS_button.collidepoint(mousePos):
                    selectedAlg = "DFS"
                elif IDEP_button.collidepoint(mousePos):
                    selectedAlg = "IDEP"
                elif GREEDY_button.collidepoint(mousePos):
                    selectedAlg = "GREEDY"
                elif ASTAR_button.collidepoint(mousePos):
                    selectedAlg = "A*"
                elif solve_button.collidepoint(mousePos):
                    return lambda: calculateSolution(screen,clock, selectedLevel, selectedAlg)
        
        pygame.display.update()
        clock.tick(60) 


def howToPlayMenu(screen, clock):
    return False

def mainMenu(screen, clock):
    screen.fill((0,0,0))
    while True:

        fontbig = pygame.font.SysFont('Bauhaus 93', 50)
        fontButton = pygame.font.SysFont('Arial bold', 50)
        fontButton2 = pygame.font.SysFont('Arial bold', 34)
        screen.blit( fontbig.render("Tenpair", False, (200,200,255)) ,(60, 50))

        play_button =      pygame.draw.rect(screen, (210,210,210), pygame.Rect(60, 150, 170, 50))
        screen.blit( fontButton.render("PLAY", False, (0,0, 0)) ,(100, 160))
        solve_button =     pygame.draw.rect(screen, (210,210,210), pygame.Rect(60, 210, 170, 50))
        screen.blit( fontButton.render("SOLVE", False, (0,0, 0)) ,(90, 220))
        #howtoplay_button = pygame.draw.rect(screen, (210,210,210), pygame.Rect(60, 270, 170, 50))
        #screen.blit( fontButton2.render("HOW TO PLAY", False, (0,0, 0)) ,(65, 285))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if play_button.collidepoint(mousePos):
                    return lambda: humanPlayer(screen, clock)
                if solve_button.collidepoint(mousePos):
                    return lambda: solveMenu(screen, clock)
                #if howtoplay_button.collidepoint(mousePos):
                 #   return lambda: howToPlayMenu(screen, clock)
        
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
        nextScreen = nextScreen()
        
    pygame.quit()


if __name__ == "__main__":
    main()
