from IPython.display import clear_output
import random

#Function to display board
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

#Function to get player markers
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player1:Choose X or O:').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#Function to mark position on board
def place_marker(board,marker,position):
    board[position]=marker

#Function to check if player with marker mark has won
def win_check(board,mark):

    return ((board[7]==mark and board[8]==mark and board[9]==mark) or #Row1
    (board[4]==mark and board[5]==mark and board[6]==mark) or         #Row2
    (board[1]==mark and board[2]==mark and board[3]==mark) or         #Row3
    (board[7]==mark and board[4]==mark and board[1]==mark) or         #Column1
    (board[8]==mark and board[5]==mark and board[2]==mark) or         #Column2
    (board[9]==mark and board[6]==mark and board[3]==mark) or         #Column3
    (board[7]==mark and board[5]==mark and board[3]==mark) or         #Diagonal1
    (board[9]==mark and board[5]==mark and board[1]==mark))           #Diagonal2

#Function to randomly assign who will start game first
def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

#Function to check if position is empty
def space_check(board,position):
    return board[position] == ' '

#Function to check if board is full
def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full
    return True

#Function to ask for position at which the player wants to put mark
def player_choice(board):

    position = 0
    while position not in list(range(1,10)) or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))

    return position

#Function to ask if player wants to play again
def replay():

    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'

def play_turn(board, player_marker,game_on):
    #Show the board
    display_board(board)
    #Choose a position
    position = player_choice(board)
    #Place the marker on the position
    place_marker(board,player_marker,position)
    #Check if they win
    if win_check(board,player_marker):
        display_board(board)
        print('PLAYER 1 HAS WON!!')
        game_on = False
    else:
        if full_board_check(board):
            display(board)
            print("TIE GAME!")
            game_on = False
    return game_on

#Main function to play
def play():

    print('Welcome to Tic Tac Toe')

    while True:

        board = [' ']*10
        player1_marker,player2_marker = player_input()

        turn = choose_first()
        print(turn + ' will go first')

        play_game = input('Ready to play? y or n? ')

        if play_game == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                turn,game_on='Player 2',play_turn(board,player1_marker,game_on)
            else:
                turn,game_on='Player 1',play_turn(board,player2_marker,game_on)

        if not replay():
             break

if __name__=='__main__':
    play()
