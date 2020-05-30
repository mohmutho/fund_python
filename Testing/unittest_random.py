import unittest
from Testing import random_test
class TestGame(unittest.TestCase):
    def test_input(self):
        result = random_test.run_guess(5, 5)
        self.assertTrue(result)
    def test_input_wrong_guess(self):
        result = random_test.run_guess(5, 7)
        self.assertFalse(result)
    def test_input_wrong_input(self):
        result = random_test.run_guess(5, 11)
        self.assertFalse(result)
    def test_input_wrong_type(self):
        result = random_test.run_guess(5, '11')
        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()