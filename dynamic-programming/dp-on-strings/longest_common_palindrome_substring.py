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
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Fill the DP table:
        # We consider all substrings by varying the end index (j)
        for j in range(2, n): # String Length
            for i in range(n-j): # Start Index
                # If the current substring is of length 2 or 3,
                # then it's a palindrome if the end characters match.
                # # Else, it is a palindrome only if the substring inside is also a palindrome.
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False

                # Update the maximum length palindrome found so far.
                if dp[i][j] and (j - i + 1) > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start+max_len]





if __name__ == "__main__":

    sol = Solution()

    # Test 1
    s = "babad"
    # Expected output: "aba"
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))

    # Test 2
    s = "cbbd"
    # Expected output: "bb"
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))

    # Test 3
    s = "ac"
    # Expected output: "a"
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))

    # Test 4
    s = "aacabdkacaa"
    # Expected output: "aca"
    print(sol.longestPalindromeSubstringBruteForce(s))
    print(sol.longestPalindromeSubstringOptimal(s))
