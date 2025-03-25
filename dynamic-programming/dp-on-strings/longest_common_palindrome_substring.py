# Longest common palindromic substring
# https://leetcode.com/problems/longest-palindromic-substring/?envType=company&envId=google&favoriteSlug=google-three-months


class Solution:
    def longestPalindromeSubstringBruteForce(self, input_string: str) -> str:
        string_length = len(input_string)
        longest_palindrome = ""
        # Iterate over possible substring lengths, starting from the full string length
        for substring_length in range(string_length, 0, -1):
            # Slide a window of size 'substring_length' across the string
            for start_index in range(string_length - substring_length + 1):
                candidate_substring = input_string[start_index:start_index + substring_length]
                # Check if the candidate substring is a palindrome
                if candidate_substring == candidate_substring[::-1]:
                    # As we iterate from longest to shortest, return the first palindrome found
                    return candidate_substring
        return longest_palindrome

    def longestPalindromeSubstringOptimal(self, s: str) -> str:
        # Using DP
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] will be True if s[i:j+1] is a palindrome
        dp = [[False] * (n+1) for _ in range(n+1)]
        start, max_len = 0, 1

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 1
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    start = i
                    max_len = length

        return s[start:start+max_len]


    def longestPalindrome(self, s: str) -> str:
        dp = {"": True}
        if len(s) == 1:
            return s
        for ch in s:
            dp[ch] = True
        max_str_size = 1
        max_str = s[0]
        n = len(s)
        for length in range(2, n+1):
            for start in range(n-length+1):
                start_ch = s[start]
                end = start + length - 1
                end_ch = s[end]
                if start_ch == end_ch and dp.get(s[start+1:end]) is True:
                    temp = s[start:end+1]
                    dp[temp] = True
                    if len(temp) > max_str_size:
                        max_str_size = len(temp)
                        max_str = temp
        return max_str



if __name__ == "__main__":

    sol = Solution()

    # Test 1
    s = "babad"
    expected_output = "aba"
    print(f"Expected output: {expected_output}")
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))
    print(sol.longestPalindrome(s))
    print("==================================")

    # Test 2
    s = "cbbd"
    expected_output = "bb"
    print(f"Expected output: {expected_output}")
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))
    print(sol.longestPalindrome(s))
    print("==================================")

    # Test 3
    s = "ac"
    expected_output = "a"
    print(f"Expected output: {expected_output}")
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))
    print(sol.longestPalindrome(s))
    print("==================================")

    # Test 4
    s = "bb"
    expected_output = "bb"
    print(f"Expected output: {expected_output}")
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))
    print(sol.longestPalindrome(s))
    print("==================================")

    # Test 5
    s = "abb"
    expected_output = "bb"
    print(f"Expected output: {expected_output}")
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))
    print(sol.longestPalindrome(s))
    print("==================================")

    # Test 4
    s = "aacabdkacaa"
    expected_output = "aca"
    print(f"Expected output: {expected_output}")
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))
    print(sol.longestPalindrome(s))
    print("==================================")
