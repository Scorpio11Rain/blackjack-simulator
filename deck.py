# Author: Runyu Tian
# PID: A15910502
from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()

    >>> len(deck.get_cards())
    52
    >>> len(hand.get_cards())
    0
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    >>> hand
    (A, clubs)
    >>> len(deck.get_cards())
    51
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        ranks = list(range(2,11)) + ["J","Q","K","A"]
        suits = ["hearts","spades","clubs","diamonds"]
        self.cards = sorted([Card(rank, suit) for rank in ranks for suit in suits])

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all([isinstance(val, int) for val in list(shuffle_and_count.values())])
        assert all([val >=0 for val in list(shuffle_and_count.values())])
        key_lst = ["modified_overhand", "mongean"]
        assert all([key in key_lst for key in list(shuffle_and_count.keys())])

        if "modified_overhand" not in shuffle_and_count.keys():
            mod_over_count = 0
        else:
            mod_over_count = shuffle_and_count["modified_overhand"]
        if "mongean" not in shuffle_and_count.keys():
            mongean_count = 0
        else:
            mongean_count = shuffle_and_count["mongean"]
        
        self.cards = Shuffle.modified_overhand(self.cards, mod_over_count)
        for i in range(mongean_count):
            self.cards = Shuffle.mongean(self.cards)


    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand) or isinstance(hand, DealerHand)
        hand.add_card(self.cards.pop(0))
 
    def get_cards(self):
        return self.cards
