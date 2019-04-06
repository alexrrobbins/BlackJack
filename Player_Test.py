from Player import Player
from Ace import Ace
import unittest

class PlayerTest(unittest.TestCase):
    def test_no_ace(self):
        player = Player()
        result = player.initialize_hand(10,2)
        self.assertEqual(result,12)

    def test_ace(self):
        player = Player()
        ace = Ace()
        print("Please enter 1 when prompted")
        result = player.initialize_hand(5,ace)
        self.assertEqual(result,6)

    def test_hit_no_ace(self):
        player = Player()
        player.initialize_hand(10,2)
        result = player.hit(2)
        self.assertEqual(result,14)

    def test_hit_with_ace(self):
        player = Player()
        ace = Ace()
        player.initialize_hand(10,2)
        print("Please enter 1 when prompted")
        result = player.hit(ace)
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()
