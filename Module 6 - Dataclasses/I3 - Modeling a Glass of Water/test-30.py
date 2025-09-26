import unittest

from main import *

class TestFunctions(unittest.TestCase):

    def test_glass_class(self):
        glass=Glass(100, 0)
        self.assertEqual(glass.capacity, 100)
        self.assertEqual(glass.current_amount, 0)

        glass2=Glass(50, 10)
        self.assertEqual(glass2.capacity, 50)
        self.assertEqual(glass2.current_amount, 10)

        glass3=Glass(200, 150)
        self.assertEqual(glass3.capacity, 200)
        self.assertEqual(glass3.current_amount, 150)

    def test_pour_in_function(self):
        glass=Glass(100, 0)
        glass.pour_in(30)
        self.assertEqual(glass.current_amount, 30)
        glass.pour_in(80)
        self.assertEqual(glass.current_amount, 100)
        glass.pour_in(100)
        self.assertEqual(glass.current_amount, 100)

    def test_pour_out_function(self):
        glass=Glass(100, 0)
        glass.pour_out(30)
        self.assertEqual(glass.current_amount, 0)
        glass.pour_in(50)
        self.assertEqual(glass.current_amount, 50)
        glass.pour_out(20)
        self.assertEqual(glass.current_amount, 30)
        glass.pour_out(50)
        self.assertEqual(glass.current_amount, 0)

if __name__ == '__main__':
    unittest.main()