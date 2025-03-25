# Number of Substrings Containing All Three Characters


from collections import defaultdict
class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = 0
        validSubstringCount = 0
        length = len(s)
        targetSet = {"a", "b", "c"}
        freqMap = defaultdict(int)
        while right < length:
            ch = s[right]
            freqMap[ch] += 1
            if ch in targetSet:
                targetSet.remove(ch)
            while len(targetSet) == 0:
                validSubstringCount += length - right
                ch = s[left]
                freqMap[ch] -= 1
                left += 1
                if freqMap[ch] == 0:
                    targetSet.add(ch)
            right += 1
        return validSubstringCount


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = total = 0
        # Track frequency of a, b, c
        freq = [0] * 3

        while right < len(s):
            # Add character at right pointer to frequency array
            freq[ord(s[right]) - ord("a")] += 1

            # While we have all required characters
            while self._has_all_chars(freq):
                # All substrings from current window to end are valid
                # Add count of valid substrings
                total += len(s) - right

                # Remove leftmost character and move left pointer
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return total

    def _has_all_chars(self, freq: list) -> bool:
        # Check if we have at least one of each character
        return all(f > 0 for f in freq)
