import unittest

from chunked import chunk_count, chunks, even, full_count, head, last_short, piece_at, piece_len, remainder, short_count, tail


class ChunkedTest(unittest.TestCase):
    def test_split(self) -> None:
        self.assertEqual(chunks([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunks([], 3), [])
        self.assertEqual(chunk_count([1, 2, 3, 4, 5], 2), 3)
        self.assertEqual(remainder([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(remainder([1, 2, 3, 4], 2), 0)
        with self.assertRaises(ValueError):
            chunks([1], 0)
        self.assertTrue(last_short([1, 2, 3], 2))
        self.assertFalse(last_short([1, 2, 3, 4], 2))
        self.assertFalse(last_short([], 2))
        self.assertEqual(full_count([1, 2, 3, 4, 5], 2), 2)
        self.assertEqual(full_count([], 2), 0)
        self.assertEqual(tail([1, 2, 3, 4, 5], 2), [5])
        self.assertEqual(tail([], 2), [])
        self.assertEqual(head([1, 2, 3, 4, 5], 2), [1, 2])
        self.assertEqual(head([], 2), [])
        self.assertTrue(even([1, 2, 3, 4], 2))
        self.assertFalse(even([1, 2, 3], 2))
        self.assertEqual(short_count([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(short_count([1, 2, 3, 4], 2), 0)
        self.assertEqual(piece_at([1, 2, 3, 4, 5], 2, 0), [1, 2])
        self.assertEqual(piece_at([1, 2, 3, 4, 5], 2, 9), [])
        self.assertEqual(piece_len([1, 2, 3, 4, 5], 2, 0), 2)
        self.assertEqual(piece_len([1, 2, 3, 4, 5], 2, 9), 0)


if __name__ == "__main__":
    unittest.main()
