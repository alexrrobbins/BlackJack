from Deck import Deck
from Player import Player

#Initialize all items
deck = Deck()
deck.shuffle()
computer_hand = []

bank_roll = int(input("Enter the amount for your bank roll: "))
player = Player(money=bank_roll)
print("For the first game:")
player.set_amount()

#Computer Starts Game
print("We are ready to start the game!")
pc_card1 = deck.draw()
computer_hand.append(pc_card1)
print("The computer's first card is " + str(pc_card1))
computer_hand.append(deck.draw())

#The player plays
print("Player, you will now draw")
player.initialize_hand(deck.draw(),deck.draw())
player.report_hand_value()
action = ''
while not action == 'stay':
    action = input("Do you want to Hit or Stay: ").lower()
    player.hit(deck.draw())
    player.report_hand_value()
    if player.get_hand_value() > 21:
        action = 'stay'
        print("You have busted. The game is over.")
        player.lose_game()
