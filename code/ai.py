from tenpair import *
from time import time
from os import system
from heapq import *

class Node(object):
    def __init__(self, data, cost=None, estimation=None, alg=None):
        self.data = data
        self.edges = []
        self.parents = []
        self.cost = cost
        self.estimation = estimation
        self.lessthan = alg

    def add_edge(self, obj):
        self.edges.append(obj)


    def __lt__(self, other):
        return self.lessthan(self, other)

class Edge(object):
    def __init__(self, data, fromNode, toNode):
        self.data = data
        toNode.parents.append(self)
        self.fromNode = fromNode
        self.toNode = toNode

def getPossibleMoves(position,board):
    x = 0
    y = 1

    moves = []

    if board[position[y]][position[x]] == 0:
        return moves
    
    if position[y]-1 >=0 and (board[position[y]][position[x]] + board[position[y]-1][position[x]] == 10 or board[position[y]][position[x]] == board[position[y]-1][position[x]]) :
        moves.append((position[x],position[y]-1))

    if position[x]-1 >=0 and (board[position[y]][position[x]] + board[position[y]][position[x]-1] == 10 or board[position[y]][position[x]] == board[position[y]][position[x]-1]):
        moves.append((position[x]-1,position[y]))

    for i in range(position[y]+1, len(board)):
        if not board[i][position[x]] == 0:
            if board[position[y]][position[x]] + board[i][position[x]] == 10 or board[position[y]][position[x]] == board[i][position[x]]:
                moves.append((position[x],i))
            break

    for i in range(position[y], len(board)):
        start = position[x]+1 if i == position[y] else 0
        brk = False
        for j in range(start, len(board[i])):
            if not board[i][j] == 0:
                if board[position[y]][position[x]] + board[i][j] == 10 or board[position[y]][position[x]] == board[i][j]:
                    moves.append((j,i))
                brk = True
                break
        if brk:
            break
            
    return moves

def countElements(board):
    return sum([sum([1 for value in line if not value == 0]) for line in board])

def getAllMovesInBoard(board):
    visited = []
    for i, line in enumerate(board):
        for j, number in enumerate(line):
            for move in getPossibleMoves((j,i), board):
                if ((j,i),move) in visited:
                    continue
                visited.append((move,(j,i)))
                
    return visited

def getAllBoards(board, shouldDeal=True):
    boards = []
    for move,(j,i) in getAllMovesInBoard(board):
        newBoard = [l[:] for l in board]
        newBoard = removePiece((j,i), move, newBoard)
        boards.append((((j,i),move),newBoard))

    if shouldDeal:
        newBoard = [l[:] for l in board]
        boards.append((("( deal )"), deal(newBoard)))
    return boards

def getMoves(node):
    path = []
    while node.parents != []:
        path.append(node.parents[0].data)
        node = node.parents[0].fromNode
    
    return path[::-1]    

def timeToRun(func, n=50):
    times=[]
    for _ in range(n):
        start = time()
        ret = func()
        end = time()
        times.append(end-start)
    return getMoves(ret), (sum(times)/len(times))
