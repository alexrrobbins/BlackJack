from Player import Player
from Ace import Ace

ace = Ace()
player1 = Player(money=100.00)
player1.setAmount()

print("----------------------------------")
print(player1.initializeHand(10,2))

player2 = Player(money=300)
print("----------------------------------")
print(player2.initializeHand(5,ace)) #Returning 0 right now
