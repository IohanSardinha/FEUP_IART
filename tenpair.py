def showBoard(board, moves):
    print("      0 1 2 3 4 5 6 7 8\n")
    print("-"*24)
    for i, line in enumerate(board):
        print(str(i)+":   ", end="")
        
        for value in line:
            print("|"+(" " if value == 0 else str(value)), end="")
        print("|")
        print("-"*24)
    print("Moves: "+str(moves))

def win(board):
    for line in board:
        if not sum(line) == 0:
            return False
    return True

def validRemove(p1, p2, board):
    x = 0
    y = 1

    if p1[x] >= len(board[0]) or p2[x] >= len(board[0]) or p1[y] >= len(board) or p2[y] > len(board):
        return False
    
    if board[p1[y]][p1[x]] + board[p2[y]][p2[x]] == 10 or board[p1[y]][p1[x]] == board[p2[y]][p2[x]]:

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
        if p1[y] == p2[y] + 1 and p1[x] == p2[x]: 
           return True;

        #[2]
        #[ ]
        #...
        #[1]
        if p1[x] == p2[x] and sum([board[i][p1[x]] for i in range(p1[y]+1,p2[y])]) == 0:
            return True
           
        #[1]
        #[ ]
        #...
        #[2]
        if p1[x] == p2[x] and sum([board[i][p2[x]] for i in range(p2[y]+1,p1[y])]) == 0:
            return True

        #[1][ ][ ]..[ ]
        #[ ]...[2]
        for i in range(p1[y],p2[y]+1):
            start = p1[x]+1 if i == p1[y] else 0
            end = p2[x] if i == p2[y] else len(board[0])
            for j in range(start,end):
                if not board[i][j] == 0:
                    return False
        
        
        #[2][ ][ ]..[ ]
        #[ ]...[1]
        for i in range(p2[y],p1[y]+1):
            start = p2[x]+1 if i == p2[y] else 0
            end = p1[x] if i == p1[y] else len(board[0])
            for j in range(start,end):
                if not board[i][j] == 0:
                    return False                    

        return True
    return False


def deal(board):
    inserti, insertj = (0,0)
    for i in range(len(board)-1, -1, -1):
        brk = False
        for j in range(len(board[0])-1, -1, -1):
            if not board[i][j] == 0:
                inserti, insertj = (i,j+1)
                brk = True
                break
        if brk:
            break

    dealValues = []
    for line in board:
        dealValues += [value for value in line if not value == 0]

    for value in dealValues:
        
        if insertj >= len(board[0]):
            insertj = 0
            inserti += 1

        if inserti >= len(board):
            board.append([0]*len(board[0]))

        board[inserti][insertj] = value

        insertj += 1

    return board
    

def removePiece(p1, p2, board):
    
    board[p1[1]][p1[0]] = 0
    board[p2[1]][p2[0]] = 0

    board = list(filter(lambda x: not sum(x) == 0, board))
    
    return board

def initialState():
    return [[1,2,3,4,5,6,7,8,9],  
            [1,1,1,2,1,3,1,4,1],
            [5,1,6,1,7,1,8,1,9]], 0

def main():
    board,moves = initialState()

    while True:
        showBoard(board, moves)
        input1 = input("> ")
        if input1.lower()  == "deal":
            board = deal(board)
            continue
        
        input2 = input("> ")
        p1 = list(map(int,input1.split(" ")))
        p2 = list(map(int,input2.split(" ")))
        
        if validRemove(p1, p2, board):
            board = removePiece(p1, p2, board)
            moves += 1
            continue
        
        print("Invalid move!\n\n")

if __name__ == "__main__":
    main()


