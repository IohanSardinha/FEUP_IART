from ai import *

def DFSNode(node, depth = -1, shouldDealOnlyFirst=False, isFirst=True):
    
    if win(node.data):
        return node

    allBoards = getAllBoards(node.data, (False if (shouldDealOnlyFirst and not isFirst) else True))
    
    if len(allBoards) == 0:
        return False
    
    for move, board in allBoards:
        child = Node(board)
        edge = Edge(move, node, child)
        node.add_edge(edge)
        
        if not depth == 1:
            retChild = DFSNode(child, depth-1, shouldDealOnlyFirst, False)
        else:
            retChild = False
        
        if not retChild == False:
            return retChild
        
        
        
        if not retChild == False:
            return retChild
        
    return False

def DFS(board, depth=-1, shouldDealOnlyFirst=False):
    node = Node(board)
    return DFSNode(node, depth, shouldDealOnlyFirst)
