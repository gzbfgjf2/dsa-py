    def bellman_ford(graph, src, n):
        dist = [float("Inf")] * n
        dist[src] = 0
        for _ in range(n - 1):
            for u, v, w in graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
