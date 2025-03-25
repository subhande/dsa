# Maximum Points You Can Obtain from Cards

from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        cardPoints = cardPoints[-k:] + cardPoints[:k]
        n = len(cardPoints)
        currSum = sum(cardPoints[:k])
        maxSum = currSum
        left = 0
        right = k-1

        while right < n-1:
            currSum -= cardPoints[left]
            left += 1
            right += 1
            currSum += cardPoints[right]
            maxSum = max(maxSum, currSum)
        return maxSum

    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        leftSum = 0
        rightSum = 0
        maxSum = 0

        leftSum = sum(cardPoints[:k])
        maxSum = leftSum

        rightIndex = len(cardPoints) - 1

        for i in range(k-1, -1, -1):
            leftSum -= cardPoints[i]
            rightSum += cardPoints[rightIndex]
            rightIndex -= 1
            maxSum = max(maxSum, leftSum + rightSum)
        return maxSum
