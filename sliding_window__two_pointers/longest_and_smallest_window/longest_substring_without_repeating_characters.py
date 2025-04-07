# Longest Substring Without Repeating Characters

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubStringLen = 0
        currSubString = {}
        currSubStringLen = 0
        for i in range(len(s)):
            # If the character is not in the current substring, add it to the substring
            if s[i] not in currSubString:
                currSubString[s[i]] = i
                currSubStringLen += 1
            # If the character is in the current substring, update the substring
            else:
                # Update the max substring length
                l = currSubString[s[i]]
                currSubString = {}
                currSubStringLen = 0
                # Add the characters from the last repeating character to the current character
                for j in range(l+1, i):
                    currSubString[s[j]] = j
                    currSubStringLen += 1
                currSubStringLen += 1
                currSubString[s[i]] = i

            maxSubStringLen = max(maxSubStringLen, currSubStringLen)
        return maxSubStringLen

from collections import Counter


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


"""
1. Initialize variables:
 • Set n as the length of the string.
 • Set ans (the longest unique substring length found so far) to 0.
 • Create an empty dictionary (charToNextIndex) to map characters to the next allowed starting index for the sliding window.
 • Set pointer i (start of the window) to 0.

2. Iterate throughthe string with pointer j (end of the window):
 • For each character at position j:
  a. Check if the character has been seen before:
   – If yes, update i to the maximum of its current value and the stored dictionary value for that character. This ensures the sliding window only contains unique characters.
  b. Compute the current window length as (j - i + 1) and update ans if this length is greater.
  c. Save or update the dictionary entry for the character with j + 1 (indicating that if this character is seen again, the new window should start right after j).

3. After the loop ends, return ans as the length of the longest substring without repeating characters.

"""

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans
