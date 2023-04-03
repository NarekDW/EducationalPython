import unittest

from src.functions import Functions


class MyTestCase(unittest.TestCase):

    def test_something(self):
        functions = Functions()
        self.assertEqual(functions.sort([1, 5, 2, 3, 2, 2, 1]), [1, 1, 2, 2, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
