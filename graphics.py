import pygame
from tenpair import *

selectedPiece = (-1,-1)


def drawBoard(board, screen, fontsmall, fontbig, moves):
    startx, starty = (15,40)

    screen.blit( fontsmall.render("Moves: "+str(moves), False, (255,255,255)) ,(startx, 10))

    numbers = []
    for i, line in enumerate(board):
        for j, value in enumerate(line):
            screen.blit( fontbig.render("0" if value == 0 else str(value), False, (255,255,0) if selectedPiece == (i,j) else (255,255,255)) ,(startx+ j*30 + 8, starty + i*30 - 3))
            number = pygame.draw.rect(screen, (255,255,0) if selectedPiece == (i,j) else (255,255,255), pygame.Rect(startx+ j*30, starty+ i*30, 30,30),1)
            numbers.append((number, i, j, value))
    return numbers

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((300,600))

clock = pygame.time.Clock()

running = True

board, moves = initialState()

fontsmall = pygame.font.SysFont('Arial', 20)
fontbig = pygame.font.SysFont('Arial', 30)

while running:
    screen.fill((0,0,0))

    numbers = drawBoard(board, screen, fontsmall, fontbig, moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for number, i, j ,value in numbers:
                if number.collidepoint(mousePos):
                    print(i,j,value)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
