import unittest

def square(x):
    return x ** 2

def area(l, w):
    return l * w

class FunctTests(unittest.TestCase):
    def test_square(self):
        x = square(3)
        self.assertEqual(x, 9)

    def test_area(self):
        x = area(3, 4)
        self.assertEqual(x, 12)

unittest.main()

# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIn(item, list)
# assertNotIn(item, list)
