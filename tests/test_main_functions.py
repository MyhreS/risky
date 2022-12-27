import unittest
from main import *


class TestMainFunctions(unittest.TestCase):
    def test_roll_dice(self):
        dice_roll = roll_dice()
        self.assertTrue(dice_roll in range(1, 7))



if __name__ == '__main__':
    unittest.main()
