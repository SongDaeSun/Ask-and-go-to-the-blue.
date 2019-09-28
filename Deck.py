import enum
import random

class Card():
    def __init__(self, month, kind, index):
        self.month = month
        self.kind = kind
        self.index = index

class Kind(enum.Enum):
    light = 0
    tenend = 1
    bird = 2
    red = 3
    blue = 4
    normal = 5
    double = 6
    blood = 7
    hybrid = 8
    

class CardDeck():
    def __init__(self):
        self.deck = list()
        self.reset()

    def reset(self): 
        self.deck= list()

        self.deck.append(Card(1, Kind.light,0))
        self.deck.append(Card(1, Kind.red,1))
        self.deck.append(Card(1, Kind.blood,2))
        self.deck.append(Card(1, Kind.blood,3))

        self.deck.append(Card(2, Kind.bird,4))
        self.deck.append(Card(2, Kind.red,5))
        self.deck.append(Card(2, Kind.blood,6))
        self.deck.append(Card(2, Kind.blood,7))

        self.deck.append(Card(3, Kind.light,8))
        self.deck.append(Card(3, Kind.red,9))
        self.deck.append(Card(3, Kind.blood,10))
        self.deck.append(Card(3, Kind.blood,11))

        self.deck.append(Card(4, Kind.bird,12))
        self.deck.append(Card(4, Kind.normal,13))
        self.deck.append(Card(4, Kind.blood,14))
        self.deck.append(Card(4, Kind.blood,15))

        self.deck.append(Card(5, Kind.tenend,16))
        self.deck.append(Card(5, Kind.normal,17))
        self.deck.append(Card(5, Kind.blood,18))
        self.deck.append(Card(5, Kind.blood,19))

        self.deck.append(Card(6, Kind.tenend,20))
        self.deck.append(Card(6, Kind.blue,21))
        self.deck.append(Card(6, Kind.blood,22))
        self.deck.append(Card(6, Kind.blood,23))

        self.deck.append(Card(7, Kind.tenend,24))
        self.deck.append(Card(7, Kind.normal,25))
        self.deck.append(Card(7, Kind.blood,26))
        self.deck.append(Card(7, Kind.blood,27))

        self.deck.append(Card(8, Kind.light,28))
        self.deck.append(Card(8, Kind.bird,29))
        self.deck.append(Card(8, Kind.blood,30))
        self.deck.append(Card(8, Kind.blood,31))

        self.deck.append(Card(9, Kind.hybrid,32))
        self.deck.append(Card(9, Kind.blue,33))
        self.deck.append(Card(9, Kind.blood,34))
        self.deck.append(Card(9, Kind.blood,35))

        self.deck.append(Card(10, Kind.tenend,36))
        self.deck.append(Card(10, Kind.blue,37))
        self.deck.append(Card(10, Kind.blood,38))
        self.deck.append(Card(10, Kind.blood,39))

        self.deck.append(Card(11, Kind.light,40))
        self.deck.append(Card(11, Kind.double,41))
        self.deck.append(Card(11, Kind.blood,42))
        self.deck.append(Card(11, Kind.blood,43))

        self.deck.append(Card(12, Kind.light,44))
        #self.deck.append(Card(12, Kind.bird,45))
        self.deck.append(Card(12, Kind.normal,46))
        self.deck.append(Card(12, Kind.double,47))

    def getCard(self):
        card = random.choice(self.deck)
        del self.deck[self.deck.index(card)]
        print(card.index)
        return card

test = CardDeck()
#print(test)
#print(test.deck[5].month)
for i in range(0, 48):
    test.getCard()

