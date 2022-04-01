# Author: Runyu Tian
# PID: A15910502
class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert (isinstance(rank,int) and (rank >=2 and rank <= 10)) or (isinstance(rank,str) and rank in ["A","J","Q","K"])
        assert isinstance(suit,str)
        assert suit in ["hearts","spades","clubs","diamonds"]
        assert isinstance(visible, bool)
        self.rank = rank 
        self.suit = suit 
        self.visible = visible
        

    def __lt__(self, other_card):
        rank_seq = list(range(2,11)) + ["J","Q","K","A"]
        this_rank_idx = rank_seq.index(self.rank)
        other_rank_idx = rank_seq.index(other_card.get_rank())
        if this_rank_idx < other_rank_idx:
            return True
        elif this_rank_idx > other_rank_idx:
            return False
        else:
            return self.suit<other_card.suit


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if not self.visible:
            return "____\n|?  |\n| ? |\n|__?|"
        else:
            if self.suit == "hearts":
                suit_s = "♥"
            elif self.suit == "spades":
                suit_s = "♠"
            elif self.suit == "clubs":
                suit_s = "♣"
            elif self.suit == "diamonds":
                suit_s = "♦"
            return "____\n|" + str(self.rank) + "  |\n| " + suit_s + " |\n|__" + str(self.rank) + "|"


    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """    
        if not self.visible:
            return "(?, ?)"
        return "(" + str(self.rank) + ", " + self.suit + ")"  
  

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
    