# TENPAIR

## Representation

* List of sublists of numbers to represent the board
  * Each sublist represents a row
  * 0 indicates empty space
* Number of moves

## Initial State

```python
[[1,2,3,4,5,6,7,8,9],
[1,1,1,2,1,3,1,4,1],
[5,1,6,1,7,1,8,1,9]]

moves = 0
```

## Operators

* Remove
  * Pre-conditions
    * The pairs can be removed if they are in the same column with no other numbers between them, or if they have only empty places between them when scanning the grid from left to right, top to bottom
    * Piece values add up to 10 or piece values are equal
  * Effects
    * Numbers are removed from the board (turn into empty spaces)
    * The number of moves is incremented
  * Cost
    * 1
* Deal
  * Pre-conditions
    * None
  * Effects
    * The remaining numbers are added, in the same order, in front of the last numbers (with no spaces between them), only adding rows
  * Cost
    * The number of pieces added, divided by 2

## Objective Test

* The board has no numbers (all spaces are empty)
    