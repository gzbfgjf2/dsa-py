from collections import defaultdict


class SegmentTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.segTree = [0] * (4 * self.size)
        self.buildSegTree(0, 0, self.size - 1, arr)

    def buildSegTree(self, node, start, end, arr):
        if start == end:
            self.segTree[node] = arr[start]
            return

        mid = (start + end) // 2
        self.buildSegTree(2 * node + 1, start, mid, arr)
        self.buildSegTree(2 * node + 2, mid + 1, end, arr)
        self.segTree[node] = (
            self.segTree[2 * node + 1] + self.segTree[2 * node + 2]
        )

    def query(self, node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and r >= end:
            return self.segTree[node]

        mid = (start + end) // 2
        return self.query(2 * node + 1, start, mid, l, r) + self.query(
            2 * node + 2, mid + 1, end, l, r
        )

    def update(self, node, start, end, idx, val):
        if start == end:
            self.segTree[node] += val
            return

        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)

        self.segTree[node] = (
            self.segTree[2 * node + 1] + self.segTree[2 * node + 2]
        )


# class SegmentTreeIndex

# Example usage:
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

# Query sum of elements from index 2 to index 4 (inclusive)
print(st.query(0, 0, len(arr) - 1, 2, 4))  # Output: 15

# Update value at index 3
st.update(0, 0, len(arr) - 1, 3, 2)

# Query sum of elements from index 0 to index 5 (inclusive)
print(st.query(0, 0, len(arr) - 1, 0, 5))  # Output: 26


# class ST:
#     L = 0
#     R = 8
#
#     def __init__(self):
#         self.t = defaultdict(int)
#         self.lazy = defaultdict(int)
#
#     def push_lazy(self, i, j, v, l=L, r=R, idx=1):
#         if i <= l and r <= j:
#             self.lazy[idx] += v
#         if self.lazy[idx] != 0:
#             self.t[idx] += self.lazy[idx] * (r - l)
#             if l + 1 < r:
#                 self.lazy[idx * 2] += self.lazy[idx]
#                 self.lazy[idx * 2 + 1] += self.lazy[idx]
#             self.lazy[idx] = 0
#
#     def range(self, i, j, v, l=L, r=R, idx=1):
#         print(i, j, l, r)
#         self.push_lazy(i, j, v, l, r, idx)
#         if i <= l and r <= j:
#             return
#         if i >= r or j <= l:
#             return
#         mid = (l + r) // 2
#         self.range(i, j, v, l, mid, idx * 2)
#         self.range(i, j, v, mid, r, idx * 2 + 1)
#         self.t[idx] = self.t[idx * 2] + self.t[idx * 2 + 1]
#
#     def query(self, i, j, l=L, r=R, idx=1):
#         self.push_lazy(i, j, 0, l, r, idx)
#         if i <= l and r <= j:
#             return self.t[idx]
#         if i >= r or j <= l:
#             return 0
#         mid = (l + r) // 2
#         return self.query(i, j, l, mid, idx * 2) + self.query(
#             i, j, mid, r, idx * 2 + 1
#         )


