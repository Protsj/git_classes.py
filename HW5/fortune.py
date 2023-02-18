from cards import CardGame as game

def play_game():
    print(f"Hey, let's play some games! There are two games: 'Guess the card'(1), 'Fortune teller'(2)")
   
    game_num = int(input("Type in a number of the game(1/2): "))
    while True:
        if game_num == 1:
            print("Your choice is 'Guess your card'")
            return game.card_guess()
        elif game_num == 2:
            print("Your choice is 'Fortune tell'")
            return game.fortune_tell()
        else:
            print("You have to choose the game form this list!")
            game_num = int(input("type it here: "))
play_game()