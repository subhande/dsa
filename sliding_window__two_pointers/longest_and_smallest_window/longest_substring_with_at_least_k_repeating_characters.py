# Longest Substring with At Least K Repeating Characters

from collections import Counter, defaultdict


class Solution:
    def longestSubstringHelper(
        self, s: str, start_index: int, end_index: int, k: int
    ) -> int:
        # If the current substring length is smaller than k,
        # it is impossible for any character to appear at least k times.
        if start_index > end_index or end_index - start_index + 1 < k:
            return 0

        # Count character frequencies in the current substring.
        frequency_map = Counter(s[start_index : end_index + 1])

        # Find a character whose frequency is less than k.
        # Such a character cannot be part of any valid substring.
        for split_index in range(start_index, end_index + 1):
            current_char = s[split_index]

            if frequency_map[current_char] < k:
                # Recursively solve the left part.
                longest_left_substring = self.longestSubstringHelper(
                    s, start_index, split_index - 1, k
                )

                # Recursively solve the right part.
                longest_right_substring = self.longestSubstringHelper(
                    s, split_index + 1, end_index, k
                )

                # Return the best answer from both sides.
                return max(longest_left_substring, longest_right_substring)

        # Every character in the current substring appears at least k times.
        # Therefore, the entire substring is valid.
        return end_index - start_index + 1

    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstringHelper(s, 0, len(s) - 1, k)


# The above implementation is straightforward but can be inefficient when there are many characters with frequency less than k, as it may lead to multiple recursive calls for the same indices.
"""
### Core Concept

A normal sliding window cannot directly solve this because we don't know **how many unique characters** the answer contains.

So we:

1. Fix the number of unique characters (`1` to `26`).
2. Use a sliding window to maintain **at most that many unique characters**.
3. Track:

   * `unique_chars` = number of distinct characters in the window.
   * `count_at_least_k` = number of characters whose frequency is at least `k`.
4. When:

```python
unique_chars == target_unique_chars
and
count_at_least_k == target_unique_chars
```

every character in the window appears at least `k` times, so it's a valid substring.

Since there are only 26 lowercase letters, trying all possible unique character counts gives an overall complexity of **O(26 × n) = O(n)**.


"""


# Time Complexity: O(n * 26) where n is the length of the input string s | Space Complexity: O(26) since we are storing frequency of characters in current window which can have at most 26 characters
class Solution2:
    def longestSubstringHelper(
        self, s: str, start_index: int, end_index: int, k: int
    ) -> int:

        # Current substring is too short to be valid.
        if start_index > end_index or end_index - start_index + 1 < k:
            return 0

        # Count frequencies in the current substring.
        frequency_map = Counter(s[start_index : end_index + 1])

        split_index = start_index

        while split_index <= end_index:
            # Found an invalid character.
            if frequency_map[s[split_index]] < k:
                next_valid_index = split_index + 1

                # Skip all consecutive invalid characters.
                while (
                    next_valid_index <= end_index
                    and frequency_map[s[next_valid_index]] < k
                ):
                    next_valid_index += 1

                longest_left_substring = self.longestSubstringHelper(
                    s, start_index, split_index - 1, k
                )

                longest_right_substring = self.longestSubstringHelper(
                    s, next_valid_index, end_index, k
                )

                return max(longest_left_substring, longest_right_substring)

            split_index += 1

        # Every character appears at least k times.
        return end_index - start_index + 1

    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstringHelper(s, 0, len(s) - 1, k)


# Approach 3: Sliding Window with Variable Number of Unique Characters
# Time Complexity: O(n * 26) where n is the length of the input string s | Space Complexity: O(26) since we are storing frequency of characters in current window which


class Solution3:
    def longestSubstring(self, s: str, k: int) -> int:

        longest_substring_length = 0

        # Try all possible counts of unique characters.
        for target_unique_chars in range(1, 27):
            frequency_map = defaultdict(int)

            left = 0

            # Number of unique characters in current window.
            current_unique_chars = 0

            # Number of characters whose frequency >= k.
            chars_with_frequency_at_least_k = 0

            for right in range(len(s)):
                right_char = s[right]

                # New unique character enters the window.
                if frequency_map[right_char] == 0:
                    current_unique_chars += 1

                frequency_map[right_char] += 1

                # Character frequency has just reached k.
                if frequency_map[right_char] == k:
                    chars_with_frequency_at_least_k += 1

                # Shrink window if unique characters exceed target.
                while current_unique_chars > target_unique_chars:
                    left_char = s[left]

                    # Character frequency is about to drop below k.
                    if frequency_map[left_char] == k:
                        chars_with_frequency_at_least_k -= 1

                    frequency_map[left_char] -= 1

                    # Character completely removed from window.
                    if frequency_map[left_char] == 0:
                        current_unique_chars -= 1

                    left += 1

                # Valid window:
                # - Exactly target_unique_chars unique characters.
                # - Every unique character appears at least k times.
                if (
                    current_unique_chars == target_unique_chars
                    and chars_with_frequency_at_least_k == target_unique_chars
                ):
                    longest_substring_length = max(
                        longest_substring_length, right - left + 1
                    )

        return longest_substring_length
