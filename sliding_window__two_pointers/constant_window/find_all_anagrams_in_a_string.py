from typing import List


# Approach 1: Brute Force
# Time Complexity: O(n * m) where n is the length of string s and m is the length of pattern p | Space Complexity: O(m) where m is the length of pattern p
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Store frequency of each character in pattern string p
        pattern_frequency = {}

        # List to store starting indices of anagrams
        anagram_indices = []

        for char in p:
            if char not in pattern_frequency:
                pattern_frequency[char] = 0
            pattern_frequency[char] += 1

        string_length = len(s)
        pattern_length = len(p)

        # Check every substring of length pattern_length
        for start_index in range(string_length - pattern_length + 1):
            # Create a fresh copy of pattern frequency map
            remaining_frequency = pattern_frequency.copy()

            # Try to match characters of current window
            for current_index in range(start_index, start_index + pattern_length):
                current_char = s[current_index]

                # Character not present in pattern
                if current_char not in remaining_frequency:
                    break

                remaining_frequency[current_char] -= 1

                # Character appears more times than allowed
                if remaining_frequency[current_char] < 0:
                    break

            # Verify all required characters were matched exactly
            is_anagram = True

            for _, count in remaining_frequency.items():
                if count != 0:
                    is_anagram = False
                    break

            if is_anagram:
                anagram_indices.append(start_index)

        return anagram_indices


# Approach 2: Optimized using Sliding Window
# Time Complexity: O(n) where n is the length of string s | Space Complexity: O(m) where m is the length of pattern p
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Frequency map of characters required from pattern p
        pattern_frequency = {}
        for char in p:
            pattern_frequency[char] = pattern_frequency.get(char, 0) + 1

        # Number of characters still needed to form an anagram
        remaining_characters = len(p)

        # Left pointer of the sliding window
        window_start = 0

        # Stores starting indices of all anagrams
        anagram_start_indices = []

        # Expand the window by moving window_end
        for window_end in range(len(s)):
            current_char = s[window_end]

            # Process the incoming character
            if current_char in pattern_frequency:
                # If frequency is positive, this character was needed
                if pattern_frequency[current_char] > 0:
                    remaining_characters -= 1

                # Decrease frequency to mark usage
                pattern_frequency[current_char] -= 1

            # Shrink the window if its size exceeds len(p)
            if window_end - window_start + 1 > len(p):
                outgoing_char = s[window_start]

                if outgoing_char in pattern_frequency:
                    # Restore the frequency since the character
                    # is leaving the window
                    pattern_frequency[outgoing_char] += 1

                    # If frequency becomes positive, the window
                    # is now missing one required character
                    if pattern_frequency[outgoing_char] > 0:
                        remaining_characters += 1

                window_start += 1

            # If window size equals len(p) and all required
            # characters have been matched, we found an anagram
            if window_end - window_start + 1 == len(p) and remaining_characters == 0:
                anagram_start_indices.append(window_start)

        return anagram_start_indices
