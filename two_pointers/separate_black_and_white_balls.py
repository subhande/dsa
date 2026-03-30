# Separate Black and White balls


# Approach 1: Brute Force
class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        s = list(s)
        while True:
            change = False
            for i in range(1, len(s)):
                if s[i - 1] == "1" and s[i] == "0":
                    s[i - 1], s[i] = s[i], s[i - 1]
                    steps += 1
                    change = True
            if change is False:
                break
        return steps


# Approach 2:
# Quick Sort: Pivot -> Move "White" as far left as possible
# Time Comeplexity: O(n) | Space Complexity: O(1)
# Ref: https://www.youtube.com/watch?v=-VVN0FI0KFo
class Solution2:
    def minimumSteps(self, s: str) -> int:
        total_swaps = 0
        white_ball_count = 0

        # Iterate through each ball in the string
        for idx, char in enumerate(s):
            if char == "0":
                # Calculate the number of swaps needed
                total_swaps += idx - white_ball_count
                # Move the next available position for a white ball one step to the right
                white_ball_count += 1
        return total_swaps
