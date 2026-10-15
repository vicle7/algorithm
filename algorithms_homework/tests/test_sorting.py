import random
import unittest

from sorting import bubble_sort, quick_sort


class TestSorting(unittest.TestCase):
    def test_common_cases(self):
        cases = [
            [], [1], [2, 1], [3, 3, 3], [1, 2, 3],
            [5, 4, 3, 2, 1], [-1, 3, 0, -7, 3, 10],
        ]
        for sorter in (bubble_sort, quick_sort):
            for values in cases:
                with self.subTest(sorter=sorter.__name__, values=values):
                    original = values.copy()
                    self.assertEqual(sorter(values), sorted(values))
                    self.assertEqual(values, original)  # Исходный список не меняется

    def test_randomized(self):
        rng = random.Random(2026)
        for sorter in (bubble_sort, quick_sort):
            for _ in range(30):
                values = [rng.randint(-100, 100) for _ in range(rng.randrange(0, 100))]
                self.assertEqual(sorter(values), sorted(values))


if __name__ == "__main__":
    unittest.main()
