import unittest
from main import roll_dice, one_attack_defence_scenario


class TestMainFunctions(unittest.TestCase):
    def test_roll_dice(self):
        dice_roll = roll_dice()
        self.assertEqual(dice_roll in range(1, 7), True)


if __name__ == '__main__':
    unittest.main()
