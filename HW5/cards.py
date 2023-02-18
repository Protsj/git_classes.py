import random

ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

suits = ['\u2660', #spades
         '\u2665', #hearts
         '\u2666', #diamonds
         '\u2663'] #clubs

class CardGame():

    def __init__(self):
        self.crank = random.choice(ranks)
        self.csuit = random.choice(suits)

    def __repr__(self):
        return f"{self.crank}{self.csuit}"

    def card_guess():
        card = CardGame()
        print("\nChoosing a card...\n")
        guess = input(f"Your card is {card}. Did i guess?: ")
        while True:
            if guess == "Yes":
                print("Thank you, i knew i can guess something :)")
                break
            elif guess == "No":
                print("Sorry... I'll try my best nex time!")
                break
            else:
                guess = input("Can you please type 'Yes'/'No': ")

    def fortune_tell():
        card = CardGame()
        print("\nGiving you some time ti think of a question...\n")
        question = input("Type your question and i will tell you the truth: ")

        if card.crank == (10 or str) and card.csuit == '\u2660':
            print (f"It is {card.csuit}{card.crank}{card.csuit}. It says: Yes!")
        elif card.crank != (10 or str) and card.csuit == '\u2660':
            print(f"It is {card.csuit}{card.crank}{card.csuit}. It says: No...")
        elif card.crank == (10 or str) and card.csuit == '\u2665':
            print(f"It is {card.csuit}{card.crank}{card.csuit}. It says: Possible.")
        elif card.crank != (10 or str) and card.csuit == '\u2665':
            print(f"It is {card.csuit}{card.crank}{card.csuit}. It says: Meh, low chances...")
        elif card.crank == (10 or str) and card.csuit == '\u2666':
            print(f"It is {card.csuit}{card.crank}{card.csuit}. It says: May happen, but something good will happen also!")
        elif card.crank != (10 or str) and card.csuit == '\u2666':
            print(f"It is {card.csuit}{card.crank}{card.csuit}. It says: No. It will be ok tho.")
        elif card.crank == (10 or str) and card.csuit == '\u2663':
            print(f"It is {card.csuit}{card.crank}{card.csuit}. It says: Most likely, yes!")
        elif card.crank != (10 or str) and card.csuit == '\u2663':
            print(f"It is {card.csuit}{card.crank}{card.csuit}. It says: Surely not, it will be so bad...") 

if __name__ == '__main__':
    CardGame()