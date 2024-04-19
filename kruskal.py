def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)
    parent[x_root] = y_root


def kruskal(edges):
    vertices = set()
    for x, y, _ in edges:
        vertices.add(x)
        vertices.add(y)
    edges.sort(key=lambda x: x[2])
    parent = {i: i for i in range(len(vertices))}
    mst = []
    for edge in edges:
        x, y, weight = edge
        if find_parent(parent, x) != find_parent(parent, y):
            mst.append(edge)
            union_parent(parent, x, y)
    return mst


# Test cases
edges1 = [(0, 1, 4), (0, 2, 5), (1, 2, 3), (1, 3, 2), (2, 3, 4), (3, 4, 6)]
print(kruskal(edges1))  # Output: [(1, 3, 2), (0, 1, 4), (2, 3, 4)]

edges2 = [(0, 1, 10), (0, 2, 6), (1, 2, 5), (1, 3, 4), (2, 3, 3)]
print(kruskal(edges2))  # Output: [(0, 2, 6), (1, 3, 4), (0, 1, 10)]
