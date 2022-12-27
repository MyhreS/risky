import unittest
from main import *


class TestMainFunctions(unittest.TestCase):
    def test_roll_dice(self):
        dice_roll = roll_dice()
        self.assertTrue(dice_roll in range(1, 7))

    def test_roll_attacker_and_defender(self):
        attacker, defender = roll_attacker_and_defender(3, 2)
        self.assertEqual(3, len(attacker))
        self.assertEqual(2, len(defender))


if __name__ == '__main__':
    unittest.main()
