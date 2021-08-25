class Card:
    def __init__(self, value, suit):
        self.v = value
        self.s = suit
    def __str__(self):
        return "("+self.v+' '+self.s+')'
    def next1(self):
        key1 =['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        key2 =['club','diamond','heart','spade'] 
        p1 = key1.index(self.v)
        p2 = key2.index(self.s)
        p2+=1
        if p2==4:
            p2 = 0
            p1 +=1
        if p1==13:
            p1 = 0
        return Card(key1[p1],key2[p2])
    def next2(self):
        a = self.next1()
        self.v = a.v
        self.s = a.s
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])