class IndexST:
    # https://cp-algorithms.com/data_structures/segment_tree.html#implementation
    def __init__(self, arr) -> None:
        self.n = len(arr)
        self.tree = [0] * (self.n * 2)
        self.lazy = [None] * (self.n * 2)
        self.build(arr, 0, self.n, 1)

    @staticmethod
    def get_right_indx(idx, start, mid):
        return idx + (mid - start) * 2

    def handle_set_lazy(self, start, stop, idx):
        if self.lazy[idx] is None:
            return
        self.tree[idx] = self.lazy[idx] * (stop - start)
        mid = (start + stop) // 2
        right_idx = self.get_right_indx(idx, start, mid)
        if start + 1 < stop:
            self.lazy[idx + 1] = self.lazy[idx]
            self.lazy[right_idx] = self.lazy[idx]
        self.lazy[idx] = None

    def build(self, arr, start, stop, idx):
        if start + 1 == stop:
            self.tree[idx] = arr[start]
            return
        mid = (start + stop) // 2
        right_idx = self.get_right_indx(idx, start, mid)
        self.build(arr, start, mid, idx + 1)
        self.build(arr, mid, stop, right_idx)
        self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]

    def query(self, tstart, tstop, start, stop, idx=1):
        self.handle_set_lazy(start, stop, idx)
        if tstop <= start or stop <= tstart:
            return 0
        if tstart <= start and stop <= tstop:
            return self.tree[idx]
        mid = (start + stop) // 2
        right_idx = self.get_right_indx(idx, start, mid)
        return self.query(tstart, tstop, start, mid, idx + 1) + self.query(
            tstart, tstop, mid, stop, right_idx
        )

    def set(self, tstart, tstop, val, start, stop, idx=1):
        if tstart <= start and stop <= tstop:
            self.lazy[idx] = val
        self.handle_set_lazy(start, stop, idx)
        if (
            tstop <= start
            or stop <= tstart
            or tstart <= start
            and stop <= tstop
        ):
            return
        mid = (start + stop) // 2
        right_idx = self.get_right_indx(idx, start, mid)
        self.set(tstart, tstop, val, start, mid, idx + 1)
        self.set(tstart, tstop, val, mid, stop, right_idx)
        self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]
        return self.tree[idx]


class ST:
    # https://cp-algorithms.com/data_structures/segment_tree.html#implementation
    def __init__(self, arr) -> None:
        n = len(arr) * 2
        self.tree = [0] * n
        self.lazy = [None] * n
        self.build(arr, 0, n, 1)

    @staticmethod
    def get_right_indx(idx, start, mid):
        return idx + (mid - start) * 2

    def push(self, start, stop, idx, right_idx):
        if self.lazy[idx]:
            self.tree[idx] = self.lazy[idx] * (stop - start)
            self.lazy[idx + 1] = self.lazy[right_idx] = self.lazy[idx]
            self.lazy[idx] = None

    def build(self, arr, start, stop, idx):
        mid = (start + stop) // 2
        right_idx = self.get_right_indx(idx, start, mid)
        if start + 1 == stop:
            self.tree[idx] = arr[start]
            return
        self.build(arr, start, mid, idx + 1)
        self.build(arr, mid, stop, right_idx)
        self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]

    def query(self, ti, tj, i, j, idx):
        # ti stands for tree_i
        mid = (i + j) // 2
        right_idx = self.get_right_indx(idx, i, mid)
        self.push(i, j, idx, right_idx)
        if tj <= i or j <= ti:
            return 0
        if ti <= i and j <= tj:
            return self.tree[idx]
        return self.query(ti, tj, i, mid, idx + 1) + self.query(
            ti, tj, mid, j, right_idx
        )

    # def set(self, ti, tj, val, i, j, idx):
    #     mid = (i + j) // 2
    #     right_idx = self.get_right_indx(idx, i, mid)
    #     if ti <= i and j <= tj:
    #         self.lazy[idx] = val
    #     self.push(i, j, idx, right_idx)
    #     if tj <= i or j <= ti or ti <= i and j <= tj:
    #         return
    #     self.set(ti, tj, val, i, mid, idx + 1)
    #     self.set(ti, tj, val, mid, j, right_idx)
    #     self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]
    #     return self.tree[idx]

    def set(self, ti, tj, val, i, j, idx):
        if tj <= i or j <= ti:
            return
        mid = (i + j) // 2
        right_idx = self.get_right_indx(idx, i, mid)
        if ti <= i and j <= tj:
            self.lazy[idx] = val
        self.push(i, j, idx, right_idx)
        if i < tj and tj < j:
            self.set(ti, tj, val, i, mid, idx + 1)
            self.set(ti, tj, val, mid, j, right_idx)
            self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]
