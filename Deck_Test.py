from Deck import Deck

deck1 = Deck()
print(len(deck1))
print(deck1)

print('---------------------------------------------------------------------')

deck1.shuffle()
print(deck1)

print('---------------------------------------------------------------------')

test_hand = []
test_hand.append(deck1.draw())
test_hand.append(deck1.draw())

print(test_hand)
print(len(deck1))
