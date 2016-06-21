class Card(object):

    val = 0
    suit = ''
    """
    @property
    def val(self):
        return self.val
    @property
    def suit(self):
        return self.suit

    @val.setter
    def age(self, val):
        self._val = val

    @suit.setter
    def suit(self, suit):
        self._suit = suit
        """

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def copy(self):
        return copy.deepcopy(self)

    def get_val_str(self):
        if(self.val > 10 or self.val == 1):
            if (self.val == 11):
                return "Jack"
            elif(self.val == 12):
                return "Queen"
            elif(self.val == 13):
                return "King"
            else:
                return "Ace"
        else:
            return str(self.val)

    def get_val(self):
        return self.val

    def get_display(self):
        return " %s of %s" % (self.get_val_str(), self.suit)