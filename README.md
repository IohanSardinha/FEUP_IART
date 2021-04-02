# TENPAIR

Tenpair is a puzzle game where you  are presented with a grid of numbers and your goal is to remove all of them by selecting pairs of pieces that either have the same number  on them or their values add up to ten. In order to do so the two pieces must be adjacent, not considering empty spaces, in four directions: up, down, left and right; or not have other numbers between them when analyzing the table left to right and top to bottom. It's also always possible to deal, that means that the remaining pieces in the board are inserted beginning at a new line at the end of the board, in the order they're read, from left to right, top to bottom. 

In this project there were implemented 5 new boards other then the original. It's possible to play the game in a terminal or with a graphic interface, as well as using the implemented algorithms to solve given boards.

## Prerequisites

The game was developed using [Python](https://www.python.org) 3 which is necessary to be installed in the computer to be able to play

The graphic interface was developed using [Pygame](https://www.pygame.org/) library that can be installed by running

```bash
python3 -m pip install -U pygame --user
```

The data analysis for the different implemented algorithms was done using [IPython](https://ipython.org) and matplotlib

## Play the game on a terminal

To play the game in any terminal just do

```bash
python3 tenpair.py
```

## Play the game with the graphic interface

Pygame must be installed in order to play the game with the graphics interface, and to play just do

 

```bash
python3 graphics.py
```

## Generating solutions using search algorithms

The search algorithms are implemented each one in a single file

| Algorithm | File |
|--|--|
| Breadth-first Search | [bfs.py](code/bfs.py) |
| Depth-first Search | [dfs.py](code/dfs.py) |
| Iterative Deepening | [idep.py](code/idep.py) |
| Greedy Search | [greedy.py](code/greedy.py) |
| A* | [astar.py](code/astar.py) |

## Using graphic interface

The same graphical interface that can be used to play the game can be used to solve and watch the solution for nine available levels, running:
```bash
python3 graphics.py
```

### Using solver

The solution for a game can be found by using [solve.py](code/solve.py)

```bash
python3 solve.py [level] [algorithm [maxDepth] ]
```

- level is a number from 0 to 8
- algorithm is a string that can be BFS, DFS, IDEP or A*
- maxDepth is the maximum depth to be used by the iterative deepening algorithm

### Using python shell

Using the python shell the algorithms can be used not only to solve the 7 levels but any custom board.

First by importing [ai.py](code/ai.py) and [tenpair.py](code/tenpair.py) which contains the game logic and the functions for solving

```python
>>> from tenpair import *
>>> from ai import *
```

The importing the desired algorithm, for exemple A*

```python
>>> from astar import aStar
```

Then to solve both the imported method, in this exemple aStar, or the timeToRun wich will return the time that it took to compute the solution, can be used

```python
>>> board = [[1,2,1],[3,3,3],[1,2,1]]
>>> moves, run_time = timeToRun(lambda: aStar(board), 1)
>>> for move in moves:
	print(move)
```

## Data Analisys

For the 7 pre-ready levels of the game some data was collected and analised by plotting some graphs using matplotlib and the results can be observed in [dataAnalisys.ipynb](code/dataAnalisys.ipynb)
