from tkinter import *
from tenpair import *

piecePosition = (-1,-1)

def clearButtons(buttons):
    for line in buttons:
        for button in line:
            button.grid_forget()



def buttonClick(position, button):
    global piecePosition

    if position == piecePosition:
        position = (-1,-1)
        button.configure(bg = "gray")
    elif not piecePosition == (-1,-1):
        position = piecePosition
        button.configure(bg = "yellow")
    else:
        print(piecePosition,position)

def displayBoard(board):
    buttons = [[0]*len(board[0]) for _ in board]
    for i, line in enumerate(board):
        for j, value in enumerate(line):
            buttons[i][j] = Button( text = (" " if value == 0 else value),
                                    command = lambda : buttonClick((i,j),self))
            buttons[i][j].grid(row = i, column = j, padx = 2, pady = 2)    
    Button(text = "deal").grid(column = len(board[0]), pady=5)
    return buttons

board, moves = initialState()
screen = Tk()

displayBoard(board)

