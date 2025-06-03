# Minimum Window Substring

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If either string is empty, return an empty string (no window possible)
        if not t or not s:
            return ""

        # Count the frequency of each character in t
        dict_t = Counter(t)

        # Number of unique characters in t that must be present in the window
        required = len(dict_t)

        # Left and right pointers for the window
        left, right = 0, 0
        # Number of unique characters in the current window that match the required count in t
        formed = 0
        # Dictionary to keep count of all characters in the current window
        window_counts = {}
        # Track the size of the smallest window found so far
        minWindowSize = float("inf")
        # Track the starting index of the smallest window
        windowStartIdx = 0

        # Start sliding the right pointer
        while right < len(s):
            character = s[right]
            # Add the current character to the window count
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the current character's count matches its count in t, increment 'formed'
            if (
                character in dict_t
                and window_counts[character] == dict_t[character]
            ):
                formed += 1

            # Try to contract the window until it ceases to be 'desirable'
            while left <= right and formed == required:
                character = s[left]
                # Update the minimum window if the current window is smaller
                if right - left + 1 < minWindowSize:
                    minWindowSize = right - left + 1
                    windowStartIdx = left
                # Remove the leftmost character from the window
                window_counts[character] -= 1

                # If the removed character is required and its count falls below the required count, decrement 'formed'
                # This will execute once in the loop at the last iteration after the while loop will break
                if (
                    character in dict_t
                    and window_counts[character] < dict_t[character]
                ):
                    formed -= 1
                # Move the left pointer forward to try and find a smaller window
                left += 1
            # Expand the window by moving the right pointer forward
            right += 1

        # Return the smallest window, or an empty string if no such window exists
        return "" if minWindowSize == float("inf") else s[windowStartIdx : windowStartIdx+minWindowSize]
