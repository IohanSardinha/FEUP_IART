from tenpair import *

class Node(object):
    def __init__(self, data, value):
        self.data = data
        self.value = value
        self.edges = []

    def add_edge(self, obj):
        self.edges.append(obj)

class Edge(object):
    def __init__(self, data, node):
        self.data = data
        self.node = node



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
    count = 0
    for line in board:
        for value in line:
            if not value == 0:
                count += 1

    return count

def elementsLeft(board):
    return (len(board)*len(board[0])) - countElements(board)

def buildTree(board, depth):
    node = Node(board, elementsLeft(board))

    if depth == 0:
        return node

    visited = []
    for i, line in enumerate(board):
        for j, number in enumerate(line):
            for move in getPossibleMoves((j,i), board):

                if ((j,i),move) in visited:
                    continue

                visited.append((move,(j,i)))
                newBoard = [l[:] for l in board]
                newBoard = removePiece((j,i),move, newBoard)
                edge = Edge(1, buildTree(newBoard, depth - 1))
                node.add_edge(edge)

    newBoard = [l[:] for l in board]
    edge = Edge(countElements(newBoard), buildTree(newBoard, depth - 1))
    node.add_edge(edge)

    return node

board, moves = initialState()

buildTree(board, 20)

print("Done")























