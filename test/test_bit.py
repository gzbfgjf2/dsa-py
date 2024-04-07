from dsa.tree.bit import BIT, FullBit
import numpy as np
import unittest


rng = np.random.default_rng(seed=0)


class TestBIT(unittest.TestCase):
    def test_s(self):
        array = [1, 2, 3]
        bit = FullBit(array)
        self.assertEqual(bit.interval(0, 3), 6)
        self.assertEqual(bit.interval(0, 2), 3)
        self.assertEqual(bit.interval(0, 1), 1)
        self.assertEqual(bit.interval(0, 0), 0)
        self.assertEqual(bit.interval(1, 3), 5)

    def test_sum(self):
        array = rng.integers(100, size=100)
        bit = FullBit(array)
        for _ in range(100):
            i = rng.integers(100)
            j = rng.integers(i, high=100)
            answer = sum(array[i:j])
            self.assertEqual(answer, bit.interval(i, j))
