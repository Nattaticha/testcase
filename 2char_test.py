import unittest
from Two_char.two_char import twochar

class Testtwochar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(twochar(""), 0)

    def test_string_one_unique_char(self):
        self.assertEqual(twochar("aaaa"), 0)

    def test_string_two_unique_char_no_alternating(self):
        self.assertEqual(twochar("aabbcc"), 0)

    def test_string_two_unique_char_alternating(self):
        self.assertEqual(twochar("ababab"), 6)

    def test_string_three_unique_char_no_alternating(self):
        self.assertEqual(twochar("abcabcabc"), 6)

    def test_string_three_unique_char_alternating(self):
        self.assertEqual(twochar("abababab"), 8)

    def test_string_mixed_char_alternating(self):
        self.assertEqual(twochar("a1b2c3d4e5"), 2)

    def test_string_special_characters(self):
        self.assertEqual(twochar("!@#$%^&*()"), 2)

    def test_string_numbers(self):
        self.assertEqual(twochar("123456789"), 2)

    def test_string_mixed_case(self):
        self.assertEqual(twochar("AbCdEfGhIjK"), 2)

if __name__ == '__main__':
    unittest.main()