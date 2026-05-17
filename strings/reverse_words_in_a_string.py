class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution2:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s[::-1].split()])


# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
from typing import List


class Solution3:
    def reverse(self, chars: List[str], left: int, right: int) -> None:
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    def reverseWords(self, s: str) -> str:
        chars = list(s)

        # Step 1: Reverse the whole string.
        # Example: "  hello world  " becomes "  dlrow olleh  "
        self.reverse(chars, 0, len(chars) - 1)

        # Step 2: Clean spaces in-place.
        # This removes leading/trailing spaces and changes multiple spaces to one.
        write_index = 0
        read_index = 0
        while read_index < len(chars):
            # Skip leading spaces.
            while read_index < len(chars) and chars[read_index] == " ":
                read_index += 1

            # If we've reached the end of the string after skipping spaces, break out of the loop.
            if read_index == len(chars):
                break

            # If this is not the first word, add a single space before the next word.
            if write_index > 0:
                chars[write_index] = " "
                write_index += 1

            # Copy the next word.
            while read_index < len(chars) and chars[read_index] != " ":
                chars[write_index] = chars[read_index]
                write_index += 1
                read_index += 1

        # Step 3: Reverse each word to restore the word's character order.
        word_start = 0
        for word_end in range(write_index + 1):
            if word_end == write_index or chars[word_end] == " ":
                self.reverse(chars, word_start, word_end - 1)
                word_start = word_end + 1

        return "".join(chars[:write_index])
