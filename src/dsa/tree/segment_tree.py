class ST:
    # https://cp-algorithms.com/data_structures/segment_tree.html#implementation
    def __init__(self, arr) -> None:
        self.n = len(arr)
        self.tree = [0] * self.n * 2
        self.lazy = [None] * self.n * 2
        self.build(arr, 0, self.n, 1)

    @staticmethod
    def get_right_indx(idx, start, mid):
        return idx + (mid - start) * 2

    def push(self, start, stop, idx, right_idx):
        if self.lazy[idx]:
            self.tree[idx] = self.lazy[idx] * (stop - start)
            self.lazy[idx + 1] = self.lazy[right_idx] = self.lazy[idx]
            self.lazy[idx] = None

    def build(self, arr, ti, tj, idx=1):
        if ti + 1 == tj:
            self.tree[idx] = arr[ti]
            return
        mid = (ti + tj + 1) // 2
        right_idx = self.get_right_indx(idx, ti, mid)
        self.build(arr, ti, mid, idx + 1)
        self.build(arr, mid, tj, right_idx)
        self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]

    def query(self, i, j, ti, tj, idx=1):
        # ti stands for tree_i
        if j <= ti or tj <= i:
            return 0
        if i <= ti and tj <= j:
            return self.tree[idx]
        mid = (ti + tj + 1) // 2
        right_idx = self.get_right_indx(idx, ti, mid)
        self.push(ti, tj, idx, right_idx)
        return self.query(i, j, ti, mid, idx + 1) + self.query(
            i, j, mid, tj, right_idx
        )

    def q(self, i, j):
        return self.query(i, j, 0, self.n)

    def set(self, i, j, val, ti, tj, idx=1):
        if tj <= i or j <= ti:
            return
        mid = (i + j + 1) // 2
        right_idx = self.get_right_indx(idx, ti, mid)
        if ti <= i and j <= tj:
            self.lazy[idx] = val
        self.push(i, j, idx, right_idx)
        if i < tj and ti < j:
            self.set(ti, tj, val, i, mid, idx + 1)
            self.set(ti, tj, val, mid, j, right_idx)
            self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]
