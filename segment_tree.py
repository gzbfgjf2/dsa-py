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


# Example usage:
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

# Query sum of elements from index 2 to index 4 (inclusive)
print(st.query(0, 0, len(arr) - 1, 2, 4))  # Output: 15

# Update value at index 3
st.update(0, 0, len(arr) - 1, 3, 2)

# Query sum of elements from index 0 to index 5 (inclusive)
print(st.query(0, 0, len(arr) - 1, 0, 5))  # Output: 26
