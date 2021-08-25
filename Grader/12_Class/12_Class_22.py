class Card:
    def __init__(self, value, suit):
        self.v = value
        self.s = suit
    def __str__(self):
        return "("+self.v+' '+self.s+')'
    def getScore(self):
        if self.v == 'A':
            return 1
        if self.v == 'J' or self.v =='K' or self.v =='Q':
            return 10
        return int(self.v)
    def sum(self, other):
        return (self.getScore()+other.getScore())%10
    def __lt__(self, rhs):
        key1 =['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        key2 =['club','diamond','heart','spade'] 
        if key1.index(self.v)==key1.index(rhs.v):
            return key2.index(self.s)<key2.index(rhs.s)
        return key1.index(self.v)<key1.index(rhs.v)
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])