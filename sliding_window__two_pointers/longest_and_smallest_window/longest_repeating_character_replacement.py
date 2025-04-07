# Longest Repeating Character Replacement


from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        characterFreqMap = defaultdict(int)
        n = len(s)
        maxLen = 0
        maxFreq = 0
        while right < n:
            characterFreqMap[s[right]] += 1
            maxFreq = max(maxFreq, characterFreqMap[s[right]])

            if right - left + 1 - maxFreq > k:
                characterFreqMap[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    solution = Solution()
    print(solution.characterReplacement(s, k))  # Output: 4
