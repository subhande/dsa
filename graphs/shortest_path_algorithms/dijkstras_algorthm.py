# Dijkstra's Algorithm

import heapq

class Solution:
    # Time complexity: O(V+E)*log(V) | Space complexity: O(V)
    def dijkstraUsingHeap(self, V, adj, S):
        INF = float('inf')
        # Initialize distance array with infinity.
        dist = [INF] * V
        dist[S] = 0
        # Initialize min heap with source node.
        minHeap = [(0, S)]
        while minHeap:
            # Pop the node with minimum distance.
            d, node = heapq.heappop(minHeap)
            # Explore each neighbor of the current node.
            for neighbor, weight in adj[node]:
                # If the distance to the neighbor is less than the current distance, update it.
                if dist[neighbor] > dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
                    heapq.heappush(minHeap, (dist[neighbor], neighbor))
        return dist

    # Time complexity: O(V^2+E) | Space complexity: O(V)
    def dijkstraUsingSet(self, V, adj, S):
        INF = float('inf')
        # Initialize distance array with infinity.
        dist = [INF] * V
        dist[S] = 0
        # Initialize set with all nodes.
        nodes = set(range(V))
        while nodes:
            # Find the node with minimum distance.
            node = min(nodes, key=lambda x: dist[x])
            nodes.remove(node)
            # Explore each neighbor of the current node.
            for neighbor, weight in adj[node]:
                # If the distance to the neighbor is less than the current distance, update it.
                if dist[neighbor] > dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
        return dist


if __name__ == '__main__':

    sol = Solution()


    # Test 1
    V = 2
    adj = [[[1, 9]], [[0, 9]]]
    S=0
    print(sol.dijkstraUsingHeap(V, adj, S))  # Expected output: [0, 9]
    print(sol.dijkstraUsingSet(V, adj, S))  # Expected output: [0, 9]

    # Test 2
    V = 3
    adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
    S=2
    print(sol.dijkstraUsingHeap(V, adj, S))  # Expected output: [4, 3, 0]
    print(sol.dijkstraUsingSet(V, adj, S))  # Expected output: [4, 3, 0]
