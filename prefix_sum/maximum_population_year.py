# 1604. Maximum Population Year

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        population = [0] * (2051 - 1950)

        n = 101

        for log in logs:
            population[log[0] - 1950] += 1
            population[log[1] - 1950] -= 1

        maxPopulation = float("-inf")
        maxPopulationYear = 0

        for i in range(len(population)):
            population[i] += population[i - 1] if i != 0 else 0

            if population[i] > maxPopulation:
                maxPopulation = population[i]
                maxPopulationYear = i + 1950

        return maxPopulationYear
