import random, itertools

class CardDeck():
    small_deck = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    classic_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['\u2660', #spades
            '\u2665', #hearts
            '\u2666', #diamonds
            '\u2663'] #clubs
    shuffle_cards = False

    def shuffle(self):
        random.shuffle(self.cards)
        self.shuffle_cards = True
        return self.cards

    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, card_index):
        try:
            if isinstance(card_index, int):
                return self.cards[card_index]
            elif isinstance(card_index, slice):
                return self.cards[card_index.start:card_index.stop:card_index.step or 1]
        except IndexError:
            raise IndexError(f'Sorry, you can not get {card_index} euros :( ...')

    def __add__(self, new_cards):
        try:
            if isinstance(new_cards, list):
                self.cards += new_cards
                return self.cards
        except Exception:
            return f'Sorry, something went wrong...'
    
    def __sub__(self, del_cards):
        try:
            if isinstance(del_cards, list):
                for card in del_cards:
                    self.cards.remove(card)
            else:
                self.cards.remove(del_cards)
            return self.cards
        except Exception:
            return f'Sorry, something went wrong...'

    def __contains__(self, card):
        return card in self.cards
    
    def __eq__(self, card_deck):
        if self.cards == card_deck.cards:
            return True
        return False
    
    def __bool__(self):
        if self.shuffle_cards == True and bool(self.cards):
            return True
        return False

class SmallDeck(CardDeck):
    def __init__(self):
        self.cards = []
        self.new_deck()

    def new_deck(self):
        self.cards = list(itertools.product(CardDeck.small_deck, CardDeck.suits))
    
    def __str__(self):
        return f'Small deck cards: {self.cards}'
    
class ClassicDeck(CardDeck):
    def __init__(self):
        self.cards = []
        self.new_deck()

    def new_deck(self):
        self.cards = list(itertools.product(CardDeck.classic_deck, CardDeck.suits))
    
    def __str__(self):
        return f'Classic deck cards: {self.cards}'

if __name__ == '__main__':
    deck_one = SmallDeck()
    deck_two = ClassicDeck()

    card = [(7, '\u2665')] #hearts
    cards = [('J', '\u2663'),(9, '\u2666')] #clubs & diamonds

    #deck_one/deck_two are lists with items(key/value - our example has suits and ranks), 
    # so we can just go through each item in this list using different loops, because they are iterable already.

    '''Shuffle the deck'''
    #print(deck_one)
    #deck_one.shuffle()
    #print(deck_one)

    #print(deck_two)
    #deck_two.shuffle()
    #print(deck_two)

    '''__len__ func check'''
    #print(len(deck_one)) #returns len of SmallDeck = 36
    #print(len(deck_two)) #returns len of ClassicDeck = 52

    '''__getitem__ func check'''
    #print(deck_two[abc]) #raises index error
    #print(deck_one[1]) #returns card with [1] index
    #print(deck_one[1:6]) #returns list of cards with indexes from 1 to 6  
    #print(deck_two[6:13:2]) #returns list of cards with indexes from 6 to 13 with a step of 2 indexes  

    '''__add__ func check'''
    #deck_one += cards #adding the list of cards to the deck
    #print(deck_one) #returns deck_one with added cards 
    #print(len(deck_one)) #returns len of the modified deck

    '''__sub__ func check'''
    #deck_two -= card #removing the card from the deck
    #print(deck_two) #returns deck_two with one card removed
    #print(len(deck_two)) #returns len of the modified deck

    '''__contains__ func check'''
    #deck_two -= cards #removing the card from the 2nd deck
    #print((9, '\u2666') in deck_two) #returns False
    #deck_one -= card #removing another the card from the 1st deck
    #print((7, '\u2665') in deck_one) #returns False

    '''__eq__ func ckeck'''
    #test_deck = ClassicDeck()
    #print(deck_one == test_deck) #returns False (different decks)
    #print(deck_two == test_deck) #returns True (decks are the same)
    
    '''__bool__ func check'''
    #deck_one -= deck_one #removing all the cards from the 1st deck
    #print(bool(deck_one)) #returns True
    #print(bool(deck_two)) #returns False
    #deck_two.shuffle() #shuffle all the cards in the 2nd deck
    #print(bool(deck_two)) #returns True