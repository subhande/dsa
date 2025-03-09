# Find the Longest Substring Containing Vowels of Even Count
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/?envType=problem-list-v2&envId=prefix-sum


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        state = {0: -1}
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if prefixXOR not in state:
                state[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - state[prefixXOR])
        return longestSubstring

"""
This solution finds the length of the longest substring in which each vowel (a, e, i, o, u) appears an even number of times. It does so by using bit manipulation to keep track of the parity (even or odd count) of each vowel as it scans through the input string.

Step-by-step explanation:

1. Initialization:
   • prefixXOR is set to 0. This variable will hold a bit-masked representation of the parity state of the vowels.
   • characterMap is a list of size 26 (for each letter of the English alphabet) initialized with zeros.
   • The vowels are then assigned specific bit values:
     - 'a' is assigned 1 (binary 00001)
     - 'e' is assigned 2 (binary 00010)
     - 'i' is assigned 4 (binary 00100)
     - 'o' is assigned 8 (binary 01000)
     - 'u' is assigned 16 (binary 10000)
   • A dictionary called state records the first index at which each unique prefixXOR value is seen. It is initialized with the key 0 mapped to -1. This helps account for the substring starting at index 0.

2. Iterating through the string:
   • For every character in the string (using a loop), the code computes its corresponding value from characterMap.
   • Then, it toggles the bit in prefixXOR using the XOR operator (^). If the character is a vowel, its corresponding bit is flipped from 0 to 1 (or vice versa), effectively updating whether the count of that vowel so far is even or odd.
   • If this new prefixXOR state has not been seen before, it is added to the state dictionary with the current index. This ensures that we always use the earliest index where this state occurred.
   • The length of the longest valid substring ending at the current index is computed by taking the difference between the current index and the first occurrence (stored in the state dictionary) of the same prefixXOR. If the same state is seen again, it means that the counts of vowels between these two indices have all become even.
   • longestSubstring is updated to the maximum of its current value and the length calculated.

3. Return the result:
   • After iterating through the string, the function returns longestSubstring, which represents the length of the longest substring where every vowel appears an even number of times.

Time Complexity:
• The algorithm processes each character of the string exactly once, so the loop is O(n), where n is the length of the string.
• All operations inside the loop (bit manipulation, dictionary access) take O(1) time.
• Thus, the overall time complexity is O(n).

Space Complexity:
• The characterMap array has size 26, which is constant space.
• The dictionary state stores at most 2^5 = 32 different states (since there are 5 vowels, each with a binary state), which is also constant space.
• Hence, the space complexity is O(1).

This approach is both time efficient and space efficient, making it a very elegant solution to the problem.
"""

if __name__ == '__main__':
    obj = Solution()
    s = "eleetminicoworoep"
    print(obj.findTheLongestSubstring(s))
    s = "leetcodeisgreat"
    print(obj.findTheLongestSubstring(s))
    s = "bcbcbc"
    print(obj.findTheLongestSubstring(s))
    s = "aeiou"
    print(obj.findTheLongestSubstring(s))
    s = "aei"
    print(obj.findTheLongestSubstring(s))
    s = "id"
    print(obj.findTheLongestSubstring(s))
