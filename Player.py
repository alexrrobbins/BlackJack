class Player():
    def __init__(self, money, hand, amount=0):
        self.money = money
        self.hand = hand
        self.amount = amount

    def setAmount(self, bet_amount):
        if (self.money - bet_amount < 0):
            print("You do not have enough money for that bet!")
        else:
            self.amount = bet_amount
            print("Bet placed!")

    def winGame(self):
        self.money += self.amount

    def loseGame(self):
        self.money -= self.amount

    def initize_hand(self, card1, card2):
        self.hand = [card1, card2]

    def stand(self):
        pass

    def hit(self, card):
        pass
