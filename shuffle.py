# Author: Runyu Tian
# PID: A15910502
class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24

    >>> odd = [1,2,3,4,5]
    >>> odd_shuf = Shuffle.modified_overhand(odd, 3)
    >>> odd_shuf
    [2, 3, 4, 1, 5]
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25

    >>> mongean_shuffle[2]
    47

    >>> mong_odd = [1,2,3,4,5]
    >>> mong_odd = Shuffle.mongean(mong_odd)
    >>> mong_odd
    [4, 2, 1, 3, 5]

    >>> mong_even = [1,2,3,4,5,6]
    >>> mong_even= Shuffle.mongean(mong_even)
    >>> mong_even
    [6, 4, 2, 1, 3, 5]
    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert isinstance(cards, list)
        assert isinstance(num, int)
        assert num <= len(cards)

        length = len(cards)
        if num == 0:
            return cards
        if length % 2 == 0:
            if num % 2 == 0:
                cards = cards[length//2 - num//2 : length//2 + num//2] + cards[:length//2 - num//2] + cards[length//2 + num//2:]
            elif num % 2 == 1:
                cards = cards[length//2 - (num+1)//2  : length//2 + (num+1)//2 - 1] + cards[:length//2 - (num+1)//2] \
                + cards[length//2 + (num+1)//2 - 1:]
        elif length % 2 == 1:
            if num % 2 == 0:
                cards = cards[length//2 - num//2 : length//2 + num//2] + cards[:length//2 - num//2] + cards[length//2 + num//2:]
            elif num % 2 == 1:
                cards = cards[length//2 - num//2 : length//2 + num//2 + 1] + cards[:length//2 - num//2] + cards[length//2 + num//2 + 1:]
        return Shuffle.modified_overhand(cards, num - 1)



    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        if len(cards) == 0:
            return []
        if len(cards) % 2 == 0:
            return [cards[-1]] + Shuffle.mongean(cards[:-1])
        elif len(cards) % 2 == 1:
            return Shuffle.mongean(cards[:-1]) + [cards[-1]]


        
        

    