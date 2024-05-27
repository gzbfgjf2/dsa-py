root_idx = 0


def left(idx):
    return idx * 2 + 1


def right(idx):
    return idx * 2 + 2


# or
# root_idx = 1
#
# def left(idx):
#     return idx * 2
#
# def right(idx):
#     return idx * 2 + 1


class SegmentTree:
    def __init__(self, values):
        self.tree_values = [0] * (4 * len(values))
        self.lazy_values = [0] * (4 * len(values))
        self.build_tree(values, 0, len(values) - 1, root_idx)
        self.last = len(values) - 1
        # print(self.tree_values)

    def build_tree(self, values, start, end, node):
        if start == end:
            # print(node, start)
            self.tree_values[node] = values[start]
        else:
            mid = (start + end) // 2
            self.build_tree(values, start, mid, left(node))
            self.build_tree(values, mid + 1, end, right(node))
            self.tree_values[node] = (
                self.tree_values[left(node)] + self.tree_values[right(node)]
            )

    def q(self, i, j):
        return self.query(0, self.last, i, j, root_idx)

    def query(
        self,
        tree_node_start,
        tree_node_end,
        query_start,
        query_end,
        current_node_id,
    ):
        # print(current_node_id)
        if self.lazy_values[current_node_id] != 0:
            self.tree_values[current_node_id] += self.lazy_values[
                current_node_id
            ] * (tree_node_end - tree_node_start + 1)
            if tree_node_start != tree_node_end:
                self.lazy_values[left(current_node_id)] += self.lazy_values[
                    current_node_id
                ]
                self.lazy_values[right(current_node_id)] += self.lazy_values[
                    current_node_id
                ]
            self.lazy_values[current_node_id] = 0

        if query_start > tree_node_end or query_end < tree_node_start:
            return 0
        if query_start <= tree_node_start and query_end >= tree_node_end:
            return self.tree_values[current_node_id]

        mid = (tree_node_start + tree_node_end) // 2
        left_sum = self.query(
            tree_node_start,
            mid,
            query_start,
            query_end,
            left(current_node_id),
        )
        right_sum = self.query(
            mid + 1,
            tree_node_end,
            query_start,
            query_end,
            right(current_node_id),
        )
        return left_sum + right_sum

    def u(self, update_start, update_end, update_value):
        self.update(
            0, self.last, update_start, update_end, update_value, root_idx
        )

    def update(
        self,
        tree_node_start,
        tree_node_end,
        update_start,
        update_end,
        update_value,
        current_node_id,
    ):
        if self.lazy_values[current_node_id] != 0:
            self.tree_values[current_node_id] += self.lazy_values[
                current_node_id
            ] * (tree_node_end - tree_node_start + 1)
            if tree_node_start != tree_node_end:
                self.lazy_values[left(current_node_id)] += self.lazy_values[
                    current_node_id
                ]
                self.lazy_values[right(current_node_id)] += self.lazy_values[
                    current_node_id
                ]
            self.lazy_values[current_node_id] = 0

        if update_start > tree_node_end or update_end < tree_node_start:
            return
        if update_start <= tree_node_start and update_end >= tree_node_end:
            self.tree_values[current_node_id] += update_value * (
                tree_node_end - tree_node_start + 1
            )
            if tree_node_start != tree_node_end:
                self.lazy_values[left(current_node_id)] += update_value
                self.lazy_values[right(current_node_id)] += update_value
            return

        mid = (tree_node_start + tree_node_end) // 2
        self.update(
            tree_node_start,
            mid,
            update_start,
            update_end,
            update_value,
            left(current_node_id),
        )
        self.update(
            mid + 1,
            tree_node_end,
            update_start,
            update_end,
            update_value,
            right(current_node_id),
        )
        self.tree_values[current_node_id] = (
            self.tree_values[left(current_node_id)]
            + self.tree_values[right(current_node_id)]
        )
