from ai import *

heuristic = lambda board: countElements(board)//2 + (1 if countElements(board)%2 ==0 else 0)

heuristic2 = lambda board: countElements(board)//2
