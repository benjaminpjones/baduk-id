import unittest

from baduk_id.baduk_id import encode

FLYING_KNIFE = (
    [0] * 19
    + [0] * 12 + [1, 2, 0, 0, 0, 0, 0]
    + [0] * 12 + [0, 1, 2, 2, 2, 0, 0]
    + [0] * 12 + [0, 1, 2, 1, 1, 0, 0]
    + [0] * 12 + [0, 0, 1, 2, 0, 0, 0]
    + [0] * 19 * 14)

# Eventually, other board sizes will be supported
N = 361

class TestEncode(unittest.TestCase):
    def test_empty(self):
        empty_board = [0] * N
        self.assertEqual(encode(empty_board), 0)

    def test_full(self):
        # techically, these are illegal positions, but for testing purposes
        # it is good to check

        all_black = [1] * N
        all_white = [2] * N

        self.assertEqual(encode(all_black), 3**N - 2**N)
        self.assertEqual(encode(all_white), 3**N - 1)

    def test_random_examples(self):
        """
        Tests some well known Joseki.  While it's hard to calculate these
        IDs by hand, I wanted to include some real-world tests to detect
        random ID changes.
        """

        self.assertEqual(encode(FLYING_KNIFE), 23785089243857643089678644)
