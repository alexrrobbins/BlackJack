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
            ace = int(input("Do you want your ace to equal 1 or 11: "))
            if (not card1.isdigit()):
                card1 = ace
            elif (not card2.isdigit()):
                card2 = ace
            self.hand_value = card1+card2
        finally:
            return self.hand_value

    def stand(self):
        pass

    def hit(self, card):
        pass
