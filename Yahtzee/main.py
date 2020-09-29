from Roll import Roll
from Player import Player

def turn(player_name):

    game_list_top = ['aces' , 'twos' , 'threes' , 'fours' , 'fives' , 'sixes']
    game_list_top_values = [1,2,3,4,5,6]

    player = Player(player_name)
    dice1 = Roll()

    for index, item in enumerate(game_list_top):
        print ('-'*40)
        print (f'rolling for {item}')
        print ('-'*40)

        dice1.roll_dice()
        keep1 = dice1.keep_dice()

        dice1.reroll_dice(keep1)
        keep2 = dice1.keep_dice()

        roll3 = dice1.reroll_dice(keep2)
        dice1.forced_keep(roll3)

        final_roll_collection = dice1.get_kept_dice()

        print (f'final roll collection: {final_roll_collection}')

        top_score = dice1.single_values(final_roll_collection,game_list_top_values[index])

        player.add_rolled(item, top_score)
        player.add_top_score(top_score)

        bottom_score = dice1.get_bottom_score(final_roll_collection)

        player.add_bottom_score(bottom_score)

    player.add_top_bonus()
    player.add_bottom_bonus()
    player.add_total_score()

    player.print_scoreboard()

    return player.get_total_score()

def play():

    while True:

        print('Welcome to Yahtzee')

        player1_name = input("Enter Player 1 Name:")
        player2_name = input("Enter Player 2 Name:")

        play_game = input('Ready to play? y or n? ')

        if play_game == 'y':
            game_on = True
        else:
            game_on = False

        if game_on:

            player1_score = turn(player1_name)
            player2_score = turn(player2_name)

            if player1_score > player2_score:
                print(player1_name+' Wins!')
            elif player2_score > player1_score:
                print(player2_name+' Wins!')
            else:
                print("It's a tie.")

        choice = input("Play again? Enter Yes or No")
        if not choice == 'Yes':
            break

if __name__=='__main__':
    play()
