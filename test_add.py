import unittest

from code.add import add1

class AddTestCase(unittest.TestCase):
    
    def test_add_multiples_of_five(self):
        self.assertEqual(add1(5, 10), 15)

    def test_add_multiples_of_four(self):
        self.assertEqual(add1(4, 8), 12)

    def test_add_multiples_of_three(self):
        self.assertNotEqual(add1(3, 6), 10)

if __name__ == "__main__":
    unittest.main()
