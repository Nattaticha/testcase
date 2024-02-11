import unittest
from grid_challenge.grid import gridChallenge  

class TestGridChallenge(unittest.TestCase):
    def test_basic_sorted_grid(self):
        self.assertEqual(gridChallenge(["abcde"]), "YES")

    def test_basic_unsorted_grid(self):
        self.assertEqual(gridChallenge(['a', 'b', 'c', 'd', 'e']), "YES")

    def test_single_row_grid(self):
        self.assertEqual(gridChallenge(['abc', 'def', 'ghi']), "YES")

    def test_single_column_grid(self):
        self.assertEqual(gridChallenge(['cba', 'fed', 'ihg']), "YES")

    def test_empty_grid(self):
        self.assertEqual(gridChallenge(['DEsom']), "YES")

    def test_repeated_characters_in_column(self):
        self.assertEqual(gridChallenge(['aed', 'bfc', 'gih']), "NO")

    def test_mixed_case_characters(self):
        self.assertEqual(gridChallenge(['abc', 'def', 'ghi']), "YES")

    def test_large_grid(self):
        self.assertEqual(gridChallenge(['aaa', 'aaa', 'aaa']), "YES")

    def test_large_grid_one_column_unsorted(self):
        self.assertEqual(gridChallenge(['a', 'b', 'H', 'c']), "NO")

    def test_grid_with_special_characters(self):
        self.assertEqual(gridChallenge(["!@#", "#$%", "%^&"]), "NO")

if __name__ == '__main__':
    unittest.main()