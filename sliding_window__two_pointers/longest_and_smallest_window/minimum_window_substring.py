# Minimum Window Substring

from collections import Counter

"""
Explanation of Minimum Window Substring

This solves the classic problem: *given strings `s` and `t`, find the smallest substring of `s` that contains all characters of `t`.*

### Core Idea

Use a **sliding window** with two pointers (`left` and `right`) that define a substring of `s`. Expand the window to include required characters, then shrink it to find the smallest valid window.

### Step-by-step Walkthrough

1. **Setup:** Count every character's frequency in `t` (e.g., `t = "ABC"` → `{A:1, B:1, C:1}`). The variable `required` stores how many *unique* characters need to be satisfied.

2. **Expand (right pointer):** Move `right` forward one character at a time, adding it to `window_counts`. Each time a character's window count *exactly matches* its count in `t`, increment `formed`. Once `formed == required`, the window contains all of `t`'s characters at the needed frequencies — it's a valid window.

3. **Contract (left pointer):** While the window is still valid, try shrinking it from the left to find a smaller answer. Record the window size if it's the smallest so far, then remove the leftmost character. If removing it causes its count to drop below what `t` needs, decrement `formed`, which breaks the inner loop.

4. **Repeat** until `right` reaches the end of `s`.

### Why It Works

- The outer loop guarantees every possible right boundary is tried.
- The inner loop guarantees that for each right boundary, the left boundary is pushed as far right as possible while staying valid.
- This means every minimal valid window is considered exactly once.

### Time & Space Complexity

- **Time:** O(|s| + |t|) — each pointer moves at most |s| times, so the work is linear.
- **Space:** O(|s| + |t|) — for the two frequency dictionaries.

### Quick Example

For `s = "ADOBECODEBANC"`, `t = "ABC"`:

- The window expands until it first contains A, B, and C → `"ADOBEC"`.
- It contracts from the left, removing A → no longer valid, so it expands again.
- Eventually it finds `"BANC"` (length 4), which is the smallest valid window.

"""


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
            if character in dict_t and window_counts[character] == dict_t[character]:
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
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                # Move the left pointer forward to try and find a smaller window
                left += 1
            # Expand the window by moving the right pointer forward
            right += 1

        # Return the smallest window, or an empty string if no such window exists
        return (
            ""
            if minWindowSize == float("inf")
            else s[windowStartIdx : windowStartIdx + minWindowSize]
        )
