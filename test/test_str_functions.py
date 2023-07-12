from unittest import TestCase

from src.str_functions import StrFunctions


class TestStrFunctions(TestCase):
    def test_get_number_of_longest_repeated_characters(self):
        functions = StrFunctions()
        res = functions.get_number_of_longest_repeated_characters("aabbbc")
        self.assertEqual(res, 3)

        res = functions.get_number_of_longest_repeated_characters("aaxxxxbbbc")
        self.assertEqual(res, 4)

        res = functions.get_number_of_longest_repeated_characters("aaxxxxbbbccccc")
        self.assertEqual(res, 5)
