from ai import *

def BFS(board, noRepeat=False, shouldDealOnlyFirst=False):

    root = Node(board, 0)

    boards = getAllBoards(board)
    newBoard = [l[:] for l in board]
    boards.append(("( Deal )", deal(newBoard)))

    queue = []

    if noRepeat:
        visited = []
    
    for move, b in boards:
        node = Node(b, root.cost + (0 if move == "( deal )" else 1))
        edge = Edge(move, root, node)
        queue.append(node)

    while queue:
        node = queue.pop(0)

        if noRepeat:       
            visited.append(str(node.data))

        if win(node.data):
            return node

        for move, b in getAllBoards(node.data, not shouldDealOnlyFirst):                
            
            if noRepeat and str(b) in visited:                    
                continue
            
            child = Node(b, node.cost + (0 if move == "( deal )" else 1))
            edge = Edge(move, node, child)
            node.add_edge(edge)
            queue.append(child)

            if noRepeat:
                visited.append(str(b))
