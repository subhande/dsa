# String Compression

from typing import List


# Time Complexity: O(n) | Space Complexity: O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:

        string_length = 0
        current_char_count = 1
        insert_index = 0
        for i in range(1, len(chars)):
            if chars[i - 1] == chars[i]:
                current_char_count += 1
            else:
                temp = (
                    chars[i - 1] + str(current_char_count)
                    if current_char_count > 1
                    else chars[i - 1]
                )
                string_length += len(temp)
                for ch in temp:
                    chars[insert_index] = ch
                    insert_index += 1
                current_char_count = 1
        temp = (
            chars[-1] + str(current_char_count) if current_char_count > 1 else chars[-1]
        )
        string_length += len(temp)
        for ch in temp:
            chars[insert_index] = ch
            insert_index += 1
        return string_length
