from Player import Player

player1 = Player(money=100.00)
player1.setAmount()

print("----------------------------------")
print(player1.initializeHand(10,2))

player2 = Player(money=300)
print("----------------------------------")
print(player2.initializeHand(5,'x')) #Returning 0 right now
