import collections
from typing import List

"""

# Problem: Substring with Concatenation of All Words

s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]
#
#

- All words are of the same length
- No string in words is a substring of another string in words

possible combinations n! -> no of words < 5000 -> 5000! is a very large number -> we need to optimize
Generating all possible combinations of words and then checking if they are present in the string s would be inefficient. Instead, we can use a hash table to store the frequency of each word in the list of words and then check for valid substrings in the string s.
-------
barfoo
foobar
------

"""


# Approach 1: Check All Indices Using a Hash Table
# n -> length of string s, k -> number of words, m -> length of each word
# Time Complexity: O(n * k * m - (k m)^2) where n is the length of string s, k is the number of words and m is the length of each word | Space Complexity: O(m + k) where m is the length of each word and k is the number of words
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j : j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer


# Approach 2: Optimized Using Sliding Window
"""
Instead of checking every possible substring independently, this solution maintains a word-frequency sliding window:

Move right one word at a time.
Keep frequencies in words_found.
Track whether a word appears too many times using excess_word.
Shrink from the left whenever:
the window becomes too large, or
a word frequency exceeds its allowed count.
When exactly k valid words are present, record the starting index.
"""

# Time Complexity: O(n * m) where n is the length of string s and m is the length of each word | Space Complexity: O(m + k) where m is the length of each word and k is the number of words


class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        total_string_length = len(s)
        total_words = len(words)
        word_length = len(words[0])

        # Total length of a valid concatenated substring
        required_window_size = total_words * word_length

        # Frequency map of the required words
        required_word_count = collections.Counter(words)

        result = []

        def sliding_window(start_offset: int):
            """
            Process one alignment of the string.

            Example for word_length = 3:

            Offset 0: abc | def | ghi
            Offset 1: bcd | efg | hi
            Offset 2: cde | fgh | i

            A valid answer can belong to any one of these alignments,
            so we run a separate sliding window for each offset.
            """

            left = start_offset

            # Frequency map of words currently inside the window
            window_word_count = collections.defaultdict(int)

            # Number of words currently contributing toward a valid solution
            matched_words = 0

            # Indicates whether some word appears more times than allowed
            has_excess_word = False

            # Move right pointer one word at a time
            for right in range(start_offset, total_string_length, word_length):
                # Not enough characters left to form a complete word
                if right + word_length > total_string_length:
                    break

                current_word = s[right : right + word_length]

                # ----------------------------------------------------------
                # Case 1:
                # Current word is not part of the required words.
                #
                # Example:
                # required = ["foo", "bar"]
                # window = foo | xyz
                #
                # Reset the entire window because no valid substring can
                # include an invalid word.
                # ----------------------------------------------------------
                if current_word not in required_word_count:
                    window_word_count.clear()
                    matched_words = 0
                    has_excess_word = False

                    # Start a new window after the invalid word
                    left = right + word_length
                    continue

                # ----------------------------------------------------------
                # Shrink the window when:
                #
                # 1. Window already contains the maximum allowed size
                #    (total_words words)
                #
                # OR
                #
                # 2. Some word appears more times than required.
                # ----------------------------------------------------------
                while right - left == required_window_size or has_excess_word:
                    leftmost_word = s[left : left + word_length]

                    # Remove leftmost word from the window
                    window_word_count[leftmost_word] -= 1
                    left += word_length

                    # If frequency becomes exactly equal to requirement,
                    # we just removed the excess occurrence.
                    if (
                        window_word_count[leftmost_word]
                        == required_word_count[leftmost_word]
                    ):
                        has_excess_word = False
                    else:
                        # We removed a word that was contributing toward
                        # a valid answer.
                        matched_words -= 1

                # Add current word into the window
                window_word_count[current_word] += 1

                # ----------------------------------------------------------
                # If frequency is still within the required limit,
                # count it as a matched word.
                # ----------------------------------------------------------
                if window_word_count[current_word] <= required_word_count[current_word]:
                    matched_words += 1
                else:
                    # Current word now appears too many times
                    has_excess_word = True

                # ----------------------------------------------------------
                # Found a valid window:
                #
                # - All required words are matched
                # - No word exceeds its allowed frequency
                # ----------------------------------------------------------
                if matched_words == total_words and not has_excess_word:
                    result.append(left)

        # Run one sliding window for each possible alignment
        for offset in range(word_length):
            sliding_window(offset)

        return result
