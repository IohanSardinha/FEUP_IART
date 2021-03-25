from tenpair import *
from time import time
from os import system
from heapq import *

class Node(object):
    def __init__(self, data):
        self.data = data
        self.edges = []
        self.parents = []

    def add_edge(self, obj):
        self.edges.append(obj)

class Edge(object):
    def __init__(self, data, fromNode, toNode):
        self.data = data
        toNode.parents.append(self)
        self.fromNode = fromNode
        self.toNode = toNode
    
class InformedNode(object):
    def __init__(self, data, cost, estimation):
        self.data = data
        self.edges = []
        self.parents = []
        self.cost = cost
        self.estimation = estimation
        
    def add_edge(self, obj):
        self.edges.append(obj)
    
    def __lt__(self, other):
        if (self.cost + self.estimation < other.cost + other.estimation):
            return True
        else:
            return False

'''class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self'''

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

def DFSNode(node, depth):
    
    if win(node.data):
        return node
    
    allBoards = getAllBoards(node.data)
    
    if len(allBoards) == 0:
        return False
    
    for move, board in allBoards:
        child = Node(board)
        edge = Edge(move, node, child)
        node.add_edge(edge)
        
        if not depth == 1:
            retChild = DFSNode(child, depth-1)
        else:
            retChild = False
        
        if not retChild == False:
            return retChild
        
    return False

def DFS(board, depth):
    node = Node(board)
    return DFSNode(node, depth)

def IDDFSNode(node, depth):
    
    if depth == 0:
        if win(node.data):
            return node
        else:
            return False
    
    allBoards = getAllBoards(node.data)
    
    if len(allBoards) == 0:
        return False
    
    for move, board in allBoards:
        child = Node(board)
        edge = Edge(move, node, child)
        node.add_edge(edge)
        
        retChild = IDDFSNode(child, depth-1)
        
        if not retChild == False:
            return retChild
        
    return False

def IDDFS(board, maxDepth):
    node = Node(board)
    for i in range(0, maxDepth):
        print("Calculating depth " + str(i))
        result = IDDFSNode(node, i)
        if not result == False:
            return result

def aStar(board, depth):
    
    root = InformedNode(board, 0, countElements(board)/2)

    boards = getAllBoards(board)
    newBoard = [l[:] for l in board]
    boards.append(("deal", deal(newBoard)))

    queue = []

    visited = []
    skip = 0
    
    for move, b in boards:
        node = InformedNode(b, root.cost + (0 if move == "deal" else 1), countElements(b)//2)
        edge = Edge(move, root, node)

        root.add_edge(edge)
        heappush(queue, node)

    while queue:
        node = heappop(queue)

        # showBoard(node.data, node.cost)
        # print("cost: " + str(node.cost) + " estimation: " + str(node.estimation))
        
        visited.append(str(node.data))

        if win(node.data):
            print("win")
            return node

        for move, b in getAllBoards(node.data):                
            
            if str(b) in visited:                    
                skip += 1
                continue
            
            child = InformedNode(b, node.cost + (0 if move == "deal" else 1), countElements(b)//2)
            edge = Edge(move, node, child)
            node.add_edge(edge)
            heappush(queue, child)

def countElements(board):
    count = 0
    for line in board:
        for value in line:
            if not value == 0:
                count += 1

    return count

def elementsLeft(board):
    return (len(board)*len(board[0])) - countElements(board)

def getAllMovesInBoard(board):
    visited = []
    for i, line in enumerate(board):
        for j, number in enumerate(line):
            for move in getPossibleMoves((j,i), board):
                if ((j,i),move) in visited:
                    continue
                visited.append((move,(j,i)))
                
    return visited

def getAllBoards(board):
    boards = []
    for move,(j,i) in getAllMovesInBoard(board):
        newBoard = [l[:] for l in board]
        newBoard = removePiece((j,i), move, newBoard)
        boards.append((((j,i),move),newBoard))

    newBoard = [l[:] for l in board]
    boards.append((("deal"), deal(newBoard)))
    return boards
    
def BFS(board):

    root = Node(board)

    boards = getAllBoards(board)
    newBoard = [l[:] for l in board]
    boards.append(("deal", deal(newBoard)))

    queue = []

    visited = []
    skip = 0
    
    for move, b in boards:
        node = Node(b)
        edge = Edge(move, root, node)

        root.add_edge(edge)
        queue.append(node)

    while queue:
        node = queue.pop(0)
        
        visited.append(str(node.data))

        if win(node.data):
            print("win")
            return node

        for move, b in getAllBoards(node.data):                
            
            if str(b) in visited:                    
                skip += 1
                continue
            #print(move)
            
            child = Node(b)
            edge = Edge(move, node, child)
            node.add_edge(edge)
            queue.append(child)
            visited.append(str(b))
    
    

board, moves = initialState(6)

start = time()

result = aStar(board, 25)

end = time()

path = []
while result.parents != []:
    path.append(result.parents[0].data)
    result = result.parents[0].fromNode
for move in path[::-1]:
    print(move[0][::-1], move[1][::-1])
    
print("Done in: " + str(end - start) + " seconds")
