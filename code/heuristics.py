from ai import *

heuristic = lambda board: countElements(board)//2

pairsHeuristic = lambda board: countElements(board)/countPairs(board)

def countPairs(board):
  pairs = 0
  c = 0

  for i in range (1, 6):
    for row in board:
      for cell in row:
        if cell == i or cell == 10-i:
          pairs += 1
      
    c += pairs/2
    pairs = 0

  return c if c != 0 else 0.000001