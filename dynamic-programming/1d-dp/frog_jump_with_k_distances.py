# Frog jump with K distances
# https://takeuforward.org/plus/dsa/dynamic-programming/1d-dp/frog-jump-with-k-distances


class Solution:
    def frogJump(self, heights, k):
        totalSteps = len(heights)
        INF = float("inf")
        energy = [INF] * totalSteps
        energy[0] = 0
        for currentStep in range(1, totalSteps):
            for step_back in range(currentStep-1, max(currentStep-k-1, -1), -1):
                energy[currentStep] = min(
                    energy[currentStep],
                    energy[step_back] + abs(heights[currentStep]-heights[step_back])
                )
        return energy[-1]
