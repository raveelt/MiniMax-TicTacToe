"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    emptyCount = 0

    for i in board:
        for j in i:
            if j == EMPTY:
                 emptyCount +=1

    if emptyCount % 2 == 0:
        return O
    else:
        return X


#needs to return x first then o then x then o until game over

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    mylist = []

    x = -1
    y = -1
    for i in board:
        x += 1
        for j in i:
            if y < 2:
                y += 1
            else:
                y = 0

            if j == EMPTY:
                mylist.append((x,y))

    return mylist



    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)

    listaction = list(action)

    try:
        if newboard[listaction[0]][listaction[1]] == X or newboard[listaction[0]][listaction[1]] == O:
            raise ValueError('Move not possible')

    except ValueError:
        pass

    else:
        newboard[listaction[0]][listaction[1]] = player(board)

    return newboard

    raise NotImplementedError


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

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    elif winner(board) == O:
        return True
    else:
        emptyCount = 0

        for i in board:
            for j in i:
                if j == EMPTY:
                    emptyCount += 1

        if emptyCount == 0:
            return True
        else:
            return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) == None:
        return 0


    raise NotImplementedError





def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimalactionX = ()
    optimalactionO = ()

    boardturn = 0


    for i in board:
        for j in i:
            if j == EMPTY:
                 boardturn +=1



    def maxvalue(board):

        nonlocal optimalactionX
        nonlocal boardturn

        if terminal(board):
            return utility(board)

        v0 = -math.inf

        for action in actions(board):

            newboardturn = 1
            for i in result(board, action):
                for j in i:
                    if j == EMPTY:
                        newboardturn += 1


            v = max(v0, minvalue(result(board, action)))

            if v0 < v:
                if newboardturn == boardturn:
                    optimalactionX = action

                v0 = v
        return v0

    def minvalue(board):

        nonlocal optimalactionO
        nonlocal boardturn

        if terminal(board):
            return utility(board)

        v0 = math.inf

        for action in actions(board):

            newboardturn = 1
            for i in result(board, action):
                for j in i:
                    if j ==EMPTY:
                        newboardturn += 1


            v = min(v0, maxvalue(result(board, action)))
            if v0 > v:
                if newboardturn == boardturn:
                    optimalactionO = action

                v0 = v
        return v0



    if terminal(board):
        return None

    if player(board) == X:
        maxvalue(board)
        return optimalactionX

    if player(board) == O:
        minvalue(board)
        return optimalactionO

    raise NotImplementedError
