# Find Eventual Safe States
# https://takeuforward.org/plus/dsa/graph/hard-problems/find-eventual-safe-states
# https://leetcode.com/problems/find-eventual-safe-states/


from collections import deque
from typing import List

# Time Complexity: O(V + E) | Space Complexity: O(V)
class Solution:
    def topologicalSort(self, graph, V):
        inDegree = [False] * V

        for node in range(V):
            for neighbour in graph[node]:
                inDegree[neighbour] += 1

        queue = deque()

        for node in range(V):
            if inDegree[node] == 0:
                queue.append(node)

        topoOrder = []
        while queue:
            node = queue.popleft()
            topoOrder.append(node)
            for neighbour in graph[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        return topoOrder


    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        reverseGraph = [[] for i in range(V)]

        for node in range(V):
            for neighbour in graph[node]:
                reverseGraph[neighbour].append(node)

        topoOrder = self.topologicalSort(reverseGraph, V)
        topoOrder.sort()
        return topoOrder


if __name__ == "__main__":
    sol = Solution()
    # Test 1
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    output = [2, 4, 5, 6]
    print(f"Expected output: {output}")
    print(f"Actual output: {sol.eventualSafeNodes(graph)}")

    # Test 2
    graph = [[1, 2], [2, 3], [5], [0], [5], [4], []]
    output = [4, 5, 6]
    print(f"Expected output: {output}")
    print(f"Actual output: {sol.eventualSafeNodes(graph)}")
