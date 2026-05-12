from collections import defaultdict


# Approach 1: Hash Map
# Time Complexity: O(n) | Space Complexity: O(1) (assuming a fixed character set)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Dictionary to store frequency of occurrence of each character
        frequency_map = defaultdict(int)

        # Count frequencies
        for ch in s:
            frequency_map[ch] += 1

        length = 0
        has_odd_frequency = False
        for ch, count in frequency_map.items():
            if count % 2 == 1:
                # If the frequency is odd, one occurrence of the
                # character will remain without a match
                length += count - 1
                has_odd_frequency = True
            else:
                # Check if the frequency is even
                length += count

        # If has_odd_frequency is true, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if has_odd_frequency:
            length += 1

        return length


# Time Complexity: O(n) | Space Complexity: O(1)
class Solution2:
    def longestPalindrome(self, s: str) -> int:
        odd_freq_chars_count = 0
        frequency_map = {}

        # Loop over the string
        for c in s:
            # Update count of current character
            frequency_map[c] = frequency_map.get(c, 0) + 1

            # If the current frequency of the character is odd,
            # increment odd_freq_chars_count
            if frequency_map[c] % 2 == 1:
                odd_freq_chars_count += 1
            else:
                odd_freq_chars_count -= 1

        # If there are characters with odd frequencies, we are
        # guaranteed to have at least one letter left unmatched,
        # which can make the center of an odd length palindrome.
        if odd_freq_chars_count > 0:
            return len(s) - odd_freq_chars_count + 1
        else:
            return len(s)
