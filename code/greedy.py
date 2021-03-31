from ai import *
from heuristics import *

lessthan = lambda left, right: left.estimation < right.estimation

def greedy(board, alg=pairsHeuristic):
    
    root = Node(board, 0, alg(board), lessthan)

    boards = getAllBoards(board)

    queue = []

    visited = []
    skip = 0
    
    for move, b in boards:
        node = Node(b, root.cost + (0 if move == "deal" else 1), alg(b), lessthan)
        edge = Edge(move, root, node)

        root.add_edge(edge)
        heappush(queue, node)

    while queue:
        node = heappop(queue)
        
        visited.append(str(node.data))
        
        print(node.parents[0].data)
        print(node.estimation)

        if win(node.data):
            return node

        allBoards = getAllBoards(node.data)

        for move, b in allBoards:           
            
            if str(b) in visited:                    
                skip += 1
                continue
            
            child = Node(b, node.cost + (0 if move == "deal" else 1), alg(b), lessthan)
            edge = Edge(move, node, child)
            node.add_edge(edge)
            heappush(queue, child)
