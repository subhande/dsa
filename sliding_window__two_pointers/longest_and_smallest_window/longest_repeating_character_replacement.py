# Longest Repeating Character Replacement

from collections import defaultdict


#  Time Complexity: O(26 * n) where n is the length of input string s | Space Complexity: O(26) since we are storing frequency of characters in current window which can have at most 26 characters
class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the sliding window pointers
        left = right = 0
        # Dictionary to keep track of character frequencies in the current window
        characterFreqMap = defaultdict(int)
        n = len(s)
        maxLen = 0  # Stores the length of the longest valid window found

        # Expand the window by moving the right pointer
        while right < n:
            # Increment the frequency of the current character
            characterFreqMap[s[right]] += 1
            # Update the max frequency in the current window
            maxFreq = max(
                characterFreqMap.values()
            )  # Get the count of the most frequent character

            # If the number of characters to change exceeds k, shrink the window from the left
            # We can also use while here
            if right - left + 1 - maxFreq > k:
                characterFreqMap[s[left]] -= 1
                left += 1  # Move the left pointer to the right

            # Update the maximum length found so far
            maxLen = max(maxLen, right - left + 1)
            right += 1  # Move the right pointer to the right

        return maxLen  # Return the length of the longest valid window


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the sliding window pointers
        left = right = 0
        # Dictionary to keep track of character frequencies in the current window
        characterFreqMap = defaultdict(int)
        n = len(s)
        maxLen = 0  # Stores the length of the longest valid window found
        maxFreq = (
            0  # Stores the count of the most frequent character in the current window
        )

        # Expand the window by moving the right pointer
        while right < n:
            # Increment the frequency of the current character
            characterFreqMap[s[right]] += 1
            # Update the max frequency in the current window
            maxFreq = max(maxFreq, characterFreqMap[s[right]])

            # If the number of characters to change exceeds k, shrink the window from the left
            # Here we can while but it will also run only once since we are only reducing the frequency of one character at a time
            if right - left + 1 - maxFreq > k:
                characterFreqMap[s[left]] -= 1
                left += 1  # Move the left pointer to the right

            # Here we are not reducing the maxFreq when we shrink the window because it will not affect the validity of the window. We are shrinking only one character at a time and to get a larger size valid window we need to have a larger maxFreq which can only be achieved by adding more characters to the right and not by removing characters from the left. So we can keep the maxFreq as it is even when we shrink the window from the left.

            # Update the maximum length found so far
            maxLen = max(maxLen, right - left + 1)
            right += 1  # Move the right pointer to the right

        return maxLen  # Return the length of the longest valid window


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    solution = Solution1()
    print(solution.characterReplacement(s, k))  # Output: 4
