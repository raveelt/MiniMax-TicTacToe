EMPTY = "y"
'''
mylist =  [ [EMPTY, "X", EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

mytuple = (1,1)

anotherlist = list(mytuple)

print(mylist[anotherlist[0]][anotherlist[1]])

print(mylist[1][1])



def player(mylist):

    emptyCount = 0

    for i in mylist:
        for j in i:
            if j == EMPTY:
                 emptyCount +=1

    if emptyCount % 2 == 0:
        print("O")
    else:
        print("X")


player(mylist)
'''
X = "X"
O = "O"

board =  [ [EMPTY, X , EMPTY],
            [O, EMPTY, O],
            [O, EMPTY, O]]

if board[0][0] == board[0][1] == board[0][2]:
    if board[0][0] == X or board[0][0] == O:
        print(board[0][0])

if board[1][0] == board[1][1] == board[1][2]:
    if board[1][0] == X or board[1][0] == O:
        print(board[1][0])

if board[2][0] == board[2][1] == board[2][2]:
    if board[2][0] == X or board[2][0] == O:
        print(board[2][0])
else:
    print('true')





'''    
    
    def winner(board):
        """
        Returns the winner of the game, if there is one.
        """
    #not sure if this works
    
      #rows
        if board[0][0] == board[0][1] == board[0][2]:
            if board[0][0] == X or board[0][0] == O:
                return board[0][0]
    
        if board[1][0] == board[1][1] == board[1][2]:
            if board[1][0] == X or board[1][0] == O:
                return board[1][0]
    
        if board[2][0] == board[2][1] == board[2][2]:
            if board[2][0] == X or board[2][0] == O:
                return board[2][0]
    #column
    
        if board[0][0] == board[1][0] == board[2][0]:
            if board[0][0] == X or board[0][0] == O:
                return board[0][0]
        if board[0][1] == board[1][1] == board[2][1]:
            if board[0][1] == X or board[0][1] == O:
                return board[0][1]
        if board[0][2] == board[1][2] == board[2][2]:
            if board[0][2] == X or board[0][2] == O:
                return board[0][2]
    
    #diagonal
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == X or board[0][0] == O:
                return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == X or board[0][2] == O:
                return board[0][2]
    #no winners
        else:
            return None
    
        raise NotImplementedError
    
 '''

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

  #all winners including the middle position [1][1]

    if board[1][1] == X or board[1][1] == O:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        if board[1][0] == board[1][1] == board[1][2]:
            return board[1][0]
        if board[0][1] == board[1][1] == board[2][1]:
            return board[0][1]

#winners from top left position [0][0]

    if board[0][0] == X or board[0][0] == O:
        if board[0][0] == board[0][1] == board[0][2]:
            return board[0][0]
        if board[0][0] == board[1][0] == board[2][0]:
            return board[0][0]

#winners from bottom right position [2][2]

    if board[2][2] == X or board[2][2] == O:
        if board[2][0] == board[2][1] == board[2][2]:
            return board[2][0]
        if board[0][2] == board[1][2] == board[2][2]:
            return board[0][2]

# no winners
    return None


winner(board)






