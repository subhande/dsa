# Course Schedule
# https://leetcode.com/problems/course-schedule/
# https://takeuforward.org/plus/dsa/graph/hard-problems/course-schedule-i


from collections import deque
from typing import List
class Solution:

    def topoSort(self, adj, V):
        inDegree = [0] * V

        for node in range(V):
            for neighbour in adj[node]:
                inDegree[neighbour] += 1

        queue = deque()
        for node in range(V):
            if inDegree[node] == 0:
                queue.append(node)


        topologicalOrder = []
        while queue:
            node = queue.popleft()
            topologicalOrder.append(node)
            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        return topologicalOrder if len(topologicalOrder) == V else []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        return self.topoSort(adj, numCourses)


class Solution2:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        V = numCourses

        inDegree = [0] * V

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            inDegree[prerequisite[0]] += 1

        queue = deque()
        for node in range(V):
            if inDegree[node] == 0:
                queue.append(node)

        topologicalOrder = []
        while queue:
            node = queue.popleft()
            topologicalOrder.append(node)
            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)

        return topologicalOrder if len(topologicalOrder) == V else []
