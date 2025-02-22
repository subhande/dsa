# Implementing a Trie data structure and its operations

class TrieNode:
    def __init__(self):
        # Array to store links to child nodes
        # each index represents a letter of the alphabet
        self.links = [None] * 26
        # Flag indicating if the node
        # marks the end of a word
        self.flag = False

    # Check if the node contains a specific key(letter)
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Insert a new node with a specific key(letter)
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Get the node with a specific key(letter)
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    # Set the current node as the end of a word
    def setEnd(self):
        self.flag = True

    # Check if the current node marks the end of a word
    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        # Constructor to initialize the Trie with an empty root node
        self.root: TrieNode = TrieNode()

    # Inserts a word into the Trie
    # Time Complexity O(len), where len
    # is the length of the word
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

    # Returns if the word
    # is in the trie
    def search(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # If a letter is not found,
                # the word is not in the Trie
                return False
            # Move to the next node
            node = node.get(ch)
        # Check if the last node
        # marks the end of a word
        return node.isEnd()

    # Returns if there is any word in the
    # trie that starts with the given prefix
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                # If a letter is not found,
                # there is no word with the
                # given prefix
                return False
            # Move to the next node
            node = node.get(ch)
        # The prefix is found in the Trie
        return True

    # Count number of words with a given length
    def countWordsEqualTo(self, word):
        pass

    # Count number of words with a given prefix
    def countWordsStartingWith(self, prefix):
        pass

    # Delete a word from the Trie
    def erase(self, word):
        pass


if __name__ == "__main__":
    trie = Trie()

    # Insert words into the Trie.
    words = ["hello", "hell", "heaven", "heavy"]
    for word in words:
        trie.insert(word)

    # Search for complete words.
    print("Search Results:")
    print("Is 'hell' in the trie?", trie.search("hell"))      # True
    print("Is 'hello' in the trie?", trie.search("hello"))    # True
    print("Is 'helloa' in the trie?", trie.search("helloa"))  # False

    # Check for prefixes.
    print("\nPrefix Checks:")
    print("Does any word start with 'he'?", trie.startsWith("he"))  # True
    print("Does any word start with 'hea'?", trie.startsWith("hea"))  # True
    print("Does any word start with 'hex'?", trie.startsWith("hex"))  # False

    # Deleting a word.
    # print("\nDeleting 'hell' from the trie.")
    # trie.delete("hell")
    # print("After deletion, is 'hell' in the trie?", trie.search("hell"))  # Should be False
    # Other words should still exist.
    print("Is 'hello' in the trie?", trie.search("hello"))              # Still True
    print("Is 'heavy' in the trie?", trie.search("heavy"))              # Still True
