# Ninja's training
# https://takeuforward.org/plus/dsa/dynamic-programming/2d-dp/ninja's-training

class Solution:
    def ninjaTraining(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        INF = float("-inf")
        prev = matrix[0][:]
        max_points = max(prev)
        for i in range(1, n):
            curr = [INF] * m
            curr[0] = max(prev[1], prev[2]) + matrix[i][0]
            curr[1] = max(prev[0], prev[2]) + matrix[i][1]
            curr[2] = max(prev[0], prev[1]) + matrix[i][2]
            max_points = max(max_points, max(curr))
            prev = curr
        return max_points
