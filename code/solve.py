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
        level = int(input("Level[0-"+str(len(LEVELS())-1)+"]: "))
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

    if level < 0 or level >= len(LEVELS()):
        print("Bad level number, must be between 0 and "+str(len(LEVELS())-1)+"!")
        return

    board, moves = initialState(level)
    moves = []
    if alg == "BFS":
        moves, cost, time_s = timeToRun(lambda : BFS(board), 1)
    elif alg == "DFS":
        moves, cost, time_s = timeToRun(lambda : DFS(board), 1)
    elif alg == "IDEP":
        moves, cost, time_s = timeToRun(lambda : IDDFS(board, maxDepth+1), 1)
    elif alg == "GREEDY":
        moves, cost, time_s = timeToRun(lambda : greedy(board), 1)
    elif alg == "A*":
        moves, cost, time_s = timeToRun(lambda : aStar(board), 1)
    else:
        print("Bad algorithm, must be BFS, DFS, IDEP or A*")
        return

    print(alg + " found a "+str(cost)+" cost solution in " + str(time_s) + " seconds")
    print("Solution:")
    for move in moves:
        print(move)



if __name__ == '__main__':
    while True:
        main(sys.argv[1:])
