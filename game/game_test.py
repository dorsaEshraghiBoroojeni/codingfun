import unittest
import game

class TestGame(unittest.TestCase):

    def test_r_wins_s(self):
        result = game.play('r','s')
        self.assertEqual(result,'Won')

    def test_s_wins_p(self):
        result = game.play('s','p')
        self.assertEqual(result,'Won')

    def test_p_wins_r(self):
        result = game.play('p','r')
        self.assertEqual(result,'Won')


    def test_r_Lost_p(self):
        result = game.play('r','p')
        self.assertEqual(result,'Lost')

    def test_s_Lost_r(self):
        result = game.play('s','r')
        self.assertEqual(result,'Lost')

    def test_equal_res_p(self):
        result = game.play('p','p')
        self.assertEqual(result,'again')

    def test_equal_res_r(self):
        result = game.play('r', 'r')
        self.assertEqual(result, 'again')


    def test_valid_input_multiple_char(self):
        self.assertFalse(game.valid('ggg'))

    def test_valid_input_number(self):
        self.assertFalse(game.valid('45'))

if __name__ == "__main__":
    unittest.main









