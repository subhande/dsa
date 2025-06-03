from typing import List

class Solution:
    def maxScoreSlidingWindow(self, card_points: List[int], k: int) -> int:
        """
        Calculates the maximum score by picking k cards from either end using a sliding window.

        Approach:
        - Concatenate the last k and first k cards to simulate all possible combinations.
        - Use a sliding window of size k to find the maximum sum.

        Args:
            card_points (List[int]): List of integers representing points on each card.
            k (int): Number of cards to pick.

        Returns:
            int: Maximum score possible.
        """
        # Form a window that can slide across both ends
        window = card_points[-k:] + card_points[:k]
        n = len(window)
        current_window_sum = sum(window[:k])
        max_score = current_window_sum
        left = 0
        right = k - 1

        # Slide the window to the right and update max_score
        while right < n - 1:
            current_window_sum -= window[left]
            left += 1
            right += 1
            current_window_sum += window[right]
            max_score = max(max_score, current_window_sum)
        return max_score

    def maxScorePrefixSuffix(self, card_points: List[int], k: int) -> int:
        """
        Calculates the maximum score by considering all combinations of prefix (from start)
        and suffix (from end) cards.

        Approach:
        - Take i cards from the start and (k-i) cards from the end for all i in [0, k].
        - Track the maximum sum among all these splits.

        Args:
            card_points (List[int]): List of integers representing points on each card.
            k (int): Number of cards to pick.

        Returns:
            int: Maximum score possible.
        """
        left_sum = sum(card_points[:k])  # Take all k cards from the start initially
        max_score = left_sum
        right_sum = 0
        right_pointer = len(card_points) - 1

        # Shift cards from the left side to the right side, one by one
        for i in range(k - 1, -1, -1):
            left_sum -= card_points[i]      # Remove one card from the left
            right_sum += card_points[right_pointer]  # Add one card from the right
            right_pointer -= 1
            max_score = max(max_score, left_sum + right_sum)
        return max_score
