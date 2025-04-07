"""
https://leetcode.com/discuss/post/6381275/google-l4-phone-screen-by-anonymous_user-ript/

Find maximum length of a substring of a string with first charachter lexicographically smaller than its last charachter.

assume string length 10^5 char long, assume 26 small case english letters in string

solve it in linear time.

input : "dbabcb"
output : 4

Similar to: https://leetcode.com/problems/maximum-width-ramp/
"""

# Time complexity: O(n^2) | Space complexity: O(1)
class Solution:
    def maxLenSubstr(self, s: str) -> int:
        """
        Parameters:
            s: str -> input string
        Returns:
            int -> maximum length of substring with first character lexicographically smaller than last character
        """
        max_len = 0
        n = len(s)

        # Iterate through the string
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] < s[j]:
                    max_len = max(max_len, j - i + 1)

        return max_len

# Time complexity: O(26n) | Space complexity: O(1
class Solution2:
    def maxLenSubstr(self, s: str) -> int:
        """
        Parameters:
            s: str -> input string
        Returns:
            int -> maximum length of substring with first character lexicographically smaller than last character
        """
        n = len(s)
        last_pos = [-1 for _ in range(26)]

        for i in range(n):
            pos = ord(s[i])-ord('a')
            last_pos[pos] = i

        max_length = -float('inf')

        for i in range(n):
            pos = ord(s[i])-ord('a')
            last_index = i
            for j in range(pos+1, 26):
                if last_pos[j] > last_index:
                    last_index = last_pos[j]

            curr_length = last_index - i + 1

            if curr_length > max_length:
                max_length = curr_length

        return max_length


# Time complexity: O(n) | Space complexity: O(1)
class Solution3:
    def maxLenSubstr(self, s: str) -> int:
        """
        Parameters:
            s: str -> input string
        Returns:
            int -> maximum length of substring with first character lexicographically smaller than last character
        """
        n = len(s)
        right_max = [-1] * n
        right_max[n - 1] = ord(s[n - 1]) - ord('a')

        # Fill right max char
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], ord(s[i]) - ord('a'))

        print(list(s))
        print([chr(i+ord('a')) for i in right_max])

        start = 0
        end = 0
        max_length = 0
        # Traverse the array using left and right pointers
        while end < n:
            while start < end and ord(s[start])-ord('a') >= right_max[end]:
                start += 1

            max_length = max(max_length, end - start + 1)
            end += 1

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLenSubstr("dbabcb"))  # Output: 4

    sol2 = Solution2()
    print(sol2.maxLenSubstr("dbabcb"))  # Output: 4

    sol3 = Solution3()
    print(sol3.maxLenSubstr("dbabcb"))  # Output: 4
