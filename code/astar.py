from ai import *

def aStar(board):
    
    root = Node(board, 0, countElements(board)/2)

    boards = getAllBoards(board)

    queue = []

    visited = []
    skip = 0
    
    for move, b in boards:
        node = Node(b, root.cost + (0 if move == "deal" else 1), countElements(b)//2)
        edge = Edge(move, root, node)

        root.add_edge(edge)
        heappush(queue, node)

    while queue:
        node = heappop(queue)
        
        visited.append(str(node.data))

        if win(node.data):
            return node

        for move, b in getAllBoards(node.data):                
            
            if str(b) in visited:                    
                skip += 1
                continue
            
            child = Node(b, node.cost + (0 if move == "deal" else 1), countElements(b)//2)
            edge = Edge(move, node, child)
            node.add_edge(edge)
            heappush(queue, child)
