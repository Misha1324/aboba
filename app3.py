from main import *
import unittest

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(add(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(add(a=10, b=20), 30)

    def test_mixed(self):
        self.assertEqual(add(3, x=8), 11)

    def test_deff(self):
        x = 10
        y = 0
        self.assertEqual(add(0, -5, y, a=x), 5)

    def test_wrong_datatype(self):
        self.assertEqual(add("5", "abc", 10), 15)

if __name__ == "__main__":
    unittest.main()