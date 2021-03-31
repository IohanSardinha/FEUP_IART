from ai import *

heuristic = lambda board: countElements(board)//2

heuristic2 = lambda board: countUniqueElements(board)

heuristic3 = lambda board: 2*countElements(board) - len(getAllBoards(board))+1

def countUniqueElements(board):
  li = []
  for line in board:
    for el in set(line):
      li.append(el)

  return len(set(li))
