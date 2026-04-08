# Longest Substring Without Repeating Characters

# Time Complexity: O(n) | Space Complexity: O(k) where k is the number of unique characters in the string.
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
                for j in range(l + 1, i):
                    currSubString[s[j]] = j
                    currSubStringLen += 1
                currSubStringLen += 1
                currSubString[s[i]] = i

            maxSubStringLen = max(maxSubStringLen, currSubStringLen)
        return maxSubStringLen


from collections import Counter


# Time Complexity: O(n) | Space Complexity: O(k) where k is the number of unique characters in the current window.
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            # Expand the window by moving right pointer and adding the character to the counter
            rightValue = s[right]
            chars[rightValue] += 1

            # If the count of the current character is greater than 1, it means we have a duplicate character in the window. We need to shrink the window from the left until we remove the duplicate character.
            # Note: Here we need while if will not work
            # e.g. pww -> we need to move left pointer twice to remove the duplicate character 'w'
            # if we use if, we will only move left pointer once and we will still have duplicate character 'w' in the window
            while chars[rightValue] > 1:
                leftValue = s[left]
                chars[leftValue] -= 1
                left += 1

            # Update the result with the maximum length of the current window
            res = max(res, right - left + 1)

            # Move the right pointer to expand the window
            right += 1

        return res


# Time Complexity: O(n * k) where n is the length of the string and k is the number of unique characters in the current window. | Space Complexity: O(k) where k is the number of unique characters in the current window.
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            # Expand the window by moving right pointer and adding the character to the counter
            rightValue = s[right]
            chars[rightValue] += 1

            # If the count of the current character is greater than 1, it means we have a duplicate character in the window. We need to shrink the window from the left until we remove the duplicate character.
            if sum(chars.values()) > len(chars):
                leftValue = s[left]
                chars[leftValue] -= 1
                left += 1
                if chars[leftValue] == 0:
                    chars.pop(leftValue)

            # Update the result with the maximum length of the current window
            res = max(res, right - left + 1)

            # Move the right pointer to expand the window
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


# Time Complexity: O(n) | Space Complexity: O(k) where k is the number of unique characters in the string.
class Solution4:
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


if __name__ == "__main__":
    s = "pwwkew"
    print(Solution1().lengthOfLongestSubstring(s))
    print(Solution2().lengthOfLongestSubstring(s))
    print(Solution3().lengthOfLongestSubstring(s))
    print(Solution4().lengthOfLongestSubstring(s))
