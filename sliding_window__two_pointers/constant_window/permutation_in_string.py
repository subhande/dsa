# Permutation in String
# Time Complexity: O(n) | Space Complexity:O(1) since we are only storing frequency of characters in pattern string p which can have at most 26 characters


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        pattern_frequency = {}

        for ch in s1:
            pattern_frequency[ch] = pattern_frequency.get(ch, 0) + 1

        window_length = len(s1)

        window_start = 0

        remaining_characters = window_length

        for window_end in range(len(s2)):
            current_char = s2[window_end]

            if current_char in pattern_frequency:
                if pattern_frequency[current_char] > 0:
                    remaining_characters -= 1
                pattern_frequency[current_char] -= 1

            if window_end - window_start + 1 > window_length:
                outgoing_char = s2[window_start]

                if outgoing_char in pattern_frequency:
                    pattern_frequency[outgoing_char] += 1

                    if pattern_frequency[outgoing_char] > 0:
                        remaining_characters += 1
                window_start += 1

            if (
                window_end - window_start + 1 == window_length
                and remaining_characters == 0
            ):
                return True
        return False
