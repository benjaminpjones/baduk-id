import unittest

from baduk_id.baduk_id import encode, decode


# Eventually, other board sizes will be supported
N = 361

EMPTY_BOARD = [0] * N

# Technically illegal positions, but useful for testing
ALL_BLACK = [1] * N
ALL_WHITE = [2] * N

# Example Joseki
# It would be cumbersome to calculate IDs for these by hand, but still useful
# to test in order to detect unexpected changes in behavior.
FLYING_KNIFE = (
    [0] * 19
    + [0] * 12 + [1, 2, 0, 0, 0, 0, 0]
    + [0] * 12 + [0, 1, 2, 2, 2, 0, 0]
    + [0] * 12 + [0, 1, 2, 1, 1, 0, 0]
    + [0] * 12 + [0, 0, 1, 2, 0, 0, 0]
    + [0] * 19 * 14)

class TestEncode(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(encode(EMPTY_BOARD), 0)

    def test_full(self):
        self.assertEqual(encode(ALL_BLACK), 3**N - 2**N)
        self.assertEqual(encode(ALL_WHITE), 3**N - 1)

    def test_random_examples(self):
        self.assertEqual(encode(FLYING_KNIFE), 23785089243857643089678644)

    def test_reversability(self):
        # Obviously we can't test every possible board state...
        # so we just test the first million
        for i in range(1000):
            self.assertEqual(encode(decode(i)), i)

class TestDecode(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(decode(0), EMPTY_BOARD)

    def test_full(self):
        self.assertEqual(decode(3**N - 2**N), ALL_BLACK)
        self.assertEqual(decode(3**N - 1), ALL_WHITE)

    def test_examples(self):
        self.assertEqual(decode(23785089243857643089678644), FLYING_KNIFE)
