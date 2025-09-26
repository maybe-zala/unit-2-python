import unittest

from main import *

class TestFunctions(unittest.TestCase):

    def test_dog_class(self):
        dog = Dog("Buddy", 50, False)
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.weight, 50)
        self.assertFalse(dog.is_tired)

        dog2 = Dog("Max", 30, True)
        self.assertEqual(dog2.name, "Max")
        self.assertEqual(dog2.weight, 30)
        self.assertTrue(dog2.is_tired)

        dog3 = Dog("Bella", 20, False)
        self.assertEqual(dog3.name, "Bella")
        self.assertEqual(dog3.weight, 20)
        self.assertFalse(dog3.is_tired)

    def test_dog_sound_function(self):
        dog = Dog("Buddy", 50, False)
        dog2 = Dog("Max", 30, True)
        dog3 = Dog("Bella", 120, False)
        dog4 = Dog("Tiny", 10, False)
        self.assertEqual(dog_sound(dog), "RUFF RUFF")
        self.assertEqual(dog_sound(dog2), "zzzzz")
        self.assertEqual(dog_sound(dog3), "RUFF RUFF")
        self.assertEqual(dog_sound(dog4), "yip yip yip")

    def test_play_with_dog_function(self):
        dog = Dog("Buddy", 50, False)
        dog2 = Dog("Max", 30, False)
        dog3 = Dog("Bella", 20, False)
        dog4 = Dog("Tiny", 10, False)
        self.assertFalse(dog.is_tired)
        self.assertFalse(dog2.is_tired)
        self.assertFalse(dog3.is_tired)
        self.assertFalse(dog4.is_tired)
        play_with_dog(dog)
        play_with_dog(dog3)
        self.assertTrue(dog.is_tired)
        self.assertFalse(dog2.is_tired)
        self.assertTrue(dog3.is_tired)
        self.assertFalse(dog4.is_tired)

if __name__ == '__main__':
    unittest.main()