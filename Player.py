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
        pass

    def loseGame(self):
        pass
