from ai import *

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
        child = Node(board, node.cost + int(move != "( deal )"))
        edge = Edge(move, node, child)
        node.add_edge(edge)
        
        retChild = IDDFSNode(child, depth-1)
        
        if not retChild == False:
            return retChild
        
    return False

def IDDFS(board, maxDepth):
    node = Node(board, 0)
    for i in range(0, maxDepth):
        result = IDDFSNode(node, i)
        if not result == False:
            return result
