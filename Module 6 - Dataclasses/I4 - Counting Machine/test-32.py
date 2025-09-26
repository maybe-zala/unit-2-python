import unittest

from main import *

class TestFunctions(unittest.TestCase):

    def test_counter_class(self):
        count=Counter()
        self.assertEqual(count.number, 0)

    def test_inc_function(self):
        count=Counter()
        self.assertEqual(count.number, 0)
        inc(count)
        self.assertEqual(count.number, 1)
        inc(count)
        self.assertEqual(count.number, 2)
        inc(count)
        self.assertEqual(count.number, 3)
        for _ in range(97):
            inc(count)
        self.assertEqual(count.number, 100)

    def test_dec_function(self):
        count=Counter()
        self.assertEqual(count.number, 0)
        dec(count)
        self.assertEqual(count.number, -1)
        inc(count)
        inc(count)
        inc(count)
        self.assertEqual(count.number, 2)
        dec(count)
        self.assertEqual(count.number, 1)
        for _ in range(101):
            dec(count)
        self.assertEqual(count.number, -100)

if __name__ == '__main__':
    unittest.main()