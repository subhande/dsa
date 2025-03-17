

class Solution:
    def bellman_ford(self, V, edges, S):
        INF = 10 ** 9
        dist = [INF] * V
        dist[S] = 0
        for _ in range(V-1):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]
        return dist
