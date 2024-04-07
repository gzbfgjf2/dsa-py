# + significant bit = move to parent node
# - significant bit = move to a even tree node left


class BIT:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.n = n

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & (-i)

    def range(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res


class FullBit(BIT):
    def __init__(self, arr):
        self.n = len(arr)
        super().__init__(self.n)
        for i, x in enumerate(arr, start=1):
            self.update(i, x)

    def interval(self, i, j):
        return self.range(j) - self.range(i)
