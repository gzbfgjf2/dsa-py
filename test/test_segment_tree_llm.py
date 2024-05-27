from dsa.tree.segment_tree_llm import SegmentTree
import numpy as np
import unittest


rng = np.random.default_rng(seed=0)


class TestSegmentTree(unittest.TestCase):
    def test_build(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        st = SegmentTree(array)
        self.assertEqual(st.q(0, 2), 6)
        self.assertEqual(st.q(0, 1), 3)
        self.assertEqual(st.q(0, 0), 1)
        self.assertEqual(st.q(1, 2), 5)
        # print(st.tree_values)
        # print(len(st.tree_values))

    def test_sum(self):
        for n in range(1, 1000):
            array = rng.integers(1000, size=n)
            st = SegmentTree(array)
            for _ in range(100):
                i = rng.integers(100)
                j = rng.integers(i, high=100)
                answer = sum(array[i:j])
                self.assertEqual(answer, st.q(i, j - 1))

    def test_update(self):
        array = rng.integers(100, size=100)
        st = SegmentTree(array)
        for _ in range(100):
            i = rng.integers(100)
            j = rng.integers(i, high=100)
            v = rng.integers(-9, 10)
            for idx in range(i, j):
                array[idx] += v
            st.u(i, j - 1, v)

            i = rng.integers(100)
            j = rng.integers(i, high=100)
            answer = sum(array[i:j])
            self.assertEqual(answer, st.q(i, j - 1))

    # def test_boundary(self):
    #     for n in range(1, 100):
    #         r = [0, n]
    #         idx = 1
    #         while r[0] != r[1]:
    #             idx = idx * 2 + 2
    #             r = [r[0] + r[1], r[1]]

    # root = 1, left = 2*i +1 right=2*i+2 won't work
    # 10
    # 1 0:9
    # 4 5:9
    # 9 5:7
    # 19 5:6
    # 40 6:6 ! wrong

    # 10 8:9
    # 22 9:9
