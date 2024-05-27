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
        for n in range(1, 1000):
            array = rng.integers(1000, size=n)
            st = ST(array)
            for _ in range(100):
                i = rng.integers(n)
                j = rng.integers(i, high=n)
                answer = sum(array[i:j])
                self.assertEqual(answer, st.q(i, j))

    # def test_update(self):
    #     array = rng.integers(100, size=100)
    #     st = ST(array)
    #     for _ in range(100):
    #         i = rng.integers(100)
    #         j = rng.integers(i, high=100)
    #         v = rng.integers(-9, 10)
    #         for idx in range(i, j):
    #             array[idx] += v
    #         st.s(i, j - 1, v)
    #
    #         i = rng.integers(100)
    #         j = rng.integers(i, high=100)
    #         answer = sum(array[i:j])
    #         self.assertEqual(answer, st.q(i, j - 1))

    def test_set_debug(self):
        array = [1, 2, 3, 4]
        st = ST(array)
        st.s(1, 2, 3)

        self.assertEqual(3, st.q(1, 2))
        self.assertEqual(11, st.q(0, 5))
        self.assertEqual(1, st.q(0, 1))
        self.assertEqual(10, st.q(1, 5))

        st.s(3, 4, -10)
        self.assertEqual(-3, st.q(0, 4))
        self.assertEqual(7, st.q(0, 3))

    def test_set(self):
        high = 100
        size = 500
        array = rng.integers(high, size=size)
        st = ST(array)
        for _ in range(100):
            i = rng.integers(size)
            j = rng.integers(i, size)
            v = rng.integers(-99, 100)
            # print("before", array, i, j, st.tree)
            for idx in range(i, j):
                array[idx] = v
            st.s(i, j, v)

            i = rng.integers(size)
            j = rng.integers(i, size)
            answer = sum(array[i:j])
            res = st.q(i, j)
            self.assertEqual(
                answer,
                res,
                msg=f"{answer} {res} i:{i} j:{j} v:{v} {array} {st.tree}",
            )
