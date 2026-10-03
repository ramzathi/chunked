import unittest

from chunked import chunk_count, chunks, remainder


class ChunkedTest(unittest.TestCase):
    def test_split(self) -> None:
        self.assertEqual(chunks([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunks([], 3), [])
        self.assertEqual(chunk_count([1, 2, 3, 4, 5], 2), 3)
        self.assertEqual(remainder([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(remainder([1, 2, 3, 4], 2), 0)
        with self.assertRaises(ValueError):
            chunks([1], 0)


if __name__ == "__main__":
    unittest.main()
