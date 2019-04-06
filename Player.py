from Ace import Ace

class Player():
    def __init__(self, money=0, hand=[], amount=0, hand_value=0):
        self.money = money
        self.hand = hand
        self.amount = amount
        self.hand_value = hand_value

    #Money related methods
    def setAmount(self):
        test = True
        while test:
            bet_amount = float(input("Enter bet amount: "))
            if (self.money - bet_amount < 0):
                print("You do not have enough money for that bet!")
            else:
                self.amount = bet_amount
                print("Bet placed!")
                test = False

    def winGame(self):
        self.money += self.amount

    def loseGame(self):
        self.money -= self.amount

    #Game related methods
    def initializeHand(self, card1, card2):
        self.hand = [card1, card2]
        try:
            self.hand_value = card1+card2
        except:
            if type(card1) == Ace:
                card1.change_value()
                self.hand_value = chard1.get_value() + card2
            else:
                card2.change_value()
                self.hand_value = card1 + card2.get_value()
        finally:
            return self.hand_value

    def stay(self):
        pass

    def hit(self, card):
        try:
            self.hand_value = self.hand_value + card
        except:
            card.change_value()
            self.hand_value = self.hand_value + card.get_value()
        finally:
            return self.hand_value
