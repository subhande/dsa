# Subset sum equals to target
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        prev = [False] * (target + 1)

        prev[0] = True

        if arr[0] <= target:
            prev[arr[0]] = True

        for ind in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True
            for i in range(1, target + 1):
                notTaken = prev[i]
                taken = False
                if arr[ind] <= i:
                    taken = prev[i - arr[ind]]
                curr[i] = notTaken or taken
            prev = curr[:]
        return prev[target]
