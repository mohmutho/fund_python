import unittest
from Testing import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('baout to test the function')
    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, 15)
    def test_do_stuff2(self):
        num2 = 'asdhka'
        result2 = main.do_stuff(num2)
        self.assertIsInstance(result2, ValueError)
    def test_do_stuff3(self):
        num2 = None
        result2 = main.do_stuff(num2)
        self.assertEqual(result2, 'please enter number')
    def tearDown(self):
        print('cleaning up')
if __name__ == '__main__':
    main()
unittest.main()