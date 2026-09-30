import unittest

from chunked import chunk_count, chunks


class ChunkedTest(unittest.TestCase):
    def test_split(self) -> None:
        self.assertEqual(chunks([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunks([], 3), [])
        self.assertEqual(chunk_count([1, 2, 3, 4, 5], 2), 3)
        with self.assertRaises(ValueError):
            chunks([1], 0)


if __name__ == "__main__":
    unittest.main()
