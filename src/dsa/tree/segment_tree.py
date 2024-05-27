class ST:
    # https://cp-algorithms.com/data_structures/segment_tree.html#implementation
    def __init__(self, arr) -> None:
        self.n = len(arr)
        self.tree = [0] * self.n * 2
        self.lazy = [None] * self.n * 2
        self.build(arr, 0, self.n, 1)

    @staticmethod
    def get_right_indx(idx, ti, mid):
        return idx + (mid - ti) * 2

    def push(self, ti, tj, idx, right_idx):
        current_lazy = self.lazy[idx]
        if current_lazy is not None:
            self.tree[idx] = current_lazy * (tj - ti)
            if ti + 1 < tj:
                self.lazy[idx + 1] = current_lazy
                self.lazy[right_idx] = current_lazy
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
        mid = (ti + tj + 1) // 2
        right_idx = self.get_right_indx(idx, ti, mid)
        self.push(ti, tj, idx, right_idx)
        if j <= ti or tj <= i:
            return 0
        if i <= ti and tj <= j:
            return self.tree[idx]
        return self.query(i, j, ti, mid, idx + 1) + self.query(
            i, j, mid, tj, right_idx
        )

    def q(self, i, j):
        return self.query(i, j, 0, self.n)

    def set(self, i, j, val, ti, tj, idx=1):
        mid = (ti + tj + 1) // 2
        right_idx = self.get_right_indx(idx, ti, mid)
        if j <= ti or tj <= i:
            # must have
            self.push(ti, tj, idx, right_idx)
            return
        if i <= ti and tj <= j:
            self.lazy[idx] = val
        self.push(ti, tj, idx, right_idx)
        if ti < j and i < tj and (ti < i or j < tj):
            self.set(i, j, val, ti, mid, idx + 1)
            self.set(i, j, val, mid, tj, right_idx)
            self.tree[idx] = self.tree[idx + 1] + self.tree[right_idx]

    def s(self, i, j, val):
        self.set(i, j, val, 0, self.n)
