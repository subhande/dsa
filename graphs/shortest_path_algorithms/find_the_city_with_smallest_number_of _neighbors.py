# Find the city with smallest number of neighbors
# https://takeuforward.org/plus/dsa/graph/shortest-path-algorithms/find-the-city-with-the-smallest-number-of-neighbors
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

from typing import List

class Solution:
    def shortestPathFloyedWarshall(self, matrix):
        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float("inf")
        matrix = [[INF] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0
        for edge in edges:
            matrix[edge[0]][edge[1]] = edge[2]
            matrix[edge[1]][edge[0]] = edge[2]
        self.shortestPathFloyedWarshall(matrix)
        minNeighbors = INF
        res = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold:
                    count += 1
            if count <= minNeighbors:
                minNeighbors = count
                res = i
        return res
