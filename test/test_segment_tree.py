from dsa.tree.segment_tree import ST
import numpy as np
import unittest


rng = np.random.default_rng(seed=0)


class TestSegmentTree(unittest.TestCase):
    def test_s(self):
        array = [1, 2, 3]
        n = len(array)
        st = ST(array)
        self.assertEqual(st.q(0, 3), 6)
        self.assertEqual(st.q(0, 2), 3)
        self.assertEqual(st.q(0, 1), 1)
        self.assertEqual(st.q(0, 0), 0)
        self.assertEqual(st.q(1, 3), 5)

    def test_sum(self):
        array = rng.integers(100, size=100)
        st = ST(array)
        for _ in range(100):
            i = rng.integers(100)
            j = rng.integers(i, high=100)
            answer = sum(array[i:j])
            self.assertEqual(answer, st.q(i, j))
