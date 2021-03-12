board = [[1,2,3,4,5,6,7,8,9],
         [1,1,1,2,1,3,1,4,1],
         [5,1,6,1,7,1,8,1,9]]

def showBoard(board):
    print("-"*19)
    for line in board:
        for value in line:
            print("|"+(" " if value == 0 else str(value)), end="")
        print("|")
        print("-"*19)

def validRemove(p1, p2, board):
    x = 0
    y = 1

    if p1[x] >= len(board[0]) or p2[x] >= len(board[0]) or p1[y] >= len(board) or p2[y] > len(board):
        return False
    
    if board[p1[y]][p1[x]] + board[p2[y]][p2[x]] == 10 or board[p1[y]][p1[x]] == board[p2[y]][p2[x]]:
        #print(board[p1[1]][p1[0]],board[p2[1]][p2[

        #[1][2]
        if p2[x] == p1[x] + 1 and p2[y] == p1[y]: 
           return True;
        #[2][1]
        if p1[x] == p2[x] + 1 and p1[y] == p2[y]: 
           return True;
        #[1]
        #[2]
        if p2[y] == p1[y] + 1 and p2[x] == p1[x]: 
           return True;

        #[2]
        #[1]
        if p1[y] == p2[y] + 1 and p1[x] == p0[x]: 
           return True;

        #[1][ ][ ]..[2]
        if p1[y] == p2[y] and sum([board[p1[y]][i] for i in range(p1[x]+1,p2[x])]) == 0:
            return True
           
        #[2][ ][ ]..[1]
        if p1[y] == p2[y] and sum([board[p1[y]][i] for i in range(p2[x]+1,p1[x])]) == 0:
            return True

        #[1][ ][ ]..[ ]
        #[ ]...[2]
        if p2[y] == p1[y] + 1 and sum([board[p1[y]][i] for i in range(p1[x]+1,len(board[p1[y]]))]) + sum([board[p2[y]][i] for i in range(0,p2[x])])  == 0:
            return True
        
        #[2][ ][ ]..[ ]
        #[ ]...[1]
        if p2[y] == p1[y] + 1 and sum([board[p2[y]][i] for i in range(p2[x]+1,len(board[p2[y]]))]) + sum([board[p1[y]][i] for i in range(0,p1[x])]) == 0:
            return True
                                

        #[1]
        #[ ]
        #...
        #[2]

        #[2]
        #[ ]
        #...
        #[1]

        
showBoard(board)
print(validRemove((8,0),(8,1), board))
