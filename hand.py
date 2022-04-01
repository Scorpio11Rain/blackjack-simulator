# Author: Runyu Tian
# PID: A15910502
from card import Card

class PlayerHand():
    """
    >>> card_1 = Card("A", "spades")
    >>> card_2 = Card(2, "diamonds")
    >>> card_3 = Card(3, "clubs")
    >>> card_4 = Card(4, "hearts")
    >>> card_5 = Card(5, "spades")
    >>> card_6 = Card("K", "diamonds")
    >>> card_7 = Card("J", "clubs")
    >>> card_8 = Card("Q", "hearts")
    
    >>> p_hand = PlayerHand()
    >>> p_hand.add_card(card_1, card_2)
    >>> p_hand
    (2, diamonds) (A, spades)
    >>> p_hand.add_card(card_3)
    >>> print(p_hand)
    ____
    |2  |
    | ♦ |
    |__2|
    ____
    |3  |
    | ♣ |
    |__3|
    ____
    |A  |
    | ♠ |
    |__A|
    
    >>> p_hand
    (2, diamonds) (3, clubs) (A, spades)

    >>> d_hand = DealerHand()
    >>> d_hand.add_card(card_4)
    >>> d_hand.add_card(card_5, card_6)
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |?  |
    | ? |
    |__?|
    ____
    |?  |
    | ? |
    |__?|
    >>> d_hand
    (4, hearts) (?, ?) (?, ?)
    >>> d_hand.reveal_hand()
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |5  |
    | ♠ |
    |__5|
    ____
    |K  |
    | ♦ |
    |__K|
    >>> d_hand
    (4, hearts) (5, spades) (K, diamonds)
    """
    
    def __init__(self):
        self.cards = []
        
    def add_card(self, *cards):
        """
        Adds cards to the hand, then sorts
        them in ascending order.
        """
        for card in cards:
            assert isinstance(card, Card)
            self.cards.append(card)
        self.sort_hand()

    def get_cards(self):
        return self.cards        

    def __str__(self):
        """
        Returns the string representation of all cards
        in the hand, with each card on a new line.
        """
        s = ""
        for i in range(len(self.cards)):
            if i == 0:
                s += str(self.cards[i]) 
            else:
                s += "\n" + str(self.cards[i])
        return s

    
    def __repr__(self):
        """
        Returns the representation of all cards, with 
        each card separated by a space.
        """
        s = ""
        for i in range(len(self.cards)):
            if i == 0:
                s += repr(self.cards[i]) 
            else:
                s += " " + repr(self.cards[i])
        return s


    def sort_hand(self):
        """
        Sorts the cards in ascending order.
        """
        self.cards.sort(reverse = False)
        
    
class DealerHand(PlayerHand):
    
    def __init__(self):
        # This should inherit attributes from
        # the parent PlayerHand class.
        self.hand_visible = False
        super().__init__()

    def add_card(self, *cards):
        """
        Adds the cards to hand such that only the first card
        in the hand is visible (when the dealer's hand is not visible).
        If the dealer's hand is visible, then add cards to hand as 
        usual and sort them in ascending order.
        """
        for card in cards:
            assert isinstance(card,Card)
            self.cards.append(card)

        if not self.hand_visible:
            for i in range(len(self.cards)):
                if i == 0:
                    self.cards[i].set_visible(True)
                else:
                    self.cards[i].set_visible(False)
        else:
            self.reveal_hand()

    
    def reveal_hand(self):
        """
        Makes all the cards in the hand visible
        and sorts them in ascending order.
        """
        for card in self.cards:
            card.set_visible(True)
        self.sort_hand()
        self.hand_visible = True
    