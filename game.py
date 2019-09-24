#n = input()
end=False
board=[1,2,3,4,5,6,7,8,9]
win=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

class tictactoe:

    def Game(self):
    #board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #win=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    def Board():
        print(board[0],board[1],board[2])
        print(board[3],board[4],board[5])
        print(board[6],board[7],board[8])
        print()

def player1():
    n = position()
    if board[n] == 'X' or board[n] == 'O':
        print("do not go there")
        player1()
    else:
        board[n] = 'X'

def player2():
    if board[n] == 'X' or board[n] == 'O':
        print("do not go there")
        player2()
    else:
        board[n] = 'O'


def position():
    while True:

        a = input()
        try:
            a = int(a)
            a -= 1
            if a in range(0,9):
                return a
            else:
                print("there is no board")
            print("there is no number")

def board_entry_win():
    count = 0
    for a in win:
        if board[a[0]] == board[a[1]] == board[a[2]] == 'X':
            print("player1 wins")
            return

        if board[a[0]] == board[a[1]] == board[a[2]] == 'O':
            print("player 2 wins")
            return

        for a in range(9):
            if board[a]=='X' or board[a]=='O':
                count+=1

            if count==9:
                print("all spaces are occupied and the game ends")
                return True

    while not end:
        end = board_entry_win()
        if end == True:
            break
        print("player 1 chose to play")
        player1()
        print()
        end = board_entry_win()
        if end == True:
            break
        print("player 2 chose to play")
        player2()
        print()


board_entry_win()


#def win_situation():
 #   if win_situation()

#def input():


Board()