# Longest Repeating Character Replacement

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the sliding window pointers
        left = right = 0
        # Dictionary to keep track of character frequencies in the current window
        characterFreqMap = defaultdict(int)
        n = len(s)
        maxLen = 0  # Stores the length of the longest valid window found
        maxFreq = 0  # Stores the count of the most frequent character in the current window

        # Expand the window by moving the right pointer
        while right < n:
            # Increment the frequency of the current character
            characterFreqMap[s[right]] += 1
            # Update the max frequency in the current window
            maxFreq = max(maxFreq, characterFreqMap[s[right]])

            # If the number of characters to change exceeds k, shrink the window from the left
            if right - left + 1 - maxFreq > k:
                characterFreqMap[s[left]] -= 1
                left += 1  # Move the left pointer to the right

            # Update the maximum length found so far
            maxLen = max(maxLen, right - left + 1)
            right += 1  # Move the right pointer to the right

        return maxLen  # Return the length of the longest valid window

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    solution = Solution()
    print(solution.characterReplacement(s, k))  # Output: 4
