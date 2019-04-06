from Player import Player
from Ace import Ace
import unittest

class PlayerTest(unittest.TestCase):
    def test_no_ace(self):
        player1 = Player(money=100.00)
        result = player1.initializeHand(10,2)
        self.assertEqual(result,12)

    def test_ace(self):
        player2 = Player(money=300)
        ace = Ace()
        print("Please enter 1 when prompted")
        result = player2.initializeHand(5,ace)
        self.assertEqual(result,6)

if __name__ == '__main__':
    unittest.main()
