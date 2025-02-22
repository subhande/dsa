# Longest word with all prefixes

class TrieNode:
    def __init__(self):
        # To store references to child nodes
        self.links = [None] * 26
        # Flag to indicate end of a word
        self.flag = False

    # Checks if the current character link exists
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Returns the next node corresponding to the character
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    # Creates a link to the next node for the current character
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Marks the end of a word
    def setEnd(self):
        self.flag = True

    # Checks if the current node is the end of a word
    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        # Constructor to initialize the Trie with an empty root node
        self.root = TrieNode()

    # Time complexity: O(m), where m is the length of the word
    # Inserts a word into the Trie
    def insert(self, word):
        # Start at the root node
        node = self.root
        # Iterate over each letter in the word
        for ch in word:
            # If the current node does not contain the letter
            if not node.containsKey(ch):
                # Insert a new node
                node.put(ch, TrieNode())
            # Move to the next node
            node = node.get(ch)
        # Mark the end of the word
        node.setEnd()

    # Time complexity: O(m), where m is the length of the word
    # Check if all prefix of a word exist or not
    def checkIfAllPrefixExists(self, word):
        # Start at the root node
        node = self.root
        # Iterate over each letter in the word
        for ch in word:
            # If the current node does not contain the letter
            if not node.containsKey(ch):
                # If a prefix is not found,
                # the word is not in the Trie
                return False
            # Move to the next node
            node = node.get(ch)
            # Check if the current node marks the end of a word
            if not node.isEnd():
                # If the current node is not the end of a word
                # then a prefix is missing
                return False
        # All prefixes exist
        return True



class Solution:
    # Time complexity: O(n*m), where n is the number of words and m is the length of the longest word
    def completeString(self, nums):
        # Initialize the Trie
        trie = Trie()
        # Insert all words into the Trie
        for word in nums:
            trie.insert(word)
        # Initialize the longest word
        longest_word = ""
        # Iterate over each word
        for word in nums:
            # Check if all prefixes of the word exist
            if trie.checkIfAllPrefixExists(word):
                # Update the longest word if the current word is longer
                if len(word) > len(longest_word):
                    longest_word = word
                elif len(word) == len(longest_word) and word < longest_word:
                    longest_word = word  # Lexicographically smaller word
        return longest_word if longest_word else "None"


if __name__ == "__main__":
    # Initialize the solution
    solution = Solution()

    # Test 1
    nums = [ "n", "ni", "nin", "ninj" , "ninja" , "nil" ]
    # Get the longest word with all prefixes
    result = solution.completeString(nums)
    print(result)  # Output: "ninja"

    # Test 1
    nums =  [ "ninja" , "night" , "nil" ]
    # Get the longest word with all prefixes
    result = solution.completeString(nums)
    print(result)  # Output: None
