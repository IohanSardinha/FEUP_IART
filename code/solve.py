import sys
from ai import *
from tenpair import *
from time import time
from bfs import BFS
from dfs import DFS
from itdep import IDDFS
from astar import aStar
from greedy import greedy

def main(argv):
    maxDepth = -1
    if len(argv) == 0:
        level = int(input("Level[0-6]: "))
        alg = input("Algorithm[BFS, DFS, IDEP, Greedy, A*]: ")
        if alg == 'IDEP':
            maxDepth = int(input("Max depth: "))

    elif len(argv) == 1:
        level = int(argv[0])
        alg = input("Algorithm[BFS, DFS, IDEP, Greedy, A*]: ")
        if alg == 'IDEP':
            maxDepth = int(input("Max depth: "))
            
    elif len(argv) == 2:
        level = int(argv[0])
        alg = argv[1]

    elif len(argv) == 3:
        level = int(argv[0])
        alg = argv[1]
        maxDepth = int(argv[2])

    else:
        print("Wrong number of arguments!")
        print("Usage: python solve.py [level] [algorithm [maxDepth]]")
        return

    if level < 0 or level > 6:
        print("Bad level number, must be between 0 and 6!")
        return

    try:
        board, moves = initialState(level)
        moves = []
        if alg == "BFS":
            moves, time_s = timeToRun(lambda : BFS(board), 1)
        elif alg == "DFS":
            moves, time_s = timeToRun(lambda : DFS(board), 1)
        elif alg == "IDEP":
            moves, time_s = timeToRun(lambda : IDDFS(board, maxDepth), 1)
        elif alg == "GREEDY":
            moves, time_s = timeToRun(lambda : greedy(board), 1)
        elif alg == "A*":
            moves, time_s = timeToRun(lambda : aStar(board), 1)
        else:
            print("Bad algorithm, must be BFS, DFS, IDEP or A*")
            return

        print(alg + " solution solved in " + str(time_s) + " seconds")
        print("Solution:")
        for move in moves:
            print(move)

    except:
        print("Something went wrong!")



if __name__ == '__main__':
    main(sys.argv[1:])